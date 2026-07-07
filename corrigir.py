with open('public/batalha.html', 'r') as f:
    conteudo = f.read()

antigo = """function tentarEspecial() {
  if (cooldownEspecial > 0 || !vivo || !ws || ws.readyState !== WebSocket.OPEN) return;
  cooldownEspecial = 150;
  let alvoMaisProximo = null;
  let menorDist = 8;
  Object.entries(outrosJogadores).forEach(([id, j]) => {
    const d = distanciaEntre(grupoPersonagem.position, j.modelo.grupo.position);
    if (d < menorDist) { menorDist = d; alvoMaisProximo = id; }
  });
  if (alvoMaisProximo) {
    ws.send(JSON.stringify({ tipo: 'socar', alvoId: alvoMaisProximo, dano: 25 }));
  }
}"""

novo = """function tentarEspecial() {
  if (cooldownEspecial > 0 || !vivo || !ws || ws.readyState !== WebSocket.OPEN) return;

  if (personagemEscolhido === 'vilao' || personagemEscolhido === 'heroi') {
    cooldownEspecial = 600;
    ws.send(JSON.stringify({ tipo: 'time_stop' }));
    return;
  }

  cooldownEspecial = 150;
  let alvoMaisProximo = null;
  let menorDist = 8;
  Object.entries(outrosJogadores).forEach(([id, j]) => {
    const d = distanciaEntre(grupoPersonagem.position, j.modelo.grupo.position);
    if (d < menorDist) { menorDist = d; alvoMaisProximo = id; }
  });
  if (alvoMaisProximo) {
    ws.send(JSON.stringify({ tipo: 'socar', alvoId: alvoMaisProximo, dano: 25 }));
  }
}"""

if antigo in conteudo:
    conteudo = conteudo.replace(antigo, novo, 1)
    with open('public/batalha.html', 'w') as f:
        f.write(conteudo)
    print('SUBSTITUIDO COM SUCESSO')
else:
    print('ERRO: texto antigo nao encontrado, nada foi mudado')
