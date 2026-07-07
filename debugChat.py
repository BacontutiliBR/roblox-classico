with open('public/batalha.html', 'r') as f:
    conteudo = f.read()

antigo = """function enviarMensagem() {
  const texto = chatInput.value.trim();
  if (!texto || !ws || ws.readyState !== WebSocket.OPEN) return;
  ws.send(JSON.stringify({ tipo: 'chat', texto: texto }));
  chatInput.value = '';
}"""

novo = """function enviarMensagem() {
  alert('DEBUG: funcao chamada. texto=' + chatInput.value + ' ws=' + (ws ? ws.readyState : 'null'));
  const texto = chatInput.value.trim();
  if (!texto || !ws || ws.readyState !== WebSocket.OPEN) return;
  ws.send(JSON.stringify({ tipo: 'chat', texto: texto }));
  chatInput.value = '';
}"""

if antigo in conteudo:
    conteudo = conteudo.replace(antigo, novo, 1)
    print('ok')
else:
    print('ERRO')

with open('public/batalha.html', 'w') as f:
    f.write(conteudo)
