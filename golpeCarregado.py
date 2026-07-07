with open('public/batalha.html', 'r') as f:
    conteudo = f.read()

antigo1 = "let ladoSocoAlternado = false;"
novo1 = "let ladoSocoAlternado = false;\nlet ultimoSocoTempo = 0;\nlet cooldownGolpeForte = 0;"
if antigo1 in conteudo:
    conteudo = conteudo.replace(antigo1, novo1, 1)
    print('ok 1')
else:
    print('ERRO 1')

antigo2 = """function socoUnico() {
  animandoSoco = 10;
  ladoSocoAlternado = !ladoSocoAlternado;
  tentarSocar();
}"""

novo2 = """function socoUnico() {
  const agora2 = Date.now();
  const socoDuplo = (agora2 - ultimoSocoTempo) < 350;
  ultimoSocoTempo = agora2;

  if (socoDuplo && cooldownGolpeForte <= 0) {
    cooldownGolpeForte = 400;
    animandoSoco = 16;
    tentarGolpeForte();
    return;
  }

  animandoSoco = 10;
  ladoSocoAlternado = !ladoSocoAlternado;
  tentarSocar();
}

function tentarGolpeForte() {
  if (!vivo || !ws || ws.readyState !== WebSocket.OPEN) return;
  const alvo = acharAlvoMaisProximo(4.5);
  if (alvo) {
    tremidaTela = 12;
    ws.send(JSON.stringify({ tipo: 'socar', alvoId: Object.keys(outrosJogadores).find(k => outrosJogadores[k] === alvo), dano: 16 }));
  }
}"""

if antigo2 in conteudo:
    conteudo = conteudo.replace(antigo2, novo2, 1)
    print('ok 2')
else:
    print('ERRO 2')

with open('public/batalha.html', 'w') as f:
    f.write(conteudo)
