with open('server.js', 'r') as f:
    conteudo = f.read()

antigo = """  ws.on('message', (dados) => {
    if (acaoSuspeita(ws.ipCliente)) {
      ws.close(1008, 'Banido por comportamento suspeito');
      return;
    }
    let msg;
    try { msg = JSON.parse(dados); } catch (e) { return; }"""

novo = """  ws.on('message', (dados) => {
    let msg;
    try { msg = JSON.parse(dados); } catch (e) { return; }

    const tiposMonitorados = ['socar', 'ultimate', 'time_stop'];
    if (tiposMonitorados.includes(msg.tipo) && acaoSuspeita(ws.ipCliente)) {
      ws.close(1008, 'Banido por comportamento suspeito');
      return;
    }"""

if antigo in conteudo:
    conteudo = conteudo.replace(antigo, novo, 1)
    print('ok')
else:
    print('ERRO')

with open('server.js', 'w') as f:
    f.write(conteudo)
