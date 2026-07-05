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

function broadcastSala(sala, mensagem) {
  const texto = JSON.stringify(mensagem);
  wss.clients.forEach((cliente) => {
    if (cliente.readyState === WebSocket.OPEN && cliente.sala === sala) {
      cliente.send(texto);
    }
  });
}

wss.on('connection', (ws) => {
  ws.vivo = true;
  ws.on('pong', () => { ws.vivo = true; });

  const id = Math.random().toString(36).substring(2, 10);

  ws.on('message', (dados) => {
    let msg;
    try { msg = JSON.parse(dados); } catch (e) { return; }

    if (msg.tipo === 'entrar') {
      const sala = msg.sala || 'blocos';
      ws.sala = sala;
      jogadores[id] = {
        id, nome: msg.nome || 'Jogador',
        skin: msg.skin || {},
        personagem: msg.personagem || null,
        x: 0, y: 0, z: 8, rotY: 0, andando: false,
        vida: 100, sala
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

    if (msg.tipo === 'socar' && jogadores[id] && jogadores[msg.alvoId]) {
      const alvo = jogadores[msg.alvoId];
      if (alvo.vida > 0) {
        alvo.vida = Math.max(0, alvo.vida - (msg.dano || 8));
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
