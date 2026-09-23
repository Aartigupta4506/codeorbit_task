"""
CodeOrbit Tech - AI Internship
Task 1: Rule-Based Chatbot

Professional Streamlit Interface
"""

import streamlit as st
from chatbot_engine import RuleBasedChatbot


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="CodeOrbit AI Assistant",
    page_icon="🤖",
    layout="centered"
)


# ==========================================================
# INITIALIZE CHATBOT
# ==========================================================

chatbot = RuleBasedChatbot()


# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown(
    """
    <style>

    /* Main page */
    .main {
        padding-top: 1rem;
    }

    /* Header */
    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 20px;
        margin-bottom: 5px;
    }

    .description {
        text-align: center;
        font-size: 14px;
        color: #777;
        margin-bottom: 20px;
    }

    /* Information card */
    .project-card {
        padding: 18px;
        border-radius: 12px;
        border: 1px solid #ddd;
        margin-bottom: 20px;
    }

    /* Quick button area */
    .quick-title {
        font-size: 18px;
        font-weight: 600;
        margin-bottom: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==========================================================
# HEADER
# ==========================================================

st.markdown(
    '<div class="main-title">🤖 CodeOrbit AI Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Rule-Based Chatbot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="description">'
    'CodeOrbit Tech | Artificial Intelligence Internship | Task 1'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# ==========================================================
# PROJECT INTRODUCTION
# ==========================================================

st.info(
    "👋 Welcome to CodeOrbit AI Assistant! "
    "I am a rule-based chatbot that uses predefined "
    "keywords, conditions and responses to answer questions."
)


# ==========================================================
# SESSION STATE
# ==========================================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.header("⚙️ Chat Controls")

    st.write(
        "Use the controls below to manage your chatbot session."
    )

    # Message count
    message_count = len(st.session_state.messages)

    user_messages = sum(
        1
        for message in st.session_state.messages
        if message["role"] == "user"
    )

    bot_messages = sum(
        1
        for message in st.session_state.messages
        if message["role"] == "assistant"
    )

    st.metric(
        "Total Messages",
        message_count
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric("You", user_messages)

    with col2:
        st.metric("Bot", bot_messages)

    st.divider()

    # Clear chat
    if st.button(
        "🗑️ Clear Chat",
        use_container_width=True
    ):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.subheader("📚 Project Information")

    st.write("**Project:** Rule-Based Chatbot")
    st.write("**Task:** Task 1")
    st.write("**Organization:** CodeOrbit Tech")
    st.write("**Technology:** Python + Streamlit")

    st.divider()

    st.caption(
        "Built for CodeOrbit Tech AI Internship"
    )


# ==========================================================
# QUICK QUESTIONS
# ==========================================================

st.markdown(
    '<div class="quick-title">⚡ Quick Questions</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)


with col1:

    if st.button(
        "🤖 What is AI?",
        use_container_width=True
    ):
        user_input = "What is AI?"

        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })

        response = chatbot.get_response(user_input)

        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })

        st.rerun()


with col2:

    if st.button(
        "🧠 What is ML?",
        use_container_width=True
    ):
        user_input = "What is Machine Learning?"

        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })

        response = chatbot.get_response(user_input)

        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })

        st.rerun()


with col3:

    if st.button(
        "🐍 What is Python?",
        use_container_width=True
    ):
        user_input = "What is Python?"

        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })

        response = chatbot.get_response(user_input)

        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })

        st.rerun()


# ==========================================================
# CHAT HISTORY
# ==========================================================

st.divider()

st.subheader("💬 Conversation")


if not st.session_state.messages:

    st.markdown(
        """
        <div style="text-align:center; padding:25px;">
            <h3>👋 Start a Conversation</h3>
            <p>
                Ask me something about AI, Machine Learning,
                Python, programming or the CodeOrbit internship.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


# Display chat messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])


# ==========================================================
# USER INPUT
# ==========================================================

user_input = st.chat_input(
    "💬 Type your message here..."
)


if user_input:

    # Store user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Generate chatbot response
    response = chatbot.get_response(user_input)

    # Store chatbot response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    # Refresh application
    st.rerun()


# ==========================================================
# EXAMPLE QUESTIONS
# ==========================================================

st.divider()

with st.expander("💡 Example Questions"):

    st.write(
        "Here are some questions you can ask the chatbot:"
    )

    st.markdown(
        """
        ### 🤖 Chatbot
        - What is your name?
        - Who created you?
        - Are you human?
        - How do you work?
        - What is a rule-based chatbot?

        ### 🧠 Artificial Intelligence
        - What is AI?
        - What are applications of AI?
        - What is Machine Learning?
        - What is Deep Learning?
        - What is NLP?
        - What is Computer Vision?
        - What is Generative AI?
        - What is a Neural Network?

        ### 💻 Programming
        - What is Python?
        - What is C++?
        - What is Java?
        - What is HTML?
        - What is CSS?
        - What is JavaScript?
        - What is SQL?
        - What is Git?
        - What is GitHub?
        - What is API?

        ### 🎓 Career & Study
        - What skills are needed for AI?
        - What is a career in AI?
        - Give me interview tips.
        - Give me study tips.
        - Motivate me.

        ### 🎓 Internship
        - Tell me about the internship.
        - What is Task 1?
        - Tell me about the project.
        - What technologies are used?
        """
    )


# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.caption(
    "🤖 CodeOrbit AI Assistant | "
    "Rule-Based Chatbot | Task 1"
)