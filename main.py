import random
import streamlit as st

def number_guessing_game():
    st.title("Number guessing game")

    # Init the game
    if "game active" not in st.session_state:
        st.session_state.guesses = 0
        st.session_state.game_active = False
        st.session_state.lives_left = 5
        st.session_state.max_lives = 5
    
    # Game start
    if st.button("Game Start"):
        st.session_state.game_active = True
        st.session_state.max_lives = 5
        st.session_state.lives_left = st.session_state.max_lives
        st.session_state.secret_number = random.randint(1, 500)
    
    st.write(f"{st.session_state.max_lives}")
    st.write(f"{st.session_state.lives_left}")

    guess = st.number_input("Guess the number")
    
    # Guessing the number
    if st.session_state.lives_left > 0:
        if st.button("Submit Number"):
            if guess == st.session_state.secret_number:
                st.write("Congratulations, you got the number")
                st.session_state.guesses += 1
                st.session_state.game_active = False
            
            else:
                st.write("Wrong number. Guess again")
                st.session_state.guesses += 1
                st.session_state.lives_left -= 1
                st.error(f"You have {st.session_state.lives_left} lives left")
                
                if st.session_state.lives_left > 0:
                    st.write("Wrong number. Guess again")
                else:
                    st.error(f"Game over. Try Again")
                    st.session_state.game_active = False
    

if __name__ == "__main__":
    number_guessing_game()

    

    