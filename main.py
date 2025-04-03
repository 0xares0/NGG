import random
import streamlit as st

def number_guessing_game():
    st.title("Number guessing game")

    # Init the game
    if "game active" not in st.session_state:
        st.session_state.guesses = 0
        st.session_state.game_active = False
        st.session_state.lives_left = 0
        st.session_state.max_lives = 5
        
    
    # Game start
    if st.button("Game Start") or not st.session_state.game_active:
        st.session_state.game_active = True
        st.session_state.max_lives = 5
        st.session_state.lives_left = st.session_state.max_lives
        st.session_state.secret_number = random.randint(1, 50)
        st.session_state.guess = None
    
    st.write(f"{st.session_state.max_lives}")
    st.write(f"{st.session_state.guesses} guesses")
    
    user_guess = st.number_input("Guess the number between 1 and 50", step=1)
    
    # Guessing the number
    if st.session_state.game_active and st.session_state.lives_left > 0:
        if st.button("Submit Number"):
            st.session_state.guess = int(user_guess)
            
            if st.session_state.guess == st.session_state.secret_number:
                st.success("Congratulations, you got the number")
                st.session_state.game_active = False
            
            else:
                
                st.session_state.guesses += 1
                st.session_state.lives_left -= 1
                
                if st.session_state.lives_left > 0:
                    st.warning(f"Wrong number. Guess again. Lives left: {st.session_state.lives_left}")
                    
                else:
                    st.error(f"Game Over. Try again. The correct answer was {st.session_state.secret_number}")
                    st.session_state.game_active = False
    

if __name__ == "__main__":
    number_guessing_game()

    

    
