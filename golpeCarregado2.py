with open('public/batalha.html', 'r') as f:
    conteudo = f.read()

antigo = """function socoUnico() {
  animandoSoco = 10;
  tentarSocar();
}"""

novo = """function socoUnico() {
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
  tentarSocar();
}

function tentarGolpeForte() {
  if (!vivo || !ws || ws.readyState !== WebSocket.OPEN) return;
  let alvoId = null;
  let menorDist = 4.5;
  Object.entries(outrosJogadores).forEach(([id, j]) => {
    const d = distanciaEntre(grupoPersonagem.position, j.modelo.grupo.position);
    if (d < menorDist) { menorDist = d; alvoId = id; }
  });
  if (alvoId) {
    tremidaTela = 12;
    ws.send(JSON.stringify({ tipo: 'socar', alvoId: alvoId, dano: 16 }));
  }
}"""

if antigo in conteudo:
    conteudo = conteudo.replace(antigo, novo, 1)
    print('ok')
else:
    print('ERRO')

with open('public/batalha.html', 'w') as f:
    f.write(conteudo)
