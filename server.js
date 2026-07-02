const http = require('http');
const fs = require('fs');
const path = require('path');
const WebSocket = require('ws');

const PORT = 3000;

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

function broadcast(mensagem, remetente) {
  const texto = JSON.stringify(mensagem);
  wss.clients.forEach((cliente) => {
    if (cliente.readyState === WebSocket.OPEN) {
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
      jogadores[id] = {
        id, nome: msg.nome || 'Jogador',
        skin: msg.skin || {},
        x: 0, y: 0, z: 8, rotY: 0, andando: false
      };
      ws.send(JSON.stringify({ tipo: 'bemvindo', id, jogadores }));
      broadcast({ tipo: 'entrou', jogador: jogadores[id] });
    }

    if (msg.tipo === 'mover' && jogadores[id]) {
      jogadores[id].x = msg.x;
      jogadores[id].y = msg.y;
      jogadores[id].z = msg.z;
      jogadores[id].rotY = msg.rotY;
      jogadores[id].andando = msg.andando;
      broadcast({ tipo: 'mover', id, x: msg.x, y: msg.y, z: msg.z, rotY: msg.rotY, andando: msg.andando });
    }

    if (msg.tipo === 'chat' && jogadores[id]) {
      broadcast({ tipo: 'chat', id, nome: jogadores[id].nome, texto: msg.texto });
    }

    if (msg.tipo === 'pular' && jogadores[id]) {
      broadcast({ tipo: 'pular', id });
    }
  });

  ws.on('close', () => {
    delete jogadores[id];
    broadcast({ tipo: 'saiu', id });
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
