import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from rag.retriever import get_retriever
from rag.prompts import PROMPT_TEMPLATE

from database.db_queries import (
    get_fee_details,
    get_seat_availability,
    get_transport_status
)

load_dotenv()

# =====================================
# Gemini Model
# =====================================

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0
)

retriever = get_retriever()


def ask_question(question, chat_history=None):

    if chat_history is None:
        chat_history = []

    question_lower = question.lower()

    # =====================================
    # Conversation Memory
    # =====================================

    last_user_message = ""

    for msg in reversed(chat_history):
        if msg["role"] == "user" and msg["content"] != question:
            last_user_message = msg["content"].lower()
            break

    # Follow-up Question Support
    if "what about" in question_lower:

        if "fee" in last_user_message:
            question_lower += " fee"

        if "seat" in last_user_message:
            question_lower += " seat"

        if "transport" in last_user_message:
            question_lower += " transport"

        if "timing" in last_user_message:
            question_lower += " timing"

        if "document" in last_user_message:
            question_lower += " document"

    # =====================================
    # Chat History for Gemini
    # =====================================

    history_text = ""

    for msg in chat_history[-6:]:
        history_text += f"{msg['role']}: {msg['content']}\n"

    grades = [
        "Nursery",
        "KG",
        "Grade 1",
        "Grade 2",
        "Grade 3",
        "Grade 4",
        "Grade 5"
    ]

    # =====================================
    # Fees Queries
    # =====================================

    for grade in grades:

        if grade.lower() in question_lower and "fee" in question_lower:

            fees = get_fee_details(grade)

            if fees:
                answer = f"""
### 💰 Fees for {grade}

- Admission Fee: ₹{fees[0]}
- Tuition Fee: ₹{fees[1]}
- Annual Fee: ₹{fees[2]}
- Transport Fee: ₹{fees[3]}

📌 Source: School Database
"""
                return answer.strip(), ["School Database"]

    # =====================================
    # Seat Queries
    # =====================================

    for grade in grades:

        if grade.lower() in question_lower and (
            "seat" in question_lower or
            "available" in question_lower
        ):

            seats = get_seat_availability(grade)

            if seats:
                answer = f"""
### 🪑 Seat Availability

Available seats in **{grade}**: **{seats[0]}**

📌 Source: School Database
"""
                return answer.strip(), ["School Database"]

    # =====================================
    # Transport Queries
    # =====================================

    areas = [
        "Nikol",
        "Naroda",
        "Chandkheda",
        "Satellite",
        "Bopal",
        "Maninagar",
        "Ranip",
        "Gota",
        "Vastral",
        "Thaltej"
    ]

    for area in areas:

        if area.lower() in question_lower:

            transport = get_transport_status(area)

            if transport:
                answer = f"""
### 🚌 Transport Information

Transport availability in **{area}**: **{transport[0]}**

📌 Source: School Database
"""
                return answer.strip(), ["School Database"]

    # =====================================
    # RAG Retrieval
    # =====================================

    docs = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = PROMPT_TEMPLATE.format(
        history=history_text,
        context=context,
        question=question
    )

    response = llm.invoke(prompt)

    return response.content, docs