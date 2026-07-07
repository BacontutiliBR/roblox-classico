with open('public/batalha.html', 'r') as f:
    conteudo = f.read()

antigo = """  const anguloRepouso = grupoPersonagem.rotation.y + Math.PI - 0.35;
  let anguloUsar = anguloRepouso;
  let distancia = 2.1;"""

novo = """  const anguloRepouso = grupoPersonagem.rotation.y + Math.PI - 0.9;
  let anguloUsar = anguloRepouso;
  let distancia = 2.4;"""

if antigo in conteudo:
    conteudo = conteudo.replace(antigo, novo, 1)
    print('ok')
else:
    print('ERRO: nao encontrado')

with open('public/batalha.html', 'w') as f:
    f.write(conteudo)
