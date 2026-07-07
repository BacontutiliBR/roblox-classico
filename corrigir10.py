with open('public/batalha.html', 'r') as f:
    conteudo = f.read()

antigo1 = "let meuVida = 100;"
novo1 = "let meuVida = 100;\nlet meuVidaMax = 100;"
if antigo1 in conteudo:
    conteudo = conteudo.replace(antigo1, novo1, 1)
    print('ok 1')
else:
    print('ERRO 1')

antigo2 = """  const skin = PERSONAGENS[personagemEscolhido];
  const modelo = criarPersonagemModelo(skin);"""
novo2 = """  const skin = PERSONAGENS[personagemEscolhido];
  meuVidaMax = skin.temStand ? 130 : 100;
  meuVida = meuVidaMax;
  const modelo = criarPersonagemModelo(skin);"""
if antigo2 in conteudo:
    conteudo = conteudo.replace(antigo2, novo2, 1)
    print('ok 2')
else:
    print('ERRO 2')

antigo3 = """      if (msg.id === meuId) {
        meuVida = msg.vida;
        document.getElementById('barra-vida-frente').style.width = meuVida + '%';
        if (meuVida <= 30) document.getElementById('barra-vida-frente').style.background = '#d32f2f';
        efeitoImpacto();"""
novo3 = """      if (msg.id === meuId) {
        meuVida = msg.vida;
        const percentual = Math.max(0, (meuVida / meuVidaMax) * 100);
        document.getElementById('barra-vida-frente').style.width = percentual + '%';
        if (percentual <= 30) document.getElementById('barra-vida-frente').style.background = '#d32f2f';
        efeitoImpacto();"""
if antigo3 in conteudo:
    conteudo = conteudo.replace(antigo3, novo3, 1)
    print('ok 3')
else:
    print('ERRO 3')

antigo4 = """        vivo = true;
        meuVida = 100;
        document.getElementById('barra-vida-frente').style.width = '100%';"""
novo4 = """        vivo = true;
        meuVida = meuVidaMax;
        document.getElementById('barra-vida-frente').style.width = '100%';"""
if antigo4 in conteudo:
    conteudo = conteudo.replace(antigo4, novo4, 1)
    print('ok 4')
else:
    print('ERRO 4')

with open('public/batalha.html', 'w') as f:
    f.write(conteudo)
