import sqlite3
import os

DB_PATH = os.path.join("data", "school.db")


def seed_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # ----------------------------
    # Clear Existing Data
    # ----------------------------
    cursor.execute("DELETE FROM classes")
    cursor.execute("DELETE FROM fees")
    cursor.execute("DELETE FROM transport")
    cursor.execute("DELETE FROM school_info")
    cursor.execute("DELETE FROM faqs")

    # ----------------------------
    # Classes
    # ----------------------------
    classes = [
        ("Nursery", 40, 12),
        ("KG", 40, 15),
        ("Grade 1", 40, 10),
        ("Grade 2", 40, 8),
        ("Grade 3", 40, 6),
        ("Grade 4", 40, 5),
        ("Grade 5", 40, 4)
    ]

    cursor.executemany("""
    INSERT INTO classes(class_name,total_seats,available_seats)
    VALUES(?,?,?)
    """, classes)

    # ----------------------------
    # Fees
    # ----------------------------
    fees = [
        ("Nursery",15000,35000,5000,12000),
        ("KG",15000,35000,5000,12000),
        ("Grade 1",20000,40000,6000,15000),
        ("Grade 2",20000,42000,6000,15000),
        ("Grade 3",20000,45000,6000,15000),
        ("Grade 4",20000,47000,7000,16000),
        ("Grade 5",25000,50000,7000,17000)
    ]

    cursor.executemany("""
    INSERT INTO fees(class_name,admission_fee,tuition_fee,annual_fee,transport_fee)
    VALUES(?,?,?,?,?)
    """, fees)

    # ----------------------------
    # Transport
    # ----------------------------
    transport = [
        ("Nikol","Yes"),
        ("Naroda","Yes"),
        ("Chandkheda","Yes"),
        ("Satellite","Yes"),
        ("Bopal","No"),
        ("Maninagar","Yes"),
        ("Ranip","Yes"),
        ("Gota","Yes"),
        ("Vastral","Yes"),
        ("Thaltej","No")
    ]

    cursor.executemany("""
    INSERT INTO transport(area_name,available)
    VALUES(?,?)
    """, transport)

    # ----------------------------
    # School Info
    # ----------------------------
    school_info = [
        ("School Timing",
         "School timing is Monday to Friday from 8:00 AM to 2:00 PM."),

        ("Admission Process",
         "Parents need to submit the admission form, required documents and pay the admission fee after selection."),

        ("Campus Visit",
         "Campus visits are available Monday to Saturday between 10:00 AM and 1:00 PM.")
    ]

    cursor.executemany("""
    INSERT INTO school_info(title,description)
    VALUES(?,?)
    """, school_info)

    # ----------------------------
    # FAQs
    # ----------------------------
    faqs = [

        ("What documents are required?",
         "Birth Certificate, Aadhaar Card, Passport Size Photos, Previous Report Card and Address Proof."),

        ("Is transport available?",
         "Transport is available only in selected areas."),

        ("How can I schedule a campus visit?",
         "You can call the admission office or fill the enquiry form."),

        ("What are the school timings?",
         "School starts at 8:00 AM and ends at 2:00 PM."),

        ("Do you provide books and uniforms?",
         "Yes. Books and uniforms are available through the school store.")
    ]

    cursor.executemany("""
    INSERT INTO faqs(question,answer)
    VALUES(?,?)
    """, faqs)

    conn.commit()
    conn.close()

    print("✅ Sample Data Inserted Successfully!")


if __name__ == "__main__":
    seed_database()