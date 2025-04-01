import random
import streamlit as st

def number_guessing_game():
    st.title("Number guessing game")

    # Init the game
    if "game active" not in st.session_state:
        st.session_state.game_active = False
        st.session_state.lives_left = 0
        st.session_state.max_lives = 5
        st.session_state.guess = None
    
    # Game start
    if st.button("Game Start"):
        st.session_state.game_active = True
        st.session_state.max_lives = 5
        st.session_state.lives_left = st.session_state.max_lives
        st.session_state.secret_number = random.randint(1, 50)
        st.session_state.guesses = 0
    
    st.write(f"{st.session_state.max_lives}")
    st.write(f"{st.session_state.guesses}")

    st.session_state.guess = st.number_input("Guess the number from 1 to 5")
    
    # Guessing the number
    if st.session_state.lives_left > 0:
        if st.button("Submit Number"):
            if st.session_state.guess == st.session_state.secret_number:
                st.write("Congratulations, you got the number")
                st.session_state.guesses += 1
                st.session_state.game_active = False
            
            else:
                st.session_state.guesses += 1
                st.session_state.lives_left -= 1
    
                if st.session_state.lives_left > 0:
                    st.write(f"Wrong number. You have {st.session_state.lives_left} lives left")
                else:
                    st.error(f"Game over. Try Again")
                    st.session_state.game_active = False
    

if __name__ == "__main__":
    number_guessing_game()

    

    