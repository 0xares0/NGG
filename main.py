import random
import streamlit as st

def number_guessing_game():
    st.title("2-player Number guessing game")

    #store player data
    if "players" not in st.session_state:
        st.session_state.players = {
            'player1' : {
                'attempts': 0,
                'secret_number': 0,
                'score': 0,
                'history': []
            },

            'player2': {
                'attempts': 0,
                'secret_number': 0,
                'score': 0,
                'history': []
            }
        }
    
    # Init the game
    if "game_active" not in st.session_state:
        st.session_state.game_active = False
    
     # init players
    if "current_player" not in st.session_state:
        st.session_state.current_player = 'player1'
        
    start = st.button("Game Start")
    # Game start
    if start:
        if not st.session_state.game_active:
            st.session_state.game_active = True
            st.session_state.current_player
            st.session_state.players['player1']['secret_number'] = random.randint(1, 50)
            st.session_state.players['player2']['secret_number'] = random.randint(51, 100)

    
    # switch player
    def switch_player():
        if st.session_state.current_player == 'player1':
            st.session_state.current_player = 'player2' 

        else:
           st.session_state.current_player = 'player1' 
            

    st.write(f"{st.session_state.players[st.session_state.current_player]['attempts']} attempts")
    
    hint = st.button("Hint")

    # Input guess
    if st.session_state.current_player == 'player1':
        user_guess = st.number_input("Guess the number between 1 and 50", step=1, min_value=1, max_value=50)
    else:
        user_guess = st.number_input("Guess the number between 51 and 100", step=1, min_value=51, max_value=100)
    
    other_player = 'player2' if st.session_state.current_player == 'player1' else 'player1'
    # Guessing the number
    if st.button("Submit Number"):
        guess = int(user_guess)
        st.session_state.players[st.session_state.current_player]['attempts'] += 1
                
        if guess == st.session_state.players[st.session_state.current_player]['secret_number']:
            st.success("Congratulations, you got the number")
            st.session_state.players[st.session_state.current_player]['score'] += 1
            
        else:
            st.warning(f"Wrong number. {other_player}'s turn")
            switch_player()
        
            
    # Hints
    if st.session_state.game_active and abs(user_guess - st.session_state.players[st.session_state.current_player]['secret_number']) <= 5:
        st.warning(f"Getting hotter")
    
    else:
        st.warning(f"Still cold")


    if hint:
            st.session_state.players[st.session_state.current_player]['attempts'] -= 1
            st.write(f"The number squared is **{st.session_state.players[st.session_state.current_player]['secret_number'] ** 2}**")
            st.write(f"You lose your turn")
            switch_player()

        
        
    # Reset game
    if st.button("Reset game"):
        st.session_state.game_active = False
        st.session_state.secret_number = 0



if __name__ == "__main__":
    number_guessing_game()

    

    
