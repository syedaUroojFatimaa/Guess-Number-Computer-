import streamlit as st
import random

# ---- Custom Styling ----
st.markdown("""
    <style>
    body {
        background-color: #f4f4f9;
    }
    .title {
        text-align: center;
        font-size: 32px;
        color: #2c3e50;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .message {
        font-size: 20px;
        font-weight: bold;
        color: #34495e;
    }
    .highlight {
        font-size: 22px;
        font-weight: bold;
        color: #27ae60;
    }
    </style>
""", unsafe_allow_html=True)

# ---- Initialize Session State Variables ----
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.leaderboard = []  # Store scores
    st.session_state.user_guess = None  # Store user guess

# ---- UI Components ----
st.markdown('<p class="title">🎯 Guess the Number Game</p>', unsafe_allow_html=True)
st.write("🤖 I have selected a number between **1 and 100**. Can you guess it?")

# ---- User Input ----
user_guess = st.number_input("🔢 Enter your guess:", min_value=1, max_value=100, step=1, format="%d", key="user_guess")

# ---- Submit Button ----
if st.button("🚀 Submit Guess"):
    if st.session_state.game_over:
        st.error("🔄 The game is over! Click 'Restart' to play again.")
    else:
        st.session_state.attempts += 1
        if user_guess < st.session_state.secret_number:
            st.warning("🔼 Too low! Try again. 💡")
        elif user_guess > st.session_state.secret_number:
            st.warning("🔽 Too high! Keep going! 😃")
        else:
            st.success(f"🎉 **Congratulations! You guessed it in {st.session_state.attempts} attempts!** 🎯")
            st.session_state.game_over = True
            st.session_state.leaderboard.append(st.session_state.attempts)
            st.balloons()

# ---- Restart Button ----
if st.button("🔄 Restart Game"):
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.user_guess = None  # Reset input field
    st.rerun()

# ---- Display Leaderboard ----
if st.session_state.leaderboard:
    st.subheader("🏆 Leaderboard - Best Scores")
    sorted_scores = sorted(st.session_state.leaderboard)[:5]  # Top 5 best scores
    for i, score in enumerate(sorted_scores, start=1):
        st.markdown(f"**{i}. {score} attempts** ⏳")
