with open('server.js', 'r') as f:
    conteudo = f.read()

antigo = """      jogadores[id] = {
        id, nome: msg.nome || 'Jogador',
        skin: msg.skin || {},
        personagem: msg.personagem || null,
        x: 0, y: 0, z: 8, rotY: 0, andando: false,
        vida: 100, sala
      };"""

novo = """      const personagensComStand = ['vilao', 'heroi', 'vidente'];
      const vidaInicial = personagensComStand.includes(msg.personagem) ? 130 : 100;
      jogadores[id] = {
        id, nome: msg.nome || 'Jogador',
        skin: msg.skin || {},
        personagem: msg.personagem || null,
        x: 0, y: 0, z: 8, rotY: 0, andando: false,
        vida: vidaInicial, vidaMax: vidaInicial, sala
      };"""

if antigo in conteudo:
    conteudo = conteudo.replace(antigo, novo, 1)
    print('ok server')
else:
    print('ERRO server')

with open('server.js', 'w') as f:
    f.write(conteudo)
