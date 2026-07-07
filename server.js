const http = require('http');
const fs = require('fs');
const path = require('path');
const WebSocket = require('ws');

const PORT = process.env.PORT || 3000;

const MIME_TYPES = {
  '.html': 'text/html',
  '.js': 'text/javascript',
  '.css': 'text/css',
  '.json': 'application/json',
};

const server = http.createServer((req, res) => {
  let filePath = req.url === '/' ? '/index.html' : req.url;
  filePath = path.join(__dirname, 'public', filePath);

  const ext = path.extname(filePath);
  const contentType = MIME_TYPES[ext] || 'application/octet-stream';

  fs.readFile(filePath, (err, content) => {
    if (err) {
      res.writeHead(404);
      res.end('Arquivo nao encontrado: ' + req.url);
      return;
    }
    res.writeHead(200, { 'Content-Type': contentType });
    res.end(content);
  });
});

const wss = new WebSocket.Server({ server });
const jogadores = {};
const ipsBanidos = new Set();
const historicoAcoes = {};

function pegarIP(req) {
  const forwardedFor = req.headers['x-forwarded-for'];
  if (forwardedFor) return forwardedFor.split(',')[0].trim();
  return req.socket.remoteAddress;
}

function acaoSuspeita(ip) {
  const agora = Date.now();
  if (!historicoAcoes[ip]) historicoAcoes[ip] = { tempos: [], avisos: 0 };
  const registro = historicoAcoes[ip];
  registro.tempos = registro.tempos.filter(t => agora - t < 1000);
  registro.tempos.push(agora);
  if (registro.tempos.length > 15) {
    registro.avisos++;
    if (registro.avisos >= 3) {
      ipsBanidos.add(ip);
      return true;
    }
  }
  return false;
}

function broadcastSala(sala, mensagem) {
  const texto = JSON.stringify(mensagem);
  wss.clients.forEach((cliente) => {
    if (cliente.readyState === WebSocket.OPEN && cliente.sala === sala) {
      cliente.send(texto);
    }
  });
}

wss.on('connection', (ws, req) => {
  const ip = pegarIP(req);
  ws.ipCliente = ip;
  if (ipsBanidos.has(ip)) {
    ws.close(1008, 'Banido por comportamento suspeito');
    return;
  }

  ws.vivo = true;
  ws.on('pong', () => { ws.vivo = true; });

  const id = Math.random().toString(36).substring(2, 10);

  ws.on('message', (dados) => {
    let msg;
    try { msg = JSON.parse(dados); } catch (e) { return; }

    const tiposMonitorados = ['socar', 'ultimate', 'time_stop'];
    if (tiposMonitorados.includes(msg.tipo) && acaoSuspeita(ws.ipCliente)) {
      ws.close(1008, 'Banido por comportamento suspeito');
      return;
    }

    if (msg.tipo === 'entrar') {
      const sala = msg.sala || 'blocos';
      ws.sala = sala;
      const personagensComStand = ['vilao', 'heroi', 'vidente'];
      const vidaInicial = personagensComStand.includes(msg.personagem) ? 130 : 100;
      jogadores[id] = {
        id, nome: msg.nome || 'Jogador',
        skin: msg.skin || {},
        personagem: msg.personagem || null,
        x: 0, y: 0, z: 8, rotY: 0, andando: false,
        vida: vidaInicial, vidaMax: vidaInicial, sala
      };
      ws.send(JSON.stringify({ tipo: 'bemvindo', id, jogadores: Object.fromEntries(Object.entries(jogadores).filter(([_, j]) => j.sala === sala)) }));
      broadcastSala(sala, { tipo: 'entrou', jogador: jogadores[id] });
    }

    if (msg.tipo === 'mover' && jogadores[id]) {
      jogadores[id].x = msg.x;
      jogadores[id].y = msg.y;
      jogadores[id].z = msg.z;
      jogadores[id].rotY = msg.rotY;
      jogadores[id].andando = msg.andando;
      broadcastSala(jogadores[id].sala, { tipo: 'mover', id, x: msg.x, y: msg.y, z: msg.z, rotY: msg.rotY, andando: msg.andando });
    }

    if (msg.tipo === 'chat' && jogadores[id]) {
      broadcastSala(jogadores[id].sala, { tipo: 'chat', id, nome: jogadores[id].nome, texto: msg.texto });
    }

    if (msg.tipo === 'pular' && jogadores[id]) {
      broadcastSala(jogadores[id].sala, { tipo: 'pular', id });
    }

    if (msg.tipo === 'time_stop' && jogadores[id]) {
      broadcastSala(jogadores[id].sala, { tipo: 'tempo_parado', id, duracao: 3000 });
    }

    if (msg.tipo === 'ultimate' && jogadores[id]) {
      broadcastSala(jogadores[id].sala, { tipo: 'ultimate_usado', id, personagem: msg.personagem });
      Object.values(jogadores).forEach((alvo) => {
        if (alvo.id === id || alvo.sala !== jogadores[id].sala) return;
        const dx = alvo.x - jogadores[id].x;
        const dz = alvo.z - jogadores[id].z;
        const dist = Math.sqrt(dx * dx + dz * dz);
        if (dist < 8 && alvo.vida > 0) {
          alvo.vida = Math.max(0, alvo.vida - 35);
          broadcastSala(jogadores[id].sala, { tipo: 'dano', id: alvo.id, vida: alvo.vida, atacante: id });
          if (alvo.vida === 0) {
            broadcastSala(jogadores[id].sala, { tipo: 'nocaute', id: alvo.id, atacante: id });
            setTimeout(() => {
              if (jogadores[alvo.id]) {
                jogadores[alvo.id].vida = jogadores[alvo.id].vidaMax || 100;
                broadcastSala(jogadores[id].sala, { tipo: 'reviveu', id: alvo.id, vida: jogadores[alvo.id].vida });
              }
            }, 3000);
          }
        }
      });
    }

    if (msg.tipo === 'socar' && jogadores[id] && jogadores[msg.alvoId] && jogadores[msg.alvoId].sala === jogadores[id].sala) {
      const alvo = jogadores[msg.alvoId];
      const danoPermitido = [8, 16, 25].includes(msg.dano) ? msg.dano : 8;
      if (alvo.vida > 0 && msg.alvoId !== id) {
        alvo.vida = Math.max(0, alvo.vida - danoPermitido);
        broadcastSala(jogadores[id].sala, { tipo: 'dano', id: msg.alvoId, vida: alvo.vida, atacante: id });
        if (alvo.vida === 0) {
          broadcastSala(jogadores[id].sala, { tipo: 'nocaute', id: msg.alvoId, atacante: id });
          setTimeout(() => {
            if (jogadores[msg.alvoId]) {
              jogadores[msg.alvoId].vida = 100;
              broadcastSala(jogadores[id].sala, { tipo: 'reviveu', id: msg.alvoId, vida: 100 });
            }
          }, 3000);
        }
      }
    }
  });

  ws.on('close', () => {
    if (jogadores[id]) {
      broadcastSala(jogadores[id].sala, { tipo: 'saiu', id });
      delete jogadores[id];
    }
  });
});

const intervaloHeartbeat = setInterval(() => {
  wss.clients.forEach((cliente) => {
    if (cliente.vivo === false) {
      cliente.terminate();
      return;
    }
    cliente.vivo = false;
    cliente.ping();
  });
}, 3000);

server.listen(PORT, '0.0.0.0', () => {
  console.log(`Servidor rodando! Abre no navegador: http://localhost:${PORT}`);
});
