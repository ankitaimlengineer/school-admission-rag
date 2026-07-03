import streamlit as st
from chatbot import ask_question

# =====================================
# Page Configuration
# =====================================

st.set_page_config(
    page_title="School Admission Assistant",
    page_icon="🎓",
    layout="wide"
)

# =====================================
# Custom CSS
# =====================================

st.markdown("""
<style>

.main-title{
    text-align:center;
    font-size:42px;
    font-weight:bold;
    color:#4F46E5;
}

.subtitle{
    text-align:center;
    color:gray;
    margin-bottom:25px;
}

.stChatMessage{
    border-radius:15px;
    padding:10px;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# Header
# =====================================

st.markdown(
    '<p class="main-title">🎓 School Admission Enquiry Assistant</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Ask anything about admissions, fees, transport, timings, seat availability and more.</p>',
    unsafe_allow_html=True
)

# =====================================
# Sidebar
# =====================================

with st.sidebar:

    st.title("📌 Sample Questions")

    st.markdown("""
- What is the admission process?
- What documents are required for admission?
- What are the fees for Grade 1?
- Are seats available for Grade 5?
- Is transport available in Nikol?
- What are the school timings?
- Can I schedule a campus visit?
""")

    st.divider()

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# =====================================
# Session State
# =====================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# =====================================
# Display Chat History
# =====================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# =====================================
# Chat Input
# =====================================

question = st.chat_input(
    "Ask your admission related question..."
)

if question:

    # -------------------------
    # User Message
    # -------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # -------------------------
    # Assistant Response
    # -------------------------

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            answer, docs = ask_question(
    question,
    st.session_state.messages
)

            st.markdown(answer)

            # -------------------------
            # Sources
            # -------------------------

            if docs:

                st.markdown("---")
                st.markdown("### 📚 Sources Used")

                shown_sources = set()

                for doc in docs:

                    # Database Source
                    if isinstance(doc, str):

                        if doc not in shown_sources:
                            st.markdown(f"🗄️ {doc}")
                            shown_sources.add(doc)

                    # RAG Source
                    else:

                        source = doc.metadata.get("source")

                        if source:

                            filename = source.split("\\")[-1]

                            if filename not in shown_sources:
                                st.markdown(f"📄 {filename}")
                                shown_sources.add(filename)

    # -------------------------
    # Save Assistant Message
    # -------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )