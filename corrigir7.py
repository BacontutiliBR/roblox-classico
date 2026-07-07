with open('public/batalha.html', 'r') as f:
    conteudo = f.read()

antigo = """    <div class="carta-personagem" data-id="vidente">
      <div class="icone-personagem" style="background:#2e7d32;">🔮</div>
      <div class="nome-personagem">Stardust Noob</div>
      <div class="desc-personagem">Ataque à distância teleguiado</div>
    </div>
  </div>"""

novo = """    <div class="carta-personagem" data-id="vidente">
      <div class="icone-personagem" style="background:#2e7d32;">🔮</div>
      <div class="nome-personagem">Stardust Noob</div>
      <div class="desc-personagem">Ataque à distância teleguiado</div>
    </div>
    <div class="carta-personagem" data-id="bolhas">
      <div class="icone-personagem" style="background:#01579b;">🫧</div>
      <div class="nome-personagem">Master of Bubbles</div>
      <div class="desc-personagem">Especial cura um pouco de vida</div>
    </div>
    <div class="carta-personagem" data-id="respiro1">
      <div class="icone-personagem" style="background:#c62828;">🌬️</div>
      <div class="nome-personagem">User of Vital Breath</div>
      <div class="desc-personagem">Socos com mais dano corpo a corpo</div>
    </div>
    <div class="carta-personagem" data-id="respiro2">
      <div class="icone-personagem" style="background:#ef6c00;">🌪️</div>
      <div class="nome-personagem">Guardian of Breath</div>
      <div class="desc-personagem">Cooldown de soco mais rápido</div>
    </div>
  </div>"""

if antigo in conteudo:
    conteudo = conteudo.replace(antigo, novo, 1)
    print('ok')
else:
    print('ERRO: nao encontrado')

with open('public/batalha.html', 'w') as f:
    f.write(conteudo)
