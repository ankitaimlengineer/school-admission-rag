import sqlite3
import os

# Database path
DB_PATH = os.path.join("data", "school.db")


def create_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # ----------------------------
    # Classes Table
    # ----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS classes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        class_name TEXT NOT NULL,
        total_seats INTEGER NOT NULL,
        available_seats INTEGER NOT NULL
    )
    """)

    # ----------------------------
    # Fees Table
    # ----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS fees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        class_name TEXT NOT NULL,
        admission_fee INTEGER,
        tuition_fee INTEGER,
        annual_fee INTEGER,
        transport_fee INTEGER
    )
    """)

    # ----------------------------
    # Transport Table
    # ----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transport (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        area_name TEXT NOT NULL,
        available TEXT NOT NULL
    )
    """)

    # ----------------------------
    # School Info Table
    # ----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS school_info (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT
    )
    """)

    # ----------------------------
    # FAQs Table
    # ----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS faqs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT,
        answer TEXT
    )
    """)

    conn.commit()
    conn.close()

    print("✅ Database Created Successfully!")


if __name__ == "__main__":
    create_database()