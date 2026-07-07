with open('public/batalha.html', 'r') as f:
    conteudo = f.read()

antigo1 = """function tentarSocar() {
  if (cooldownSoco > 0 || !vivo || !ws || ws.readyState !== WebSocket.OPEN) return;
  cooldownSoco = 25;
  ganharCargaUltimate(6);"""
novo1 = """function tentarSocar() {
  if (cooldownSoco > 0 || !vivo || !ws || ws.readyState !== WebSocket.OPEN) return;
  cooldownSoco = 25;"""
if antigo1 in conteudo:
    conteudo = conteudo.replace(antigo1, novo1, 1)
    print('ok 1')
else:
    print('ERRO 1')

antigo2 = """      } else if (outrosJogadores[msg.id]) {
        outrosJogadores[msg.id].vida = msg.vida;
        if (msg.atacante === meuId) efeitoImpacto();
      }
    }"""
novo2 = """      } else if (outrosJogadores[msg.id]) {
        outrosJogadores[msg.id].vida = msg.vida;
        if (msg.atacante === meuId) {
          efeitoImpacto();
          ganharCargaUltimate(10);
        }
      }
    }"""
if antigo2 in conteudo:
    conteudo = conteudo.replace(antigo2, novo2, 1)
    print('ok 2')
else:
    print('ERRO 2')

with open('public/batalha.html', 'w') as f:
    f.write(conteudo)
