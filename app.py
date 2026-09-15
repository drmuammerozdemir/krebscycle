import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="Krebs Döngüsü & PDH İnteraktif İstasyon")

html_code = """
<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
  :root {
    --bg-main: #0e1117;
    --bg-card: #161b22;
    --border-color: #30363d;
    --text-main: #c9d1d9;
    --text-bright: #f0f6fc;
    --accent-blue: #58a6ff;
    --accent-green: #3fb950;
    --accent-purple: #bc8cff;
    --accent-red: #f85149;
    --accent-gold: #e3b341;
  }
  * { box-sizing: border-box; user-select: none; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
  body { background: var(--bg-main); color: var(--text-main); margin: 0; padding: 16px; }
  .container { display: flex; flex-direction: row; gap: 20px; max-width: 1550px; margin: 0 auto; }
  @media (max-width: 1080px) { .container { flex-direction: column; } }
  
  .panel {
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 12px;
    padding: 16px;
    flex: 1;
  }
  .panel h2 {
    margin: 0 0 12px 0;
    color: var(--text-bright);
    font-size: 1.15rem;
    border-bottom: 2px solid var(--border-color);
    padding-bottom: 8px;
    display: flex;
    justify-content: space-between;
  }
  
  /* Kelime Avı Grid */
  .grid-wrapper { display: flex; justify-content: center; margin-bottom: 12px; }
  .word-grid {
    display: grid;
    grid-template-columns: repeat(14, 28px);
    grid-gap: 3px;
    background: #090d13;
    padding: 8px;
    border-radius: 8px;
    border: 1px solid var(--border-color);
    touch-action: none;
  }
  .cell {
    width: 28px;
    height: 28px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 0.85rem;
    color: #8b949e;
    background: #21262d;
    border-radius: 4px;
    cursor: pointer;
  }
  .cell.selecting { background: #388bfd; color: #fff; }
  .cell.found-h { background: #1f6feb; color: #fff; }
  .cell.found-v { background: #238636; color: #fff; }
  .cell.found-both { background: #8957e5; color: #fff; }
  
  /* Token Parçalar */
  .tokens-area {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    padding: 10px;
    background: #0d1117;
    border: 1px dashed var(--border-color);
    border-radius: 8px;
    min-height: 80px;
  }
  .token {
    padding: 6px 12px;
    border-radius: 6px;
    font-size: 0.8rem;
    font-weight: 700;
    cursor: grab;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    border: 1px solid transparent;
  }
  .token:active { cursor: grabbing; }
  .token.metabolite { background: #1c2d42; color: #58a6ff; border-color: #388bfd55; }
  .token.cofactor { background: #2e1f47; color: #bc8cff; border-color: #8957e555; }
  .token.clinical { background: #421c24; color: #f85149; border-color: #f8514955; }
  .token.selected { outline: 2px solid #fff; }
  
  /* Sağ Taraf: Şema */
  .scheme-block {
    background: #0d1117;
    border: 1px solid var(--border-color);
    border-radius: 8px;
    padding: 12px;
    margin-bottom: 16px;
  }
  .scheme-title {
    font-size: 0.9rem;
    font-weight: 700;
    color: var(--accent-gold);
    margin-bottom: 8px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }
  
  /* Drop Zones */
  .drop-zone {
    min-width: 90px;
    height: 32px;
    border: 2px dashed #484f58;
    border-radius: 6px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 0.75rem;
    font-weight: 600;
    color: #6e7681;
    background: #161b22;
    padding: 2px 8px;
  }
  .drop-zone.over { border-color: var(--accent-gold); background: #262c36; }
  .drop-zone.filled { border-style: solid; }
  
  /* PDH Flex Düzeni */
  .pdh-flow {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 8px;
    flex-wrap: wrap;
  }
  .flow-item { text-align: center; }
  .flow-arrow { color: #8b949e; font-size: 1.2rem; }
  
  /* Krebs Dairesi Matrisi */
  .krebs-cycle-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 12px;
    text-align: center;
  }
  .cycle-node {
    background: #161b22;
    border: 1px solid var(--border-color);
    border-radius: 8px;
    padding: 8px;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 4px;
  }
  .node-label { font-size: 0.7rem; color: #8b949e; }
  
  .score-badge {
    background: #238636;
    color: #fff;
    padding: 2px 8px;
    border-radius: 12px;
    font-size: 0.8rem;
  }
</style>
</head>
<body>

<div class="container">
  <!-- SOL PANEL: KELİME AVI -->
  <div class="panel">
    <h2>
      <span>🧩 Kelime Avı (Maus veya Dokunmatik)</span>
      <span class="score-badge" id="found-count">0 / 12</span>
    </h2>
    <div class="grid-wrapper">
      <div class="word-grid" id="grid"></div>
    </div>
    <div style="font-size: 0.8rem; color: #8b949e; margin-bottom: 8px;">
      💡 Bulduğunuz kelimeler aşağıdaki panoda açılır. Masaüstünde sürükleyin, mobilde parçaya ardından sağdaki boş kutucuğa dokunun.
    </div>
    <div class="scheme-title">AÇILAN PARÇALAR</div>
    <div class="tokens-area" id="tokens-tray"></div>
  </div>

  <!-- SAĞ PANEL: PDH & KREBS DİYAGRAMI -->
  <div class="panel">
    <h2>
      <span>⚡ Şema Eşleme İstasyonu</span>
      <span class="score-badge" style="background: #1f6feb;" id="placed-count">0 / 12</span>
    </h2>

    <!-- PDH KÖPRÜSÜ -->
    <div class="scheme-block">
      <div class="scheme-title">1. Piruvat Dehidrojenaz (PDH) Köprüsü</div>
      <div class="pdh-flow">
        <div class="flow-item">
          <div style="font-weight:700; color:#fff;">PİRUVAT</div>
          <div style="font-size:0.7rem; color:#8b949e;">(Sitozolden Gelen)</div>
        </div>
        <div class="flow-arrow">➔</div>
        <div class="flow-item">
          <div class="node-label">E1 Kofaktörü (B1)</div>
          <div class="drop-zone" data-target="TPP">TPP ?</div>
        </div>
        <div class="flow-item">
          <div class="node-label">E2 Kofaktörü</div>
          <div class="drop-zone" data-target="LİPOİKASİT">Lipoik ?</div>
        </div>
        <div class="flow-item">
          <div class="node-label">Giren Kofaktör (B5)</div>
          <div class="drop-zone" data-target="KOENZİMA">KoA ?</div>
        </div>
        <div class="flow-arrow">➔</div>
        <div class="flow-item">
          <div class="node-label">Çıkan Taşıyıcı (B3)</div>
          <div class="drop-zone" data-target="NADH">İndirgenen ?</div>
        </div>
        <div class="flow-arrow">➔</div>
        <div class="flow-item">
          <div style="font-weight:700; color:var(--accent-green);">ASETİL-KoA</div>
          <div style="font-size:0.7rem; color:#8b949e;">(Döngüye Giriş)</div>
        </div>
      </div>

      <div style="display:flex; gap:12px; margin-top:10px; padding-top:8px; border-top:1px dashed #30363d;">
        <div style="display:flex; align-items:center; gap:6px;">
          <span style="font-size:0.75rem; color:#f85149; font-weight:700;">⚠️ E2 İnhibitörü:</span>
          <div class="drop-zone" data-target="ARSENİK">Toksik Ajan ?</div>
        </div>
        <div style="display:flex; align-items:center; gap:6px;">
          <span style="font-size:0.75rem; color:#f85149; font-weight:700;">⚠️ TPP Eksikliği:</span>
          <div class="drop-zone" data-target="BERİBERİ">Klinik Tablo ?</div>
        </div>
      </div>
    </div>

    <!-- KREBS DÖNGÜSÜ ŞEMASI -->
    <div class="scheme-block">
      <div class="scheme-title">2. Sitrik Asit Döngüsü & İnhibitörler</div>
      <div class="krebs-cycle-grid">
        <div class="cycle-node">
          <span class="node-label">1. Basamak (İlk Ürün - C6)</span>
          <div class="drop-zone" data-target="SİTRAT">1. Ürün ?</div>
        </div>
        <div class="cycle-node">
          <span class="node-label">⚠️ Akonitaz Blokajı</span>
          <div class="drop-zone" data-target="FLOROASETAT">İntihar İnhibitörü ?</div>
        </div>
        <div class="cycle-node">
          <span class="node-label">2. Basamak (İzomer - C6)</span>
          <div class="drop-zone" data-target="İZOSİTRAT">2. Ürün ?</div>
        </div>
        <div class="cycle-node">
          <span class="node-label">8. Basamak (Rejenerasyon - C4)</span>
          <div class="drop-zone" data-target="OKSALOASETAT">Başlangıç Omurgası ?</div>
        </div>
        <div style="display:flex; align-items:center; justify-content:center; font-weight:800; color:#8b949e;">
          TCA DÖNGÜSÜ
        </div>
        <div class="cycle-node">
          <span class="node-label">4. Basamak (GTP Öncülü - C4)</span>
          <div class="drop-zone" data-target="SÜKSİNİLKOA">Tiyoester Bağı ?</div>
        </div>
        <div class="cycle-node">
          <span class="node-label">7. Basamak (Mekik Taşıyıcısı - C4)</span>
          <div class="drop-zone" data-target="MALAT">Fumaraz Ürünü ?</div>
        </div>
        <div class="cycle-node">
          <span class="node-label">⚠️ Kompleks II İnhibitörü</span>
          <div class="drop-zone" data-target="MALONAT">Kompetitif Ajan ?</div>
        </div>
        <div class="cycle-node">
          <span class="node-label">5. Basamak (Kompleks II Substratı - C4)</span>
          <div class="drop-zone" data-target="SÜKSİNAT">FAD Redükleyen ?</div>
        </div>
      </div>
    </div>
  </div>
</div>

<script>
const WORDS = [
  { id: "SİTRAT", word: "SİTRAT", r: 0, c: 0, dir: "H", type: "metabolite" },
  { id: "MALONAT", word: "MALONAT", r: 1, c: 2, dir: "H", type: "clinical" },
  { id: "MALAT", word: "MALAT", r: 3, c: 4, dir: "H", type: "metabolite" },
  { id: "LİPOİKASİT", word: "LİPOİKASİT", r: 5, c: 0, dir: "H", type: "cofactor" },
  { id: "BERİBERİ", word: "BERİBERİ", r: 7, c: 3, dir: "H", type: "clinical" },
  { id: "FLOROASETAT", word: "FLOROASETAT", r: 9, c: 1, dir: "H", type: "clinical" },
  { id: "ARSENİK", word: "ARSENİK", r: 11, c: 0, dir: "H", type: "clinical" },
  { id: "İZOSİTRAT", word: "İZOSİTRAT", r: 2, c: 1, dir: "V", type: "metabolite" },
  { id: "OKSALOASETAT", word: "OKSALOASETAT", r: 1, c: 13, dir: "V", type: "metabolite" },
  { id: "SÜKSİNAT", word: "SÜKSİNAT", r: 4, c: 8, dir: "V", type: "metabolite" },
  { id: "SÜKSİNİLKOA", word: "SÜKSİNİLKOA", r: 0, c: 11, dir: "V", type: "metabolite" },
  { id: "TPP", word: "TPP", r: 10, c: 5, dir: "V", type: "cofactor" },
  { id: "NADH", word: "NADH", r: 0, c: 6, dir: "V", type: "cofactor" },
  { id: "KOENZİMA", word: "KOENZİMA", r: 6, c: 12, dir: "V", type: "cofactor" }
];

const GRID_SIZE = 14;
let grid = Array(GRID_SIZE).fill(null).map(() => Array(GRID_SIZE).fill(''));

// Harfleri yerleştir
WORDS.forEach(w => {
  for(let i = 0; i < w.word.length; i++) {
    let r = w.dir === "H" ? w.r : w.r + i;
    let c = w.dir === "H" ? w.c + i : w.c;
    if(r < GRID_SIZE && c < GRID_SIZE) grid[r][c] = w.word[i];
  }
});

const DUMMY = "ABCDEFGHİKLMNOPRSTUVYZ";
for(let r = 0; r < GRID_SIZE; r++) {
  for(let c = 0; c < GRID_SIZE; c++) {
    if(!grid[r][c]) grid[r][c] = DUMMY[Math.floor(Math.random() * DUMMY.length)];
  }
}

// Izgarayı çiz
const gridEl = document.getElementById("grid");
for(let r = 0; r < GRID_SIZE; r++) {
  for(let c = 0; c < GRID_SIZE; c++) {
    const d = document.createElement("div");
    d.className = "cell";
    d.dataset.r = r;
    d.dataset.c = c;
    d.textContent = grid[r][c];
    gridEl.appendChild(d);
  }
}

// Seçim mantığı (Mouse + Touch)
let isSelecting = false;
let startCell = null;
let currentSelection = [];
let foundWords = new Set();
let selectedToken = null;

function getCellFromPoint(x, y) {
  const el = document.elementFromPoint(x, y);
  return el && el.classList.contains("cell") ? el : null;
}

function handleStart(cell) {
  if(!cell) return;
  isSelecting = true;
  startCell = cell;
  currentSelection = [cell];
  cell.classList.add("selecting");
}

function handleMove(cell) {
  if(!isSelecting || !cell || !startCell) return;
  const sr = parseInt(startCell.dataset.r), sc = parseInt(startCell.dataset.c);
  const cr = parseInt(cell.dataset.r), cc = parseInt(cell.dataset.c);
  
  if (sr === cr || sc === cc) {
    document.querySelectorAll(".cell.selecting").forEach(c => c.classList.remove("selecting"));
    currentSelection = [];
    const rStep = sr === cr ? 0 : (cr > sr ? 1 : -1);
    const cStep = sc === cc ? 0 : (cc > sc ? 1 : -1);
    let r = sr, c = sc;
    while(true) {
      const el = document.querySelector(`.cell[data-r='${r}'][data-c='${c}']`);
      if(el) { el.classList.add("selecting"); currentSelection.push(el); }
      if(r === cr && c === cc) break;
      r += rStep; c += cStep;
    }
  }
}

function handleEnd() {
  if(!isSelecting) return;
  isSelecting = false;
  const wordStr = currentSelection.map(c => c.textContent).join("");
  const revStr = wordStr.split("").reverse().join("");
  
  WORDS.forEach(w => {
    if(!foundWords.has(w.id) && (w.word === wordStr || w.word === revStr)) {
      foundWords.add(w.id);
      currentSelection.forEach(c => {
        c.classList.remove("selecting");
        c.classList.add(w.dir === "H" ? "found-h" : "found-v");
      });
      unlockToken(w);
      document.getElementById("found-count").textContent = `${foundWords.size} / ${WORDS.length}`;
    }
  });
  document.querySelectorAll(".cell.selecting").forEach(c => c.classList.remove("selecting"));
  currentSelection = [];
}

gridEl.addEventListener("mousedown", e => handleStart(e.target));
window.addEventListener("mousemove", e => handleMove(getCellFromPoint(e.clientX, e.clientY)));
window.addEventListener("mouseup", handleEnd);

gridEl.addEventListener("touchstart", e => {
  const t = e.touches[0];
  handleStart(getCellFromPoint(t.clientX, t.clientY));
  e.preventDefault();
}, { passive: false });

window.addEventListener("touchmove", e => {
  if(!isSelecting) return;
  const t = e.touches[0];
  handleMove(getCellFromPoint(t.clientX, t.clientY));
}, { passive: false });

window.addEventListener("touchend", handleEnd);

// Token Panosuna Ekle
const tray = document.getElementById("tokens-tray");
function unlockToken(w) {
  const tok = document.createElement("div");
  tok.className = `token ${w.type}`;
  tok.textContent = `📦 ${w.word}`;
  tok.draggable = true;
  tok.dataset.word = w.id;

  tok.addEventListener("dragstart", e => {
    e.dataTransfer.setData("text/plain", w.id);
  });
  tok.addEventListener("click", () => {
    document.querySelectorAll(".token").forEach(t => t.classList.remove("selected"));
    selectedToken = tok;
    tok.classList.add("selected");
  });
  tray.appendChild(tok);
}

// Drop Zones Etkileşimi
let placedCount = 0;
document.querySelectorAll(".drop-zone").forEach(zone => {
  zone.addEventListener("dragover", e => { e.preventDefault(); zone.classList.add("over"); });
  zone.addEventListener("dragleave", () => zone.classList.remove("over"));
  zone.addEventListener("drop", e => {
    e.preventDefault();
    zone.classList.remove("over");
    const wordId = e.dataTransfer.getData("text/plain");
    checkAndPlace(zone, wordId);
  });
  zone.addEventListener("click", () => {
    if(selectedToken) {
      checkAndPlace(zone, selectedToken.dataset.word);
    }
  });
});

function checkAndPlace(zone, wordId) {
  if(zone.dataset.target === wordId) {
    zone.textContent = `✓ ${wordId}`;
    zone.classList.add("filled");
    zone.style.background = "#238636";
    zone.style.color = "#ffffff";
    zone.style.borderColor = "#3fb950";
    
    const tok = document.querySelector(`.token[data-word='${wordId}']`);
    if(tok) tok.remove();
    selectedToken = null;
    placedCount++;
    document.getElementById("placed-count").textContent = `${placedCount} / 12`;
  } else {
    zone.style.borderColor = "#f85149";
    setTimeout(() => { zone.style.borderColor = "#484f58"; }, 600);
  }
}
</script>
</body>
</html>
"""

components.html(html_code, height=960, scrolling=True)
