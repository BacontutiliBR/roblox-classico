with open('server.js', 'r') as f:
    conteudo = f.read()

antigo = "const jogadores = {};"
novo = """const jogadores = {};
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
}"""

if antigo in conteudo:
    conteudo = conteudo.replace(antigo, novo, 1)
    print('ok anticheat 1')
else:
    print('ERRO anticheat 1')

antigo2 = "wss.on('connection', (ws) => {"
novo2 = """wss.on('connection', (ws, req) => {
  const ip = pegarIP(req);
  ws.ipCliente = ip;
  if (ipsBanidos.has(ip)) {
    ws.close(1008, 'Banido por comportamento suspeito');
    return;
  }
"""
if antigo2 in conteudo:
    conteudo = conteudo.replace(antigo2, novo2, 1)
    print('ok anticheat 2')
else:
    print('ERRO anticheat 2')

antigo3 = "  ws.on('message', (dados) => {\n    let msg;\n    try { msg = JSON.parse(dados); } catch (e) { return; }"
novo3 = """  ws.on('message', (dados) => {
    if (acaoSuspeita(ws.ipCliente)) {
      ws.close(1008, 'Banido por comportamento suspeito');
      return;
    }
    let msg;
    try { msg = JSON.parse(dados); } catch (e) { return; }"""
if antigo3 in conteudo:
    conteudo = conteudo.replace(antigo3, novo3, 1)
    print('ok anticheat 3')
else:
    print('ERRO anticheat 3')

with open('server.js', 'w') as f:
    f.write(conteudo)
