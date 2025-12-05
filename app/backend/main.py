import os
from flask import Flask
import mysql.connector

class DBManager:
    def __init__(self, database='example', host="db", user="root", password_file=None):
        pf = open(password_file, 'r')
        self.connection = mysql.connector.connect(
            user=user, 
            password=pf.read(),
            host=host,
            database=database,
        )
        pf.close()
        self.cursor = self.connection.cursor()

    def populate_db(self):
        self.cursor.execute('DROP TABLE IF EXISTS songs')
        self.cursor.execute('''
            CREATE TABLE songs (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255),
                description TEXT,
                listen_count INT
            )
        ''')

        top_songs = [
            {
                "title": "Die With a Smile - Lady Gaga & Bruno Mars",
                "description": "A global hit known for its emotional vocals and retro music video.",
                "count": 520_000_000
            },
            {
                "title": "Apt. - ROSÉ & Bruno Mars",
                "description": "A soft, melodic duet blending pop and R&B influences.",
                "count": 310_000_000
            },
            {
                "title": "Luther - Kendrick Lamar & SZA",
                "description": "A powerful collaboration with deep lyrics and atmospheric production.",
                "count": 420_000_000
            },
            {
                "title": "DTMF - Bad Bunny",
                "description": "A reggaeton/Latin trap fusion currently dominating global charts.",
                "count": 380_000_000
            },
            {
                "title": "Beautiful Things - Benson Boone",
                "description": "Viral hit praised for its emotional delivery and strong chorus.",
                "count": 600_000_000
            },
            {
                "title": "Espresso - Sabrina Carpenter",
                "description": "A viral pop anthem known for its catchy hook and massive TikTok presence.",
                "count": 780_000_000
            },
            {
                "title": "Fortnight - Taylor Swift ft. Post Malone",
                "description": "A moody, atmospheric pop track blending Swift's storytelling with Post Malone's soft vocals.",
                "count": 650_000_000
            },
            {
                "title": "Lose Control - Teddy Swims",
                "description": "A soulful powerhouse performance that became a global breakout hit.",
                "count": 890_000_000
            }
        ]

        self.cursor.executemany(
            'INSERT INTO songs (title, description, listen_count) VALUES (%s, %s, %s);',
            [(s["title"], s["description"], s["count"]) for s in top_songs]
        )
        self.connection.commit()

    def query_titles(self):
        self.cursor.execute('SELECT title, description, listen_count FROM songs')
        return [
            {
                "title": row[0],
                "description": row[1],
                "count": row[2]
            }
            for row in self.cursor
        ]


server = Flask(__name__)
conn = None

@server.route('/')
def listBlog():
    global conn
    if not conn:
        conn = DBManager(password_file='/run/secrets/db-password')
        conn.populate_db()
    rec = conn.query_titles()

    list_items = ""
    for song in rec:
        list_items += f"""
            <div class="card">
                <h2>{song['title']}</h2>
                <p>{song['description']}</p>
                <p><strong>Listens:</strong> {song['count']:,}</p>
            </div>
        """


    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Devops - Songs</title>

        <!-- Google Font -->
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">

        <style>
            body {{
                margin: 0;
                padding: 0;
                font-family: 'Poppins', sans-serif;
                background: #0f0f17;
                color: #f0f0f0;
                display: flex;
                justify-content: center;
                min-height: 100vh;
                overflow-x: hidden;
            }}

            /* RIGHT SIDE BANNER */
            .right-banner {{
                position: fixed;
                top: 0;
                right: 0;
                width: 320px;
                height: 100vh;
                background-image: url('https://cdn.bannerbuzz.co.uk/media/catalog/product/n/5/n5_bbxskx01_1_uk.jpg');
                background-size: cover;
                background-position: center;
                filter: brightness(0.75);
            }}

            .container {{
                width: 100%;
                max-width: 900px;
                padding: 40px 20px;
                padding-right: 320px; /* space for banner */
            }}

            header {{
                margin-bottom: 40px;
            }}

            h1 {{
                margin: 0;
                font-size: 2.6rem;
                font-weight: 600;
                color: #58a6ff;
            }}

            .subtitle {{
                color: #b5b5b5;
                margin-top: 10px;
                font-size: 1rem;
            }}

            /* GRID POSTS */
            .posts {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
                gap: 20px;
            }}

            /* CARD */
            .card {{
                background: #1c1c29;
                border-radius: 16px;
                padding: 22px;
                border: 1px solid #2b2b3c;
                transition: 0.25s ease;
                box-shadow: 0 4px 18px rgba(0, 0, 0, 0.25);
            }}

            .card:hover {{
                transform: translateY(-5px);
                box-shadow: 0 6px 25px rgba(0,0,0,0.40);
                border-color: #58a6ff;
            }}

            .card h2 {{
                margin: 0;
                color: #58a6ff;
                font-size: 1.4rem;
            }}

            .card p {{
                color: #cccccc;
                line-height: 1.5;
                margin-top: 10px;
                font-size: 0.95rem;
            }}

            footer {{
                margin-top: 50px;
                text-align: center;
                color: #777;
                font-size: 0.85rem;
            }}

            /* RESPONSIVE – hide banner on phones */
            @media (max-width: 900px) {{
                .right-banner {{ display: none; }}
                .container {{ padding-right: 20px; }}
            }}
        </style>
    </head>

    <body>
        <div class="right-banner"></div>

        <div class="container">
            <header>
                <h1>Top Songs This Year</h1>
                <div class="subtitle">Most streamed songs of 2025. Exclusive for Devops course!</div>
            </header>

            <div class="posts">
                {list_items}
            </div>

            <footer>
                <p>Custom UI by Natig. 2025. Ansible devops.</p>
            </footer>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    server.run()
