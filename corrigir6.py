with open('public/batalha.html', 'r') as f:
    conteudo = f.read()

antigo = """const PERSONAGENS = {
  vilao: { nome: 'Time Stop Villain', corPele: '#e8c39e', corCamisa: '#4a148c', corCalca: '#1a0a2a', corCabelo: '#f5e050' },
  heroi: { nome: 'Time Stop Hero', corPele: '#c99a6b', corCamisa: '#1565c0', corCalca: '#0d2b4a', corCabelo: '#1a1a1a' },
  vidente: { nome: 'Stardust Noob', corPele: '#e0b090', corCamisa: '#2e7d32', corCalca: '#1a3a1a', corCabelo: '#7a4a2a' }
};"""

novo = """const PERSONAGENS = {
  vilao: { nome: 'Time Stop Villain', corPele: '#e8c39e', corCamisa: '#4a148c', corCalca: '#1a0a2a', corCabelo: '#f5e050', temStand: true },
  heroi: { nome: 'Time Stop Hero', corPele: '#c99a6b', corCamisa: '#1565c0', corCalca: '#0d2b4a', corCabelo: '#1a1a1a', temStand: true },
  vidente: { nome: 'Stardust Noob', corPele: '#e0b090', corCamisa: '#2e7d32', corCalca: '#1a3a1a', corCabelo: '#7a4a2a', temStand: true },
  bolhas: { nome: 'Master of Bubbles', corPele: '#f0d0a0', corCamisa: '#e0e0e0', corCalca: '#2a2a2a', corCabelo: '#2a2a2a', temStand: false },
  respiro1: { nome: 'User of Vital Breath', corPele: '#d4a878', corCamisa: '#5d4037', corCalca: '#3e2723', corCabelo: '#3a2a1a', temStand: false },
  respiro2: { nome: 'Guardian of Breath', corPele: '#e8c39e', corCamisa: '#795548', corCalca: '#4e342e', corCabelo: '#1a1a1a', temStand: false }
};"""

if antigo in conteudo:
    conteudo = conteudo.replace(antigo, novo, 1)
    print('ok')
else:
    print('ERRO: nao encontrado')

with open('public/batalha.html', 'w') as f:
    f.write(conteudo)
