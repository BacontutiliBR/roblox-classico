with open('public/batalha.html', 'r') as f:
    conteudo = f.read()

# Corrige as cores do stand: vilao amarelo, heroi roxo
antigo1 = "const corStand = { vilao: 0x9c27b0, heroi: 0x2196f3, vidente: 0x4caf50 }[personagemEscolhido] || 0xffffff;"
novo1 = "const corStand = { vilao: 0xffd600, heroi: 0x9c27b0, vidente: 0x4caf50 }[personagemEscolhido] || 0xffffff;"
if antigo1 in conteudo:
    conteudo = conteudo.replace(antigo1, novo1, 1)
    print('ok cores locais')
else:
    print('ERRO cores locais')

antigo2 = "const corStandOutro = { vilao: 0x9c27b0, heroi: 0x2196f3, vidente: 0x4caf50 }[dados.personagem] || null;"
novo2 = "const corStandOutro = { vilao: 0xffd600, heroi: 0x9c27b0, vidente: 0x4caf50 }[dados.personagem] || null;"
if antigo2 in conteudo:
    conteudo = conteudo.replace(antigo2, novo2, 1)
    print('ok cores outros')
else:
    print('ERRO cores outros')

# Adiciona aura na funcao criarStand
antigo3 = """function criarStand(cor) {
  const stand = new THREE.Group();"""

novo3 = """function criarStand(cor) {
  const stand = new THREE.Group();
  const aura = new THREE.Mesh(
    new THREE.SphereGeometry(1.8, 12, 12),
    new THREE.MeshBasicMaterial({ color: cor, transparent: true, opacity: 0.12, depthWrite: false })
  );
  aura.position.y = 3.2;
  stand.add(aura);"""

if antigo3 in conteudo:
    conteudo = conteudo.replace(antigo3, novo3, 1)
    print('ok aura')
else:
    print('ERRO aura')

with open('public/batalha.html', 'w') as f:
    f.write(conteudo)
