with open('public/batalha.html', 'r') as f:
    conteudo = f.read()

antigo1 = """  const skin = PERSONAGENS[personagemEscolhido];
  meuVidaMax = skin.temStand ? 130 : 100;
  meuVida = meuVidaMax;
  const modelo = criarPersonagemModelo(skin);"""

novo1 = """  const skin = PERSONAGENS[personagemEscolhido];
  meuVidaMax = skin.temStand ? 130 : 100;
  meuVida = meuVidaMax;
  const skinVisual = {
    corPele: skinSalva.corPele || skin.corPele,
    corCamisa: skinSalva.corCamisa || skin.corCamisa,
    corCalca: skinSalva.corCalca || skin.corCalca,
    corCabelo: skinSalva.corCabelo || skin.corCabelo
  };
  const modelo = criarPersonagemModelo(skinVisual);"""

if antigo1 in conteudo:
    conteudo = conteudo.replace(antigo1, novo1, 1)
    print('ok 1 - meu personagem')
else:
    print('ERRO 1')

antigo2 = """function criarOutroJogador(dados) {
  const skinBase = PERSONAGENS[dados.personagem] || PERSONAGENS.vilao;
  const modelo = criarPersonagemModelo(skinBase);"""

novo2 = """function criarOutroJogador(dados) {
  const skinBase = PERSONAGENS[dados.personagem] || PERSONAGENS.vilao;
  const skinVisualOutro = {
    corPele: (dados.skin && dados.skin.corPele) || skinBase.corPele,
    corCamisa: (dados.skin && dados.skin.corCamisa) || skinBase.corCamisa,
    corCalca: (dados.skin && dados.skin.corCalca) || skinBase.corCalca,
    corCabelo: (dados.skin && dados.skin.corCabelo) || skinBase.corCabelo
  };
  const modelo = criarPersonagemModelo(skinVisualOutro);"""

if antigo2 in conteudo:
    conteudo = conteudo.replace(antigo2, novo2, 1)
    print('ok 2 - outros jogadores')
else:
    print('ERRO 2')

with open('public/batalha.html', 'w') as f:
    f.write(conteudo)
