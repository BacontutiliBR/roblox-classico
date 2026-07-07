with open('public/batalha.html', 'r') as f:
    conteudo = f.read()

antigo = """function distanciaEntre(a, b) {"""
novo = """function usarUltimate() {
  if (cargaUltimate < CARGA_MAXIMA || !vivo || !ws || ws.readyState !== WebSocket.OPEN) return;
  cargaUltimate = 0;
  document.getElementById('barra-ultimate-frente').style.width = '0%';
  const btnUlt = document.getElementById('btn-ultimate');
  btnUlt.disabled = true;
  btnUlt.style.background = 'rgba(80,80,80,0.5);';
  ws.send(JSON.stringify({ tipo: 'ultimate', personagem: personagemEscolhido }));
}

document.getElementById('btn-ultimate').addEventListener('touchstart', (e) => { e.preventDefault(); usarUltimate(); });
document.getElementById('btn-ultimate').addEventListener('mousedown', () => usarUltimate());

function distanciaEntre(a, b) {"""

if antigo in conteudo:
    conteudo = conteudo.replace(antigo, novo, 1)
    print('ok C')
else:
    print('ERRO C')

with open('public/batalha.html', 'w') as f:
    f.write(conteudo)
