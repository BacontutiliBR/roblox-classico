with open('server.js', 'r') as f:
    conteudo = f.read()

antigo = """    if (msg.tipo === 'ultimate' && jogadores[id]) {
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

novo = """    if (msg.tipo === 'ultimate' && jogadores[id]) {
      const eu = jogadores[id];
      const personagem = msg.personagem;

      if (personagem === 'vilao') {
        broadcastSala(eu.sala, { tipo: 'ultimate_usado', id, personagem });
        broadcastSala(eu.sala, { tipo: 'tempo_parado', id, duracao: 5000 });
        Object.values(jogadores).forEach((alvo) => {
          if (alvo.id === id || alvo.sala !== eu.sala || alvo.vida <= 0) return;
          const dx = alvo.x - eu.x;
          const dz = alvo.z - eu.z;
          if (Math.sqrt(dx * dx + dz * dz) < 9) {
            alvo.vida = Math.max(0, alvo.vida - 40);
            broadcastSala(eu.sala, { tipo: 'dano', id: alvo.id, vida: alvo.vida, atacante: id });
            if (alvo.vida === 0) {
              broadcastSala(eu.sala, { tipo: 'nocaute', id: alvo.id, atacante: id });
              setTimeout(() => {
                if (jogadores[alvo.id]) {
                  jogadores[alvo.id].vida = jogadores[alvo.id].vidaMax || 100;
                  broadcastSala(eu.sala, { tipo: 'reviveu', id: alvo.id, vida: jogadores[alvo.id].vida });
                }
              }, 3000);
            }
          }
        });
        return;
      }

      if (personagem === 'heroi') {
        broadcastSala(eu.sala, { tipo: 'ultimate_usado', id, personagem });
        broadcastSala(eu.sala, { tipo: 'tempo_parado', id, duracao: 4000 });
        return;
      }

      if (personagem === 'vidente') {
        broadcastSala(eu.sala, { tipo: 'ultimate_usado', id, personagem });
        let alvoMaisProximo = null;
        let menorDist = 10;
        Object.values(jogadores).forEach((alvo) => {
          if (alvo.id === id || alvo.sala !== eu.sala || alvo.vida <= 0) return;
          const dx = alvo.x - eu.x;
          const dz = alvo.z - eu.z;
          const dist = Math.sqrt(dx * dx + dz * dz);
          if (dist < menorDist) { menorDist = dist; alvoMaisProximo = alvo; }
        });
        if (alvoMaisProximo) {
          [0, 300, 600].forEach((atraso) => {
            setTimeout(() => {
              if (!jogadores[alvoMaisProximo.id] || jogadores[alvoMaisProximo.id].vida <= 0) return;
              jogadores[alvoMaisProximo.id].vida = Math.max(0, jogadores[alvoMaisProximo.id].vida - 12);
              broadcastSala(eu.sala, { tipo: 'dano', id: alvoMaisProximo.id, vida: jogadores[alvoMaisProximo.id].vida, atacante: id });
              if (jogadores[alvoMaisProximo.id].vida === 0) {
                broadcastSala(eu.sala, { tipo: 'nocaute', id: alvoMaisProximo.id, atacante: id });
                setTimeout(() => {
                  if (jogadores[alvoMaisProximo.id]) {
                    jogadores[alvoMaisProximo.id].vida = jogadores[alvoMaisProximo.id].vidaMax || 100;
                    broadcastSala(eu.sala, { tipo: 'reviveu', id: alvoMaisProximo.id, vida: jogadores[alvoMaisProximo.id].vida });
                  }
                }, 3000);
              }
            }, atraso);
          });
        }
        return;
      }

      if (personagem === 'bolhas') {
        eu.vida = Math.min(eu.vidaMax || 100, eu.vida + 40);
        broadcastSala(eu.sala, { tipo: 'ultimate_usado', id, personagem });
        broadcastSala(eu.sala, { tipo: 'dano', id, vida: eu.vida, atacante: null });
        return;
      }

      if (personagem === 'respiro1' || personagem === 'respiro2') {
        broadcastSala(eu.sala, { tipo: 'ultimate_usado', id, personagem });
        broadcastSala(eu.sala, { tipo: 'buff_ativo', id, personagem });
        return;
      }

      broadcastSala(eu.sala, { tipo: 'ultimate_usado', id, personagem });
    }"""

if antigo in conteudo:
    conteudo = conteudo.replace(antigo, novo, 1)
    print('ok')
else:
    print('ERRO')

with open('server.js', 'w') as f:
    f.write(conteudo)
