with open('public/batalha.html', 'r') as f:
    conteudo = f.read()

antigo1 = """  if (personagemEscolhido === 'vilao' || personagemEscolhido === 'heroi') {
    cooldownEspecial = 600;
    ws.send(JSON.stringify({ tipo: 'time_stop' }));
    return;
  }"""

novo1 = """  if (personagemEscolhido === 'vilao' || personagemEscolhido === 'heroi') {
    cooldownEspecial = 600;
    ws.send(JSON.stringify({ tipo: 'time_stop' }));
    const corPropria = personagemEscolhido === 'vilao' ? '#ffd600' : '#9c27b0';
    efeitoUltimate(corPropria);
    return;
  }"""

if antigo1 in conteudo:
    conteudo = conteudo.replace(antigo1, novo1, 1)
    print('ok 1')
else:
    print('ERRO 1')

antigo2 = """      congelado = true;
      document.getElementById('overlay-tempo-parado').style.display = 'block';
      document.getElementById('aviso-tempo-parado').style.display = 'block';"""

novo2 = """      congelado = true;
      document.getElementById('overlay-tempo-parado').style.display = 'block';
      document.getElementById('aviso-tempo-parado').style.display = 'block';
      tremidaTela = 15;"""

if antigo2 in conteudo:
    conteudo = conteudo.replace(antigo2, novo2, 1)
    print('ok 2')
else:
    print('ERRO 2')

with open('public/batalha.html', 'w') as f:
    f.write(conteudo)
