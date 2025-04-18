import random
import streamlit as st

def number_guessing_game():
    st.title("Number guessing game")

    # Init the game
    if "game_active" not in st.session_state:
        st.session_state.game_active = False
        st.session_state.max_lives = 5
        st.session_state.guesses = 0
        st.session_state.lives_left = 0
        st.session_state.secret_number = 0
        
    start = st.button("Game Start")
    # Game start
    if start:
        if not st.session_state.game_active:
            st.session_state.guesses = 0
            st.session_state.game_active = True
            st.session_state.max_lives = 5
            st.session_state.lives_left = st.session_state.max_lives
            st.session_state.secret_number = random.randint(1, 50)
            
    
    st.write(f"{st.session_state.max_lives} max lives")
    st.write(f"{st.session_state.guesses} guesses")
    
    hint = st.button("Hint")
    
    user_guess = st.number_input("Guess the number between 1 and 50", step=1, min_value=1, max_value=50)
    
    
    # Guessing the number
    if st.button("Submit Number"):
        if st.session_state.lives_left > 0:
            guess = int(user_guess)
            st.session_state.guesses += 1
                
            if guess == st.session_state.secret_number:
                st.success("Congratulations, you got the number")
                st.session_state.game_active = False
            
            else:
                st.session_state.lives_left -= 1
        
                if st.session_state.lives_left > 1:
                    st.warning(f"Wrong number. Guess again. Lives left: {st.session_state.lives_left}")
                
                elif st.session_state.lives_left == 1:
                    st.warning(f"Last Life. Check carefully")
                    
                else:
                    st.error(f"Game Over. Try again. The correct answer was {st.session_state.secret_number}")
                    st.session_state.game_active = False

    # Hints
    if st.session_state.game_active and abs(user_guess - st.session_state.secret_number) <= 5:
        st.warning(f"Getting hotter")
    
    else:
        st.warning(f"Still cold")


    if hint:
        if st.session_state.lives_left > 1:
            st.session_state.lives_left -= 1
            st.write(f"The number squared is **{st.session_state.secret_number ** 2}**")
        
        else:
            st.warning(f"You're on your last life. No more hints")

    # Ending game
    if st.button("Reset game"):
        st.session_state.game_active = False
        st.session_state.secret_number = None



if __name__ == "__main__":
    number_guessing_game()

    

    
