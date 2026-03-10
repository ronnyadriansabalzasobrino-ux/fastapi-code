import psycopg2

def get_db_connection():
    return psycopg2.connect(
        host="ep-raspy-resonance-aiqjiigd-pooler.c-4.us-east-1.aws.neon.tech",
        port="5432",
        user="neondb_owner",
        password="npg_b0wOEr3kIQvi",
        dbname="neondb"
    )