import sqlite3
import os

DB_PATH = os.path.join("data", "school.db")


def get_fee_details(class_name):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT admission_fee, tuition_fee, annual_fee, transport_fee
        FROM fees
        WHERE class_name = ?
    """, (class_name,))

    result = cursor.fetchone()
    conn.close()

    return result


def get_seat_availability(class_name):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT available_seats
        FROM classes
        WHERE class_name = ?
    """, (class_name,))

    result = cursor.fetchone()
    conn.close()

    return result


def get_transport_status(area):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT available
        FROM transport
        WHERE area_name = ?
    """, (area,))

    result = cursor.fetchone()
    conn.close()

    return result