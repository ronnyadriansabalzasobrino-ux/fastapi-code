import psycopg2

def get_db_connection():
    try:
        conn = psycopg2.connect()
    except Exception as e:
        print("Error al conectar a la base de datos:", e)
        return None
    return psycopg2.connect(
        host="ep-raspy-resonance-aiqjiigd-pooler.c-4.us-east-1.aws.neon.tech",
        port="5432",
        user="neondb_owner",
        password="npg_b0wOEr3kIQvi",
        dbname="neondb"
        
    )
    



def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50),
        password VARCHAR(100),
        role VARCHAR(20),

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        state INTEGER DEFAULT 1
    );
    """)

    conn.commit()
    cursor.close()
    conn.close()