with open('public/batalha.html', 'r') as f:
    conteudo = f.read()

antigo1 = "let cooldownEspecial = 0;"
novo1 = "let cooldownEspecial = 0;\nlet cargaUltimate = 0;\nconst CARGA_MAXIMA = 100;"
if antigo1 in conteudo:
    conteudo = conteudo.replace(antigo1, novo1, 1)
    print('ok B1')
else:
    print('ERRO B1')

antigo2 = """function tentarSocar() {
  if (cooldownSoco > 0 || !vivo || !ws || ws.readyState !== WebSocket.OPEN) return;
  cooldownSoco = 25;"""
novo2 = """function ganharCargaUltimate(quantia) {
  cargaUltimate = Math.min(CARGA_MAXIMA, cargaUltimate + quantia);
  const barraEl = document.getElementById('barra-ultimate-frente');
  const btnUlt = document.getElementById('btn-ultimate');
  if (barraEl) barraEl.style.width = cargaUltimate + '%';
  if (cargaUltimate >= CARGA_MAXIMA && btnUlt) {
    btnUlt.disabled = false;
    btnUlt.style.background = 'rgba(255,202,40,0.7)';
  }
}

function tentarSocar() {
  if (cooldownSoco > 0 || !vivo || !ws || ws.readyState !== WebSocket.OPEN) return;
  cooldownSoco = 25;
  ganharCargaUltimate(6);"""
if antigo2 in conteudo:
    conteudo = conteudo.replace(antigo2, novo2, 1)
    print('ok B2')
else:
    print('ERRO B2')

with open('public/batalha.html', 'w') as f:
    f.write(conteudo)
