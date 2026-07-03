from database.db_queries import *

print("Grade 1 Fees:")
print(get_fee_details("Grade 1"))

print("\nGrade 5 Seats:")
print(get_seat_availability("Grade 5"))

print("\nTransport in Nikol:")
print(get_transport_status("Nikol"))