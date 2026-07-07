with open('public/batalha.html', 'r') as f:
    conteudo = f.read()

antigo1 = "function efeitoImpacto() {"
novo1 = """let particulasAtivas = [];
function criarParticulaImpacto(pos, cor) {
  for (let i = 0; i < 7; i++) {
    const p = new THREE.Mesh(
      new THREE.BoxGeometry(0.22, 0.22, 0.22),
      new THREE.MeshBasicMaterial({ color: cor, transparent: true, opacity: 1 })
    );
    p.position.copy(pos);
    const ang = Math.random() * Math.PI * 2;
    const forca = 0.06 + Math.random() * 0.06;
    const vel = new THREE.Vector3(Math.cos(ang) * forca, Math.random() * 0.1 + 0.04, Math.sin(ang) * forca);
    scene.add(p);
    particulasAtivas.push({ mesh: p, vel, vida: 22, vidaMax: 22 });
  }
}

function efeitoImpacto() {"""

if antigo1 in conteudo:
    conteudo = conteudo.replace(antigo1, novo1, 1)
    print('ok 1')
else:
    print('ERRO 1')

antigo2 = """    if (msg.tipo === 'dano') {
      if (msg.id === meuId) {
        meuVida = msg.vida;
        const percentual = Math.max(0, (meuVida / meuVidaMax) * 100);
        document.getElementById('barra-vida-frente').style.width = percentual + '%';
        if (percentual <= 30) document.getElementById('barra-vida-frente').style.background = '#d32f2f';
        efeitoImpacto();
      } else if (outrosJogadores[msg.id]) {
        outrosJogadores[msg.id].vida = msg.vida;
        if (msg.atacante === meuId) {
          efeitoImpacto();
          ganharCargaUltimate(10);
        }
      }
    }"""

novo2 = """    if (msg.tipo === 'dano') {
      if (msg.id === meuId) {
        meuVida = msg.vida;
        const percentual = Math.max(0, (meuVida / meuVidaMax) * 100);
        document.getElementById('barra-vida-frente').style.width = percentual + '%';
        if (percentual <= 30) document.getElementById('barra-vida-frente').style.background = '#d32f2f';
        efeitoImpacto();
        const posImpacto = grupoPersonagem.position.clone();
        posImpacto.y += 3;
        criarParticulaImpacto(posImpacto, 0xff5252);
      } else if (outrosJogadores[msg.id]) {
        outrosJogadores[msg.id].vida = msg.vida;
        if (msg.atacante === meuId) {
          efeitoImpacto();
          ganharCargaUltimate(10);
          const posImpacto2 = outrosJogadores[msg.id].modelo.grupo.position.clone();
          posImpacto2.y += 3;
          criarParticulaImpacto(posImpacto2, 0xffca28);
        }
      }
    }"""

if antigo2 in conteudo:
    conteudo = conteudo.replace(antigo2, novo2, 1)
    print('ok 2')
else:
    print('ERRO 2')

antigo3 = "  renderer.render(scene, camera);"
novo3 = """  particulasAtivas = particulasAtivas.filter((part) => {
    part.mesh.position.add(part.vel);
    part.vel.y -= 0.008;
    part.vida--;
    part.mesh.material.opacity = Math.max(0, part.vida / part.vidaMax);
    if (part.vida <= 0) { scene.remove(part.mesh); return false; }
    return true;
  });

  renderer.render(scene, camera);"""

if antigo3 in conteudo:
    conteudo = conteudo.replace(antigo3, novo3, 1)
    print('ok 3')
else:
    print('ERRO 3')

with open('public/batalha.html', 'w') as f:
    f.write(conteudo)
