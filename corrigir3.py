with open('public/batalha.html', 'r') as f:
    conteudo = f.read()

antigo = """  const offsetX = distancia * Math.sin(anguloUsar);
  const offsetZ = distancia * Math.cos(anguloUsar);
  const alturaExtra = atrasLateral ? -0.3 : 0;
  const alvoX = grupoPersonagem.position.x + offsetX;
  const alvoY = grupoPersonagem.position.y + alturaExtra;
  const alvoZ = grupoPersonagem.position.z + offsetZ;
  const suavidade = atacando ? 0.5 : 0.15;
  meuStand.grupo.position.x = THREE.MathUtils.lerp(meuStand.grupo.position.x, alvoX, suavidade);
  meuStand.grupo.position.y = THREE.MathUtils.lerp(meuStand.grupo.position.y, alvoY, suavidade);
  meuStand.grupo.position.z = THREE.MathUtils.lerp(meuStand.grupo.position.z, alvoZ, suavidade);
  meuStand.grupo.rotation.y = THREE.MathUtils.lerp(meuStand.grupo.rotation.y, anguloUsar, suavidade);
}"""

novo = """  const offsetX = distancia * Math.sin(anguloUsar);
  const offsetZ = distancia * Math.cos(anguloUsar);
  const alvoX = grupoPersonagem.position.x + offsetX;
  const alvoY = grupoPersonagem.position.y;
  const alvoZ = grupoPersonagem.position.z + offsetZ;
  const rotacaoAlvo = atacando ? anguloUsar : grupoPersonagem.rotation.y;
  const suavidade = atacando ? 0.5 : 0.15;
  meuStand.grupo.position.x = THREE.MathUtils.lerp(meuStand.grupo.position.x, alvoX, suavidade);
  meuStand.grupo.position.y = THREE.MathUtils.lerp(meuStand.grupo.position.y, alvoY, suavidade);
  meuStand.grupo.position.z = THREE.MathUtils.lerp(meuStand.grupo.position.z, alvoZ, suavidade);
  meuStand.grupo.rotation.y = THREE.MathUtils.lerp(meuStand.grupo.rotation.y, rotacaoAlvo, suavidade);
}"""

if antigo in conteudo:
    conteudo = conteudo.replace(antigo, novo, 1)
    print('ok')
else:
    print('ERRO: nao encontrado')

with open('public/batalha.html', 'w') as f:
    f.write(conteudo)
