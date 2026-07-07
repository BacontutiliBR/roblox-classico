with open('public/batalha.html', 'r') as f:
    conteudo = f.read()

antigo = """chatEnviar.addEventListener('click', enviarMensagem);
chatInput.addEventListener('keydown', (e) => { if (e.key === 'Enter') enviarMensagem(); });"""

novo = """chatEnviar.addEventListener('click', enviarMensagem);
chatEnviar.addEventListener('touchstart', (e) => { e.preventDefault(); e.stopPropagation(); enviarMensagem(); });
chatInput.addEventListener('keydown', (e) => { if (e.key === 'Enter') enviarMensagem(); });
chatInput.addEventListener('touchstart', (e) => { e.stopPropagation(); });"""

if antigo in conteudo:
    conteudo = conteudo.replace(antigo, novo, 1)
    print('ok')
else:
    print('ERRO')

with open('public/batalha.html', 'w') as f:
    f.write(conteudo)
