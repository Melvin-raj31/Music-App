from flask import Flask, render_template_string

app = Flask(__name__)

MUSICIANS = [
    {
        "name": "Melvin",
        "emoji": "🎤",
        "genre": "Rock",
        "era": "1970s–2k",
        "born": "1946, Zanzibar",
        "instrument": "Vocals, Piano",
        "tagline": "The Greatest Showman of Rock",
        "bio": "Farrokh Bulsara, known as Freddie Mercury, was the lead vocalist of Queen. Regarded as one of the greatest singers in history, he possessed a four-octave vocal range and a larger-than-life stage presence. His theatrical performances transformed rock concerts into unforgettable spectacles.",
        "known_for": ["Bohemian Rhapsody", "We Will Rock You", "Live Aid 1985"],
    },
    {
        "name": "Miles Davis",
        "emoji": "🎺",
        "genre": "Jazz",
        "era": "1940s–90s",
        "born": "1926, Illinois",
        "instrument": "Trumpet",
        "tagline": "The Prince of Darkness",
        "bio": "Miles Davis was an American jazz trumpeter widely considered one of the most influential musicians of the 20th century. He pioneered multiple major developments in jazz — bebop, cool jazz, hard bop, and jazz fusion. His album Kind of Blue remains the best-selling jazz record of all time.",
        "known_for": ["Kind of Blue", "Bitches Brew", "Birth of the Cool"],
    },
    {
        "name": "Aretha Franklin",
        "emoji": "👑",
        "genre": "Soul",
        "era": "1960s–2010s",
        "born": "1942, Memphis",
        "instrument": "Vocals, Piano",
        "tagline": "The Queen of Soul",
        "bio": "Aretha Louise Franklin was an American singer and pianist. The undisputed Queen of Soul, she was the first woman inducted into the Rock and Roll Hall of Fame and won 18 Grammy Awards. Her recording of Respect became an anthem of both the civil rights and women's movements.",
        "known_for": ["Respect", "Natural Woman", "Think"],
    },
    {
        "name": "Jimi Hendrix",
        "emoji": "🎸",
        "genre": "Rock",
        "era": "1960s",
        "born": "1942, Seattle",
        "instrument": "Electric Guitar",
        "tagline": "The Electric Wizard",
        "bio": "James Marshall Hendrix was an American guitarist who fundamentally changed what was possible on an electric guitar. His innovative use of feedback, distortion, and whammy-bar techniques created an entirely new sonic language. Despite a career lasting just four years, his influence is incalculable.",
        "known_for": ["Purple Haze", "Voodoo Child", "Woodstock 1969"],
    },
    {
        "name": "Johann Sebastian Bach",
        "emoji": "🎼",
        "genre": "Classical",
        "era": "1700s",
        "born": "1685, Eisenach",
        "instrument": "Organ, Harpsichord",
        "tagline": "Father of Western Music",
        "bio": "Johann Sebastian Bach was a German composer of the late Baroque period, considered one of the greatest composers of all time. His intricate counterpoint and harmonic language remain unmatched. He composed over 1,000 works. Western music theory is built on the foundations he established.",
        "known_for": ["Brandenburg Concertos", "Goldberg Variations", "Mass in B Minor"],
    },
    {
        "name": "David Bowie",
        "emoji": "⚡",
        "genre": "Rock",
        "era": "1970s–2010s",
        "born": "1947, London",
        "instrument": "Vocals, Guitar",
        "tagline": "The Chameleon of Rock",
        "bio": "David Bowie was an English singer-songwriter celebrated for his constant reinvention across five decades. From glam-rock Ziggy Stardust to soul-influenced Young Americans, Bowie blurred the boundaries between music, art, and fashion. He remained creatively restless until his final album Blackstar.",
        "known_for": ["Heroes", "Space Oddity", "Ziggy Stardust"],
    },
    {
        "name": "Nina Simone",
        "emoji": "🎹",
        "genre": "Jazz",
        "era": "1950s–90s",
        "born": "1933, North Carolina",
        "instrument": "Piano, Vocals",
        "tagline": "The High Priestess of Soul",
        "bio": "Nina Simone was an American singer, pianist, and civil rights activist. Her music defied genre, blending jazz, blues, gospel, folk, and classical. Beyond music she was a fierce advocate for racial equality — her songs became anthems of the civil rights movement.",
        "known_for": ["Feeling Good", "Strange Fruit", "I Put a Spell on You"],
    },
    {
        "name": "Bob Marley",
        "emoji": "🌿",
        "genre": "Reggae",
        "era": "1970s",
        "born": "1945, Jamaica",
        "instrument": "Vocals, Guitar",
        "tagline": "King of Reggae",
        "bio": "Robert Nesta Marley was a Jamaican singer-songwriter who transformed reggae into a worldwide phenomenon. His music carried messages of love, unity, and spiritual freedom rooted in Rastafarian philosophy. He remains one of the best-selling artists of all time.",
        "known_for": ["No Woman No Cry", "One Love", "Redemption Song"],
    },
    {
        "name": "Ella Fitzgerald",
        "emoji": "🌸",
        "genre": "Jazz",
        "era": "1930s–90s",
        "born": "1917, Virginia",
        "instrument": "Vocals",
        "tagline": "The First Lady of Song",
        "bio": "Ella Fitzgerald was an American jazz vocalist known for her purity of tone, impeccable diction, and near-perfect intonation. Her three-octave vocal range and mastery of scat singing made her one of the most celebrated singers of all time. She won 13 Grammy Awards.",
        "known_for": ["Misty", "Summertime", "Scat singing mastery"],
    },
    {
        "name": "Ludwig van Beethoven",
        "emoji": "🎻",
        "genre": "Classical",
        "era": "1800s",
        "born": "1770, Bonn",
        "instrument": "Piano, Violin",
        "tagline": "The Titan of Classical Music",
        "bio": "Ludwig van Beethoven was a German composer who bridged the Classical and Romantic eras. Remarkably, he composed many of his greatest works — including the Ninth Symphony — after becoming almost completely deaf. His innovations in structure and harmonic language shaped all music that followed.",
        "known_for": ["Symphony No. 9", "Moonlight Sonata", "Fur Elise"],
    },
    {
        "name": "Prince",
        "emoji": "💜",
        "genre": "Pop/Funk",
        "era": "1980s–2010s",
        "born": "1958, Minneapolis",
        "instrument": "Vocals, Guitar, Piano",
        "tagline": "The Purple One",
        "bio": "Prince Rogers Nelson was an American musician who defied every category. A genuine multi-instrumentalist, he played every instrument on many recordings. His music fused rock, R&B, funk, pop, and soul with flamboyance and mystique that was entirely his own.",
        "known_for": ["Purple Rain", "Sign o the Times", "When Doves Cry"],
    },
    {
        "name": "Johnny Cash",
        "emoji": "🖤",
        "genre": "Country",
        "era": "1950s–2000s",
        "born": "1932, Arkansas",
        "instrument": "Vocals, Guitar",
        "tagline": "The Man in Black",
        "bio": "John R. Cash was an American country musician with one of the most distinctive voices in history — a deep, resonant bass-baritone carrying both pain and tenderness. He embodied the struggles of working-class people, earning respect across all genre lines.",
        "known_for": ["Ring of Fire", "Hurt (cover)", "Folsom Prison Blues"],
    },
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Soundboard — Musician Directory</title>
  <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Lato:wght@300;400;700&display=swap" rel="stylesheet"/>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    :root {
      --bg: #0e0e0e; --surface: #181818; --card: #1f1f1f;
      --border: #2c2c2c; --accent: #e8ff47; --text: #f2f2f2;
      --muted: #777; --radius: 12px;
    }
    html { scroll-behavior: smooth; }
    body { font-family: 'Lato', sans-serif; background: var(--bg); color: var(--text); min-height: 100vh; }

    header {
      background: var(--surface); border-bottom: 1px solid var(--border);
      padding: 1.2rem 2.5rem; display: flex; align-items: center;
      justify-content: space-between; position: sticky; top: 0; z-index: 50;
    }
    .logo { font-family: 'Bebas Neue', sans-serif; font-size: 1.9rem; letter-spacing: 3px; color: var(--accent); }
    .logo span { color: var(--text); }
    .header-tag { font-size: 0.7rem; letter-spacing: 3px; text-transform: uppercase; color: var(--muted); }

    .hero { padding: 5rem 2.5rem 3rem; max-width: 900px; margin: 0 auto; }
    .hero-eyebrow { font-size: 0.7rem; letter-spacing: 4px; text-transform: uppercase; color: var(--accent); margin-bottom: 0.8rem; }
    .hero h1 { font-family: 'Bebas Neue', sans-serif; font-size: clamp(3.5rem, 8vw, 7rem); line-height: 0.95; letter-spacing: 2px; margin-bottom: 1.2rem; }
    .hero h1 em { font-style: normal; color: var(--accent); }
    .hero-desc { color: var(--muted); font-size: 0.95rem; line-height: 1.7; max-width: 500px; font-weight: 300; }

    .controls { max-width: 900px; margin: 0 auto 1.5rem; padding: 0 2.5rem; display: flex; gap: 1rem; flex-wrap: wrap; }
    .search-wrap { flex: 1; min-width: 200px; position: relative; }
    .search-wrap input {
      width: 100%; padding: 0.72rem 1rem 0.72rem 2.6rem;
      background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius);
      color: var(--text); font-family: 'Lato', sans-serif; font-size: 0.88rem; outline: none; transition: border-color 0.2s;
    }
    .search-wrap input:focus { border-color: var(--accent); }
    .search-wrap input::placeholder { color: var(--muted); }
    .search-icon { position: absolute; left: 0.85rem; top: 50%; transform: translateY(-50%); color: var(--muted); pointer-events: none; }
    .filters { display: flex; gap: 0.5rem; flex-wrap: wrap; }
    .filter-btn {
      padding: 0.5rem 1rem; background: var(--surface); border: 1px solid var(--border);
      border-radius: 50px; color: var(--muted); font-size: 0.75rem; letter-spacing: 1px;
      text-transform: uppercase; cursor: pointer; transition: all 0.2s; font-family: 'Lato', sans-serif;
    }
    .filter-btn:hover { border-color: var(--accent); color: var(--accent); }
    .filter-btn.active { background: var(--accent); color: #0e0e0e; border-color: var(--accent); font-weight: 700; }

    .stats-bar { max-width: 900px; margin: 0 auto 1.2rem; padding: 0 2.5rem; font-size: 0.78rem; color: var(--muted); }
    .stats-bar strong { color: var(--accent); }

    .grid { max-width: 900px; margin: 0 auto; padding: 0 2.5rem 5rem; display: grid; grid-template-columns: repeat(auto-fill, minmax(255px, 1fr)); gap: 1.1rem; }

    .card {
      background: var(--card); border: 1px solid var(--border); border-radius: var(--radius);
      overflow: hidden; cursor: pointer; transition: transform 0.22s, border-color 0.22s, box-shadow 0.22s;
      animation: fadeUp 0.35s ease both;
    }
    @keyframes fadeUp { from { opacity: 0; transform: translateY(14px); } to { opacity: 1; transform: translateY(0); } }
    .card:hover { transform: translateY(-5px); border-color: var(--accent); box-shadow: 0 12px 36px rgba(232,255,71,0.07); }
    .card-top { padding: 1.4rem 1.4rem 0.9rem; display: flex; align-items: flex-start; gap: 1rem; }
    .avatar { width: 54px; height: 54px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; flex-shrink: 0; border: 2px solid var(--border); background: #1a1a1a; }
    .card-name { font-family: 'Bebas Neue', sans-serif; font-size: 1.3rem; letter-spacing: 1px; line-height: 1.1; margin-bottom: 0.35rem; }
    .card-genre { display: inline-block; font-size: 0.65rem; letter-spacing: 2px; text-transform: uppercase; color: #0e0e0e; background: var(--accent); padding: 0.18rem 0.55rem; border-radius: 4px; font-weight: 700; }
    .card-bio { padding: 0 1.4rem 0.9rem; font-size: 0.83rem; color: var(--muted); line-height: 1.65; font-weight: 300; }
    .card-footer { padding: 0.75rem 1.4rem; border-top: 1px solid var(--border); display: flex; justify-content: space-between; font-size: 0.72rem; color: var(--muted); }

    .modal-overlay {
      position: fixed; inset: 0; background: rgba(0,0,0,0.85);
      display: flex; align-items: center; justify-content: center;
      z-index: 200; padding: 1.5rem; opacity: 0; pointer-events: none; transition: opacity 0.25s;
    }
    .modal-overlay.open { opacity: 1; pointer-events: all; }
    .modal {
      background: var(--card); border: 1px solid var(--border); border-radius: 18px;
      max-width: 560px; width: 100%; max-height: 90vh; overflow-y: auto;
      transform: scale(0.94) translateY(18px); transition: transform 0.28s;
    }
    .modal-overlay.open .modal { transform: scale(1) translateY(0); }
    .modal-header { padding: 1.8rem 1.8rem 1rem; border-bottom: 1px solid var(--border); display: flex; align-items: flex-start; gap: 1.2rem; }
    .modal-avatar { width: 70px; height: 70px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 2.1rem; border: 2px solid var(--accent); flex-shrink: 0; background: #1a1a1a; }
    .modal-name { font-family: 'Bebas Neue', sans-serif; font-size: 2rem; letter-spacing: 2px; line-height: 1; margin-bottom: 0.3rem; }
    .modal-tagline { font-size: 0.8rem; color: var(--muted); margin-bottom: 0.5rem; }
    .modal-tags { display: flex; gap: 0.4rem; flex-wrap: wrap; }
    .tag { font-size: 0.65rem; letter-spacing: 1.5px; text-transform: uppercase; padding: 0.2rem 0.6rem; border-radius: 4px; font-weight: 700; }
    .tag-genre { background: var(--accent); color: #0e0e0e; }
    .tag-era { background: var(--surface); color: var(--muted); border: 1px solid var(--border); }
    .modal-body { padding: 1.5rem 1.8rem; }
    .modal-label { font-size: 0.65rem; letter-spacing: 3px; text-transform: uppercase; color: var(--accent); margin-bottom: 0.55rem; }
    .modal-bio { color: #bbb; font-size: 0.9rem; line-height: 1.82; margin-bottom: 1.5rem; font-weight: 300; }
    .facts-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem; margin-bottom: 1.5rem; }
    .fact { background: var(--surface); border: 1px solid var(--border); border-radius: 10px; padding: 0.85rem 1rem; }
    .fact-label { font-size: 0.62rem; letter-spacing: 2px; text-transform: uppercase; color: var(--muted); margin-bottom: 0.25rem; }
    .fact-val { font-size: 0.88rem; font-weight: 700; }
    .chips { display: flex; flex-wrap: wrap; gap: 0.45rem; margin-top: 0.55rem; margin-bottom: 1.5rem; }
    .chip { background: var(--surface); border: 1px solid var(--border); border-radius: 50px; padding: 0.28rem 0.8rem; font-size: 0.76rem; color: var(--muted); }
    .modal-close-row { display: flex; justify-content: flex-end; padding: 0 1.8rem 1.5rem; }
    .close-btn { background: var(--surface); border: 1px solid var(--border); color: var(--muted); padding: 0.55rem 1.3rem; border-radius: 50px; cursor: pointer; font-family: 'Lato', sans-serif; font-size: 0.8rem; letter-spacing: 1px; transition: all 0.2s; }
    .close-btn:hover { border-color: var(--accent); color: var(--accent); }

    .empty { grid-column: 1/-1; text-align: center; padding: 4rem 2rem; color: var(--muted); }
    .empty-icon { font-size: 3rem; margin-bottom: 1rem; display: block; }
    .empty h3 { font-family: 'Bebas Neue', sans-serif; font-size: 1.8rem; letter-spacing: 2px; margin-bottom: 0.5rem; color: var(--text); }

    footer { border-top: 1px solid var(--border); text-align: center; padding: 2rem; font-size: 0.76rem; color: var(--muted); }
    footer strong { color: var(--accent); }
    ::-webkit-scrollbar { width: 5px; }
    ::-webkit-scrollbar-track { background: var(--bg); }
    ::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }
  </style>
</head>
<body>

<header>
  <div class="logo">Sound<span>board</span></div>
  <div class="header-tag">Musician Directory</div>
</header>

<div class="hero">
  <p class="hero-eyebrow">Explore · Discover · Learn</p>
  <h1>The World's<br/><em>Greatest</em><br/>Musicians</h1>
  <p class="hero-desc">A curated directory of iconic musicians across genres and eras — their stories, their sound, their legacy.</p>
</div>

<div class="controls">
  <div class="search-wrap">
    <span class="search-icon">🔍</span>
    <input type="text" id="searchInput" placeholder="Search musicians, genres…"/>
  </div>
  <div class="filters" id="filters"></div>
</div>

<div class="stats-bar">
  <strong id="countDisplay">{{ musicians|length }}</strong> musicians found
</div>

<div class="grid" id="grid"></div>

<div class="modal-overlay" id="modalOverlay">
  <div class="modal" id="modal">
    <div class="modal-header">
      <div class="modal-avatar" id="mAvatar"></div>
      <div>
        <div class="modal-name" id="mName"></div>
        <div class="modal-tagline" id="mTagline"></div>
        <div class="modal-tags" id="mTags"></div>
      </div>
    </div>
    <div class="modal-body">
      <div class="modal-label">Biography</div>
      <p class="modal-bio" id="mBio"></p>
      <div class="modal-label">Quick Facts</div>
      <div class="facts-grid" id="mFacts"></div>
      <div class="modal-label">Known For</div>
      <div class="chips" id="mChips"></div>
    </div>
    <div class="modal-close-row">
      <button class="close-btn" id="closeBtn">✕ Close</button>
    </div>
  </div>
</div>

<footer>Built with <strong>Python Flask</strong> · Musician Directory App · CI/CD Ready</footer>

<script>
const musicians = {{ musicians | tojson }};
const genres = ['All', ...new Set(musicians.map(m => m.genre))];
let activeGenre = 'All';
let searchVal = '';

function renderFilters() {
  document.getElementById('filters').innerHTML = genres.map(g =>
    `<button class="filter-btn ${g === activeGenre ? 'active' : ''}" onclick="setGenre('${g}')">${g}</button>`
  ).join('');
}
function setGenre(g) { activeGenre = g; renderFilters(); renderGrid(); }

function renderGrid() {
  const q = searchVal.toLowerCase();
  const filtered = musicians.filter(m => {
    const matchGenre = activeGenre === 'All' || m.genre === activeGenre;
    const matchSearch = !q || m.name.toLowerCase().includes(q) || m.genre.toLowerCase().includes(q) || m.tagline.toLowerCase().includes(q) || m.bio.toLowerCase().includes(q);
    return matchGenre && matchSearch;
  });
  document.getElementById('countDisplay').textContent = filtered.length;
  const grid = document.getElementById('grid');
  if (!filtered.length) {
    grid.innerHTML = `<div class="empty"><span class="empty-icon">🎵</span><h3>No Musicians Found</h3><p>Try a different search or filter.</p></div>`;
    return;
  }
  grid.innerHTML = filtered.map((m, i) => `
    <div class="card" style="animation-delay:${i*0.045}s" onclick="openModal(${musicians.indexOf(m)})">
      <div class="card-top">
        <div class="avatar">${m.emoji}</div>
        <div>
          <div class="card-name">${m.name}</div>
          <span class="card-genre">${m.genre}</span>
        </div>
      </div>
      <div class="card-bio">${m.bio.substring(0,115).trim()}…</div>
      <div class="card-footer">
        <span>🎵 ${m.instrument.split(',')[0].trim()}</span>
        <span>📅 ${m.era}</span>
      </div>
    </div>
  `).join('');
}

function openModal(idx) {
  const m = musicians[idx];
  document.getElementById('mAvatar').textContent = m.emoji;
  document.getElementById('mName').textContent = m.name;
  document.getElementById('mTagline').textContent = m.tagline;
  document.getElementById('mBio').textContent = m.bio;
  document.getElementById('mTags').innerHTML = `<span class="tag tag-genre">${m.genre}</span><span class="tag tag-era">${m.era}</span>`;
  document.getElementById('mFacts').innerHTML = [
    { label:'Born', val: m.born },
    { label:'Era', val: m.era },
    { label:'Instrument', val: m.instrument },
    { label:'Genre', val: m.genre },
  ].map(f => `<div class="fact"><div class="fact-label">${f.label}</div><div class="fact-val">${f.val}</div></div>`).join('');
  document.getElementById('mChips').innerHTML = m.known_for.map(k => `<span class="chip">${k}</span>`).join('');
  document.getElementById('modalOverlay').classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeModal() {
  document.getElementById('modalOverlay').classList.remove('open');
  document.body.style.overflow = '';
}

document.getElementById('modalOverlay').addEventListener('click', function(e) { if (e.target === this) closeModal(); });
document.getElementById('closeBtn').addEventListener('click', closeModal);
document.addEventListener('keydown', e => { if (e.key === 'Escape') closeModal(); });
document.getElementById('searchInput').addEventListener('input', function() { searchVal = this.value; renderGrid(); });

renderFilters();
renderGrid();
</script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE, musicians=MUSICIANS)

@app.route("/health")
def health():
    return {"status": "ok", "app": "Musician Directory", "version": "1.0.0"}

@app.route("/api/musicians")
def api_musicians():
    return {"musicians": MUSICIANS, "total": len(MUSICIANS)}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
