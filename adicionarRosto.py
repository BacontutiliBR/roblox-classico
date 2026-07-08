with open('public/batalha.html', 'r') as f:
    conteudo = f.read()

antigo = """  const cabeca = criarCaixa(1.2, 1.2, 1.2, skin.corPele);
  cabeca.position.y = 4.8;
  grupo.add(cabeca);"""

novo = """  const cabeca = criarCaixa(1.2, 1.2, 1.2, skin.corPele);
  cabeca.position.y = 4.8;
  grupo.add(cabeca);

  const materialRosto = new THREE.MeshBasicMaterial({ color: 0x222222 });
  const olhoEsquerdo = new THREE.Mesh(new THREE.BoxGeometry(0.12, 0.12, 0.05), materialRosto);
  olhoEsquerdo.position.set(-0.25, 4.9, 0.61);
  grupo.add(olhoEsquerdo);
  const olhoDireito = new THREE.Mesh(new THREE.BoxGeometry(0.12, 0.12, 0.05), materialRosto);
  olhoDireito.position.set(0.25, 4.9, 0.61);
  grupo.add(olhoDireito);

  const sorrisoGrupo = new THREE.Group();
  for (let i = -2; i <= 2; i++) {
    const ponto = new THREE.Mesh(new THREE.BoxGeometry(0.08, 0.08, 0.05), materialRosto);
    ponto.position.set(i * 0.09, -Math.abs(i) * 0.04, 0);
    sorrisoGrupo.add(ponto);
  }
  sorrisoGrupo.position.set(0, 4.55, 0.61);
  grupo.add(sorrisoGrupo);"""

if antigo in conteudo:
    conteudo = conteudo.replace(antigo, novo, 1)
    print('ok')
else:
    print('ERRO')

with open('public/batalha.html', 'w') as f:
    f.write(conteudo)
