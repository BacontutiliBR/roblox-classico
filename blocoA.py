with open('public/batalha.html', 'r') as f:
    conteudo = f.read()

antigo = """  <div id="barra-vida-wrap">
    <div id="barra-vida-nome">Você</div>
    <div id="barra-vida-fundo"><div id="barra-vida-frente"></div></div>
  </div>"""

novo = """  <div id="barra-vida-wrap">
    <div id="barra-vida-nome">Você</div>
    <div id="barra-vida-fundo"><div id="barra-vida-frente"></div></div>
    <div id="barra-ultimate-fundo" style="background:#222; height:8px; border-radius:0; margin-top:4px; border:1px solid #555;"><div id="barra-ultimate-frente" style="background:#ffca28; height:100%; width:0%;"></div></div>
  </div>"""

if antigo in conteudo:
    conteudo = conteudo.replace(antigo, novo, 1)
    print('ok A1')
else:
    print('ERRO A1')

antigo2 = """    <button id="btn-especial">ESPECIAL</button>"""
novo2 = """    <button id="btn-especial">ESPECIAL</button>
    <button id="btn-ultimate" disabled style="background:rgba(80,80,80,0.5);">ULT</button>"""
if antigo2 in conteudo:
    conteudo = conteudo.replace(antigo2, novo2, 1)
    print('ok A2')
else:
    print('ERRO A2')

with open('public/batalha.html', 'w') as f:
    f.write(conteudo)
