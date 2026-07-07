with open('public/batalha.html', 'r') as f:
    conteudo = f.read()

antigo = """    if (msg.tipo === 'saiu') removerOutroJogador(msg.id);"""

novo = """    if (msg.tipo === 'ultimate_usado') {
      const corUlt = { vilao: '#ffd600', heroi: '#9c27b0', vidente: '#4caf50', bolhas: '#01579b', respiro1: '#c62828', respiro2: '#ef6c00' }[msg.personagem] || '#ffffff';
      efeitoUltimate(corUlt);
    }
    if (msg.tipo === 'saiu') removerOutroJogador(msg.id);"""

if antigo in conteudo:
    conteudo = conteudo.replace(antigo, novo, 1)
    print('ok E1')
else:
    print('ERRO E1')

antigo2 = "function efeitoImpacto() {"
novo2 = """function efeitoUltimate(cor) {
  const flash = document.getElementById('flash-impacto');
  flash.style.transition = 'none';
  flash.style.background = cor;
  flash.style.opacity = '0.5';
  requestAnimationFrame(() => {
    flash.style.transition = 'opacity 0.6s';
    flash.style.opacity = '0';
  });
  setTimeout(() => { flash.style.background = 'white'; }, 700);
  tremidaTela = 20;
}

function efeitoImpacto() {"""

if antigo2 in conteudo:
    conteudo = conteudo.replace(antigo2, novo2, 1)
    print('ok E2')
else:
    print('ERRO E2')

with open('public/batalha.html', 'w') as f:
    f.write(conteudo)
