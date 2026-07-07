with open('server.js', 'r') as f:
    conteudo = f.read()

antigo = """    if (msg.tipo === 'time_stop' && jogadores[id]) {
      broadcastSala(jogadores[id].sala, { tipo: 'tempo_parado', id, duracao: 3000 });
    }"""

novo = """    if (msg.tipo === 'time_stop' && jogadores[id]) {
      broadcastSala(jogadores[id].sala, { tipo: 'tempo_parado', id, duracao: 3000 });
    }

    if (msg.tipo === 'ultimate' && jogadores[id]) {
      broadcastSala(jogadores[id].sala, { tipo: 'ultimate_usado', id, personagem: msg.personagem });
      Object.values(jogadores).forEach((alvo) => {
        if (alvo.id === id || alvo.sala !== jogadores[id].sala) return;
        const dx = alvo.x - jogadores[id].x;
        const dz = alvo.z - jogadores[id].z;
        const dist = Math.sqrt(dx * dx + dz * dz);
        if (dist < 8 && alvo.vida > 0) {
          alvo.vida = Math.max(0, alvo.vida - 35);
          broadcastSala(jogadores[id].sala, { tipo: 'dano', id: alvo.id, vida: alvo.vida, atacante: id });
          if (alvo.vida === 0) {
            broadcastSala(jogadores[id].sala, { tipo: 'nocaute', id: alvo.id, atacante: id });
            setTimeout(() => {
              if (jogadores[alvo.id]) {
                jogadores[alvo.id].vida = jogadores[alvo.id].vidaMax || 100;
                broadcastSala(jogadores[id].sala, { tipo: 'reviveu', id: alvo.id, vida: jogadores[alvo.id].vida });
              }
            }, 3000);
          }
        }
      });
    }"""

if antigo in conteudo:
    conteudo = conteudo.replace(antigo, novo, 1)
    print('ok D')
else:
    print('ERRO D')

with open('server.js', 'w') as f:
    f.write(conteudo)
