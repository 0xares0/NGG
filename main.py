import random
import streamlit

def number_guessing_game():
    st.title("Number guessing game")

    # Init the game
    if "game active" not in st.session_state:
        st.session_state.guesses = 0
        st.session_state.game_active = "False"
        st.session_state.lives_left = 0
        st.session_state.max_lives = 0
    
    # Game start
    if "game active" in st.session_state:
        st.session_state.game_active = "True"
        st.session_state.lives_left = 5
        st.session_state.max_lives = 5
        st.session_state.secret_number = random(1, 500)
        st.number_input("Guess the number")
    
    # Guessing the number
    while st.session_state.lives_left > 5:
        if st.number_input == st.session_state.secret_number:
            st.write("Congratulations, you got the number")
            st.session_state.guesses += 1
        
        elif st.number_input != st.session_state.secret_number:
            st.write("Wrong number. Guess again")
            st.session_state.guesses += 1
            st.session_state.lives_left -= 1
    
    st.write("Game Over.")

    if st.button("Game Start"):
        st.session_state.game_active = 'True'

if __name__ == "__main__":
    main()

    

    