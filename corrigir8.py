with open('public/batalha.html', 'r') as f:
    conteudo = f.read()

antigo = """function criarOutroJogador(dados) {
  const skinBase = PERSONAGENS[dados.personagem] || PERSONAGENS.vilao;
  const modelo = criarPersonagemModelo(skinBase);
  modelo.grupo.position.set(dados.x || 0, dados.y || 0, dados.z || 8);

  const nomeSprite = document.createElement('div');
  nomeSprite.className = 'nome-flutuante';
  nomeSprite.textContent = (dados.nome || 'Jogador') + ' (' + skinBase.nome + ')';
  document.body.appendChild(nomeSprite);

  outrosJogadores[dados.id] = {
    modelo, bolha: criarBolhaElemento(), nomeSprite,
    alvoX: dados.x || 0, alvoY: dados.y || 0, alvoZ: dados.z || 8,
    alvoRotY: dados.rotY || 0, andando: false, tempoAnimacao: 0,
    vida: dados.vida != null ? dados.vida : 100
  };
}"""

novo = """function criarOutroJogador(dados) {
  const skinBase = PERSONAGENS[dados.personagem] || PERSONAGENS.vilao;
  const modelo = criarPersonagemModelo(skinBase);
  modelo.grupo.position.set(dados.x || 0, dados.y || 0, dados.z || 8);

  const nomeSprite = document.createElement('div');
  nomeSprite.className = 'nome-flutuante';
  nomeSprite.textContent = (dados.nome || 'Jogador') + ' (' + skinBase.nome + ')';
  document.body.appendChild(nomeSprite);

  const corStandOutro = { vilao: 0x9c27b0, heroi: 0x2196f3, vidente: 0x4caf50 }[dados.personagem] || null;
  const standOutro = skinBase.temStand ? criarStand(corStandOutro) : null;

  outrosJogadores[dados.id] = {
    modelo, bolha: criarBolhaElemento(), nomeSprite,
    alvoX: dados.x || 0, alvoY: dados.y || 0, alvoZ: dados.z || 8,
    alvoRotY: dados.rotY || 0, andando: false, tempoAnimacao: 0,
    vida: dados.vida != null ? dados.vida : 100,
    stand: standOutro, animandoSocoOutro: 0
  };
}"""

if antigo in conteudo:
    conteudo = conteudo.replace(antigo, novo, 1)
    print('ok parte 1')
else:
    print('ERRO parte 1')

antigo2 = """function removerOutroJogador(id) {
  const j = outrosJogadores[id];
  if (!j) return;
  scene.remove(j.modelo.grupo);
  j.bolha.remove();
  j.nomeSprite.remove();
  delete outrosJogadores[id];
}"""

novo2 = """function removerOutroJogador(id) {
  const j = outrosJogadores[id];
  if (!j) return;
  scene.remove(j.modelo.grupo);
  if (j.stand) scene.remove(j.stand.grupo);
  j.bolha.remove();
  j.nomeSprite.remove();
  delete outrosJogadores[id];
}"""

if antigo2 in conteudo:
    conteudo = conteudo.replace(antigo2, novo2, 1)
    print('ok parte 2')
else:
    print('ERRO parte 2')

with open('public/batalha.html', 'w') as f:
    f.write(conteudo)
