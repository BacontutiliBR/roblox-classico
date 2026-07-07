with open('public/batalha.html', 'r') as f:
    conteudo = f.read()

antigo = """  const anguloRepouso = grupoPersonagem.rotation.y + Math.PI - 0.9;
  let anguloUsar = anguloRepouso;
  let distancia = 2.4;"""

novo = """  const anguloRepouso = grupoPersonagem.rotation.y + Math.PI - 1.15;
  let anguloUsar = anguloRepouso;
  let distancia = 2.4;"""

if antigo in conteudo:
    conteudo = conteudo.replace(antigo, novo, 1)
    print('ok parte 1')
else:
    print('ERRO parte 1')

antigo2 = """  const alvoX = grupoPersonagem.position.x + offsetX;
  const alvoY = grupoPersonagem.position.y;
  const alvoZ = grupoPersonagem.position.z + offsetZ;"""

novo2 = """  const alvoX = grupoPersonagem.position.x + offsetX;
  const alvoY = grupoPersonagem.position.y + 0.6;
  const alvoZ = grupoPersonagem.position.z + offsetZ;"""

if antigo2 in conteudo:
    conteudo = conteudo.replace(antigo2, novo2, 1)
    print('ok parte 2')
else:
    print('ERRO parte 2')

with open('public/batalha.html', 'w') as f:
    f.write(conteudo)
