with open('public/batalha.html', 'r') as f:
    conteudo = f.read()

antigo = """  const atacando = animandoSoco > 0;
  const anguloRepouso = grupoPersonagem.rotation.y - 0.6;
  let anguloUsar = anguloRepouso;
  let distancia = 1.7;
  let atrasLateral = true;"""

novo = """  const atacando = animandoSoco > 0;
  const anguloRepouso = grupoPersonagem.rotation.y + Math.PI - 0.35;
  let anguloUsar = anguloRepouso;
  let distancia = 2.1;
  let atrasLateral = true;"""

if antigo in conteudo:
    conteudo = conteudo.replace(antigo, novo, 1)
    print('parte 1 ok')
else:
    print('ERRO parte 1: nao encontrado')

antigo2 = """    } else {
      meuStand.bracoDirStand.rotation.x = THREE.MathUtils.lerp(meuStand.bracoDirStand.rotation.x, 0, 0.35);
      meuStand.bracoEsqStand.rotation.x = THREE.MathUtils.lerp(meuStand.bracoEsqStand.rotation.x, 0, 0.35);
    }
  }"""

novo2 = """    } else {
      meuStand.bracoDirStand.rotation.x = THREE.MathUtils.lerp(meuStand.bracoDirStand.rotation.x, -0.45, 0.2);
      meuStand.bracoEsqStand.rotation.x = THREE.MathUtils.lerp(meuStand.bracoEsqStand.rotation.x, -0.45, 0.2);
    }
  }"""

if antigo2 in conteudo:
    conteudo = conteudo.replace(antigo2, novo2, 1)
    print('parte 2 ok')
else:
    print('ERRO parte 2: nao encontrado')

with open('public/batalha.html', 'w') as f:
    f.write(conteudo)
