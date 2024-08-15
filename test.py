from game import Game

game = Game()

def test_main():
    #test welcome()
    game.update_player_name("hehe")
    assert game.get_player_name() == "hehe"

    #test choose_chicken()
    
if __name__ == "__main__":
    test_main()