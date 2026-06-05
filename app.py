import os
import streamlit as st
import google.generativeai as genai
from datetime import datetime
from dotenv import load_dotenv

# --------------------------------------------------
# Load Environment Variables
# --------------------------------------------------
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

MODEL_NAME = "gemini-2.5-flash"
TEMPERATURE = 0.7
MAX_TOKENS = 1024

SYSTEM_PROMPT = """
You are GemBot Pro, a professional AI assistant.
Always provide accurate, helpful, and concise answers.
"""

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="GemBot Pro",
    page_icon="🤖",
    layout="centered"
)

# --------------------------------------------------
# Custom CSS
# --------------------------------------------------
st.markdown("""
<style>

.stApp {
    background: #0f1117;
    color: white;
}

/* Hide Sidebar */
[data-testid="stSidebar"] {
    display: none;
}

[data-testid="collapsedControl"] {
    display: none;
}

/* Title */
.main-title {
    text-align:center;
    font-size:3rem;
    font-weight:700;
    color:white;
    margin-bottom:0px;
}

.subtitle {
    text-align:center;
    color:#8b93b0;
    margin-bottom:20px;
}

/* Chat Bubble */
.user-bubble {
    background: linear-gradient(135deg,#4f8ef7,#6c63ff);
    color:white;
    padding:12px 16px;
    border-radius:18px 18px 4px 18px;
    margin:10px 0;
}

.bot-bubble {
    background:#1d2130;
    color:#e6e9f2;
    padding:12px 16px;
    border-radius:18px 18px 18px 4px;
    border:1px solid #2e3147;
    margin:10px 0;
}

.timestamp {
    font-size:11px;
    color:#8b93b0;
}

/* Input */
.stTextInput input {
    background:#1d2130 !important;
    color:white !important;
    border-radius:12px !important;
    border:1px solid #2e3147 !important;
}

/* Buttons */
.stButton button {
    background: linear-gradient(135deg,#4f8ef7,#6c63ff);
    color:white;
    border:none;
    border-radius:10px;
    font-weight:600;
}

/* Metrics */
[data-testid="metric-container"] {
    background:#1d2130;
    border:1px solid #2e3147;
    border-radius:12px;
    padding:10px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Session State
# --------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_session" not in st.session_state:
    st.session_state.chat_session = None

# --------------------------------------------------
# Gemini Initialization
# --------------------------------------------------
def initialize_chat():

    if not API_KEY:
        return None

    if st.session_state.chat_session is None:

        genai.configure(api_key=API_KEY)

        model = genai.GenerativeModel(
            model_name=MODEL_NAME,
            system_instruction=SYSTEM_PROMPT,
            generation_config=genai.GenerationConfig(
                temperature=TEMPERATURE,
                max_output_tokens=MAX_TOKENS
            )
        )

        history = []

        for msg in st.session_state.messages:

            role = "user" if msg["role"] == "user" else "model"

            history.append({
                "role": role,
                "parts": [msg["content"]]
            })

        st.session_state.chat_session = model.start_chat(
            history=history
        )

    return st.session_state.chat_session

# --------------------------------------------------
# Chat Handler
# --------------------------------------------------
def execute_chat_turn(prompt_text):

    current_time = datetime.now().strftime("%H:%M")

    st.session_state.messages.append({
        "role": "user",
        "content": prompt_text,
        "time": current_time
    })

    with st.spinner("GemBot is thinking..."):

        try:

            session = initialize_chat()

            if session:

                response = session.send_message(prompt_text)

                reply = (
                    response.text
                    if hasattr(response, "text")
                    else "No response generated."
                )

            else:
                reply = "Gemini API key not found in .env"

        except Exception as e:
            reply = f"Error: {str(e)}"

    st.session_state.messages.append({
        "role": "assistant",
        "content": reply,
        "time": datetime.now().strftime("%H:%M")
    })

    st.rerun()

# --------------------------------------------------
# Header
# --------------------------------------------------
st.markdown(
    "<div class='main-title'>🤖 GemBot Pro</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Powered by Google Gemini</div>",
    unsafe_allow_html=True
)

# --------------------------------------------------
# Chat Display
# --------------------------------------------------
for msg in st.session_state.messages:

    if msg["role"] == "user":

        st.markdown(
            f"""
            <div class="user-bubble">
            🧑 {msg["content"]}
            <br>
            <span class="timestamp">{msg["time"]}</span>
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class="bot-bubble">
            🤖 {msg["content"]}
            <br>
            <span class="timestamp">{msg["time"]}</span>
            </div>
            """,
            unsafe_allow_html=True
        )

# --------------------------------------------------
# Input Form
# --------------------------------------------------
with st.form("chat_form", clear_on_submit=True):

    user_input = st.text_input(
        "",
        placeholder="Ask anything..."
    )

    submitted = st.form_submit_button(
        "Send ➤",
        use_container_width=True
    )

if submitted and user_input.strip():

    execute_chat_turn(user_input.strip())

# --------------------------------------------------
# Welcome Screen
# --------------------------------------------------
if len(st.session_state.messages) == 0:

    st.markdown("""
    <div style="text-align:center;padding:30px;color:#8b93b0;">
        <div style="font-size:70px;">🤖</div>
        <h2>Welcome to GemBot Pro</h2>
        <p>Start chatting with Gemini AI.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 💡 Suggestions")

    suggestions = [
        "Explain Artificial Intelligence",
        "Write a Python Fibonacci Program",
        "What is Cloud Computing?",
        "Explain Machine Learning Simply"
    ]

    cols = st.columns(2)

    for i, suggestion in enumerate(suggestions):

        with cols[i % 2]:

            if st.button(
                suggestion,
                use_container_width=True
            ):
                execute_chat_turn(suggestion)

# --------------------------------------------------
# Footer Controls
# --------------------------------------------------
st.markdown("---")

turns = len([
    m for m in st.session_state.messages
    if m["role"] == "user"
])

col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    st.metric("Conversation Turns", turns)

    if st.button(
        "🗑 Clear Chat",
        use_container_width=True,
        key="footer_clear_chat"
    ):
        st.session_state.messages = []
        st.session_state.chat_session = None
        st.rerun()

st.markdown(
    """
    <div style="text-align:center;color:#8b93b0;padding:15px;">
        GemBot Pro • Powered by Google Gemini
    </div>
    """,
    unsafe_allow_html=True
)