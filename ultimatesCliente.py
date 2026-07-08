with open('public/batalha.html', 'r') as f:
    conteudo = f.read()

antigo1 = """    if (msg.tipo === 'tempo_parado' && msg.id !== meuId) {"""
novo1 = """    if (msg.tipo === 'tempo_parado' && msg.id === meuId && personagemEscolhido === 'heroi') {
      liberdadeTempoParado = true;
      setTimeout(() => { liberdadeTempoParado = false; }, msg.duracao || 4000);
    }
    if (msg.tipo === 'tempo_parado' && msg.id !== meuId) {"""

if antigo1 in conteudo:
    conteudo = conteudo.replace(antigo1, novo1, 1)
    print('ok 1')
else:
    print('ERRO 1')

antigo2 = "let congelado = false;"
novo2 = "let congelado = false;\nlet liberdadeTempoParado = false;\nlet buffDanoDobrado = 0;\nlet buffCooldownRapido = 0;"
if antigo2 in conteudo:
    conteudo = conteudo.replace(antigo2, novo2, 1)
    print('ok 2')
else:
    print('ERRO 2')

antigo3 = """    if (msg.tipo === 'ultimate_usado') {"""
novo3 = """    if (msg.tipo === 'buff_ativo' && msg.id === meuId) {
      if (msg.personagem === 'respiro1') buffDanoDobrado = 400;
      if (msg.personagem === 'respiro2') buffCooldownRapido = 400;
    }
    if (msg.tipo === 'ultimate_usado') {"""
if antigo3 in conteudo:
    conteudo = conteudo.replace(antigo3, novo3, 1)
    print('ok 3')
else:
    print('ERRO 3')

with open('public/batalha.html', 'w') as f:
    f.write(conteudo)
