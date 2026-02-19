from flask import Flask, render_template_string
import os

app = Flask(__name__)

MUSICIANS = [
    {
        "name": "Freddie Mercury",
        "emoji": "🎤",
        "genre": "Rock",
        "era": "1970s–90s",
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
        "bio": "Aretha Louise Franklin was an American singer and pianist. The undisputed Queen of Soul, she was the first woman inducted into the Rock and Roll Hall of Fame and won 18 Grammy Awards.",
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
        "bio": "James Marshall Hendrix was an American guitarist who fundamentally changed what was possible on an electric guitar.",
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
        "bio": "Johann Sebastian Bach was a German composer of the late Baroque period.",
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
        "bio": "David Bowie was an English singer-songwriter celebrated for his constant reinvention.",
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
        "bio": "Nina Simone was an American singer, pianist, and civil rights activist.",
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
        "bio": "Robert Nesta Marley transformed reggae into a worldwide phenomenon.",
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
        "bio": "Ella Fitzgerald was known for her purity of tone and scat singing mastery.",
        "known_for": ["Misty", "Summertime"],
    },
    {
        "name": "Ludwig van Beethoven",
        "emoji": "🎻",
        "genre": "Classical",
        "era": "1800s",
        "born": "1770, Bonn",
        "instrument": "Piano, Violin",
        "tagline": "The Titan of Classical Music",
        "bio": "Beethoven composed many masterpieces after losing his hearing.",
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
        "bio": "Prince was a musical genius who blended multiple genres.",
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
        "bio": "Johnny Cash gave voice to the struggles of working-class people.",
        "known_for": ["Ring of Fire", "Hurt (cover)", "Folsom Prison Blues"],
    },
]

HTML_TEMPLATE = """<!DOCTYPE html>
<html>
<head><title>Musician Directory</title></head>
<body style="background:#111;color:#eee;font-family:Arial">
<h1>🎵 Musician Directory</h1>
<ul>
{% for m in musicians %}
<li><b>{{ m.name }}</b> — {{ m.genre }} ({{ m.era }})</li>
{% endfor %}
</ul>
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
    port = int(os.environ.get("PORT", 4022))
    app.run(host="0.0.0.0", port=port, debug=False)
