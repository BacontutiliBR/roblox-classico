with open('public/batalha.html', 'r') as f:
    conteudo = f.read()

antigo1 = "if (vivo && !congelado) {"
novo1 = "if (vivo && (!congelado || liberdadeTempoParado)) {"
if antigo1 in conteudo:
    conteudo = conteudo.replace(antigo1, novo1, 1)
    print('ok 1')
else:
    print('ERRO 1')

antigo2 = """function tentarSocar() {
  if (cooldownSoco > 0 || !vivo || !ws || ws.readyState !== WebSocket.OPEN) return;
  cooldownSoco = 25;"""
novo2 = """function tentarSocar() {
  if (cooldownSoco > 0 || !vivo || !ws || ws.readyState !== WebSocket.OPEN) return;
  cooldownSoco = buffCooldownRapido > 0 ? 10 : 25;"""
if antigo2 in conteudo:
    conteudo = conteudo.replace(antigo2, novo2, 1)
    print('ok 2')
else:
    print('ERRO 2')

antigo3 = """  if (alvoMaisProximo) {
    ws.send(JSON.stringify({ tipo: 'socar', alvoId: alvoMaisProximo, dano: 8 }));
  }
}"""
novo3 = """  if (alvoMaisProximo) {
    const danoFinal = buffDanoDobrado > 0 ? 16 : 8;
    ws.send(JSON.stringify({ tipo: 'socar', alvoId: alvoMaisProximo, dano: danoFinal }));
  }
}"""
if antigo3 in conteudo:
    conteudo = conteudo.replace(antigo3, novo3, 1)
    print('ok 3')
else:
    print('ERRO 3')

antigo4 = "if (cooldownEspecial > 0) cooldownEspecial--;"
novo4 = "if (cooldownEspecial > 0) cooldownEspecial--;\n  if (buffDanoDobrado > 0) buffDanoDobrado--;\n  if (buffCooldownRapido > 0) buffCooldownRapido--;"
if antigo4 in conteudo:
    conteudo = conteudo.replace(antigo4, novo4, 1)
    print('ok 4')
else:
    print('ERRO 4')

with open('public/batalha.html', 'w') as f:
    f.write(conteudo)
