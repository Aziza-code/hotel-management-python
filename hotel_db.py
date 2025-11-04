import sqlite3
connection = sqlite3.connect('hotel.db')
connection.executescript("""
CREATE TABLE IF NOT EXISTS clients (
    CNE INTEGER PRIMARY KEY ,
    name TEXT NOT NULL,
    phone TEXT,
    email TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
 
    CREATE TABLE IF NOT EXISTS rooms (
    room_id INTEGER PRIMARY KEY AUTOINCREMENT,
    room_number TEXT UNIQUE NOT NULL,
    type TEXT NOT NULL,
    price REAL NOT NULL,
    available INTEGER DEFAULT 1
);

CREATE TABLE IF NOT EXISTS reservations (
    booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    CNE INTEGER NOT NULL,
    room_number INTEGER NOT NULL,
    date_entree TEXT NOT NULL,
    date_sortie TEXT NOT NULL,
    FOREIGN KEY(CNE) REFERENCES clients(CNE),
    FOREIGN KEY(room_number) REFERENCES rooms(rooms_number)
);
""")
"""rooms = [
    ("101", "Simple", 200.0, 1),
    ("102", "Simple", 220.0, 1),
    ("103", "Double", 250.0, 1),
    ("104", "Double", 270.0, 1),
    ("105", "Suite", 300.0, 1),
    ("106", "Simple", 320.0, 1),
    ("107", "Double", 350.0, 1),
    ("108", "Suite", 370.0, 1),
    ("109", "Simple", 400.0, 1),
    ("110", "Suite", 420.0, 1),
]

for room in rooms:
    try:
        connection.execute(
            "INSERT INTO rooms (room_number, type, price, available) VALUES (?, ?, ?, ?)",
            room
        )
    except sqlite3.IntegrityError:
        print(f" Chambre {room[0]} existe déjà.")"""

connection.commit()
connection.close()


def connect():
    return sqlite3.connect("hotel.db")

def add_client(CNE,nom, telephone, email):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO clients (CNE,name, phone, email) VALUES ( ?, ?, ?, ?)",
            (CNE,nom, telephone, email)
        )
    except sqlite3.IntegrityError:
        conn.rollback()
        raise ValueError("Un client avec ce CIN existe déjà.")
    finally:
        conn.close()
    conn.commit()
    conn.close()
def get_clients():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clients ") # du client le plus récent jusqu'au le plus ancien
    rows = cursor.fetchall()  # pour récupérer toutes les lignes disponibles
    conn.close()
    return rows
#pour récupérer toutes les lignes disponibles
def get_free_rooms():
    conn = sqlite3.connect("hotel.db")
    cursor = conn.cursor()
    cursor.execute("SELECT room_number, price FROM rooms WHERE available = 1")
    data = cursor.fetchall()
    conn.close()
    return data
def update_room_status(room_number):
    conn = sqlite3.connect("hotel.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE rooms SET available = 1 WHERE room_number = ?", ( room_number))
    conn.commit()
    conn.close()
def add_booking(room_number,cne,date_entree,date_sortie):
    conn = sqlite3.connect("hotel.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO reservations (room_number,cne,date_entree,date_sortie) VALUES ( ?, ?, ?, ?)",
        (room_number,cne,date_entree,date_sortie))
    conn.commit()

