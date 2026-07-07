with open('public/batalha.html', 'r') as f:
    conteudo = f.read()

antigo = """  const corStand = { vilao: 0xffd600, heroi: 0x9c27b0, vidente: 0x4caf50 }[personagemEscolhido] || 0xffffff;
  meuStand = criarStand(corStand);

  conectar(personagemEscolhido);"""

novo = """  const corStand = { vilao: 0xffd600, heroi: 0x9c27b0, vidente: 0x4caf50 }[personagemEscolhido] || 0xffffff;
  if (skin.temStand) {
    meuStand = criarStand(corStand);
  }

  conectar(personagemEscolhido);"""

if antigo in conteudo:
    conteudo = conteudo.replace(antigo, novo, 1)
    print('ok')
else:
    print('ERRO: nao encontrado')

with open('public/batalha.html', 'w') as f:
    f.write(conteudo)
