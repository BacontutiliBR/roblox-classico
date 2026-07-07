with open('server.js', 'r') as f:
    conteudo = f.read()

antigo = """    if (msg.tipo === 'socar' && jogadores[id] && jogadores[msg.alvoId]) {
      const alvo = jogadores[msg.alvoId];
      if (alvo.vida > 0) {
        alvo.vida = Math.max(0, alvo.vida - (msg.dano || 8));"""

novo = """    if (msg.tipo === 'socar' && jogadores[id] && jogadores[msg.alvoId] && jogadores[msg.alvoId].sala === jogadores[id].sala) {
      const alvo = jogadores[msg.alvoId];
      const danoPermitido = [8, 25].includes(msg.dano) ? msg.dano : 8;
      if (alvo.vida > 0 && msg.alvoId !== id) {
        alvo.vida = Math.max(0, alvo.vida - danoPermitido);"""

if antigo in conteudo:
    conteudo = conteudo.replace(antigo, novo, 1)
    print('ok seg 1')
else:
    print('ERRO seg 1')

with open('server.js', 'w') as f:
    f.write(conteudo)
