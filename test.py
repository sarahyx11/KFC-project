from game import Game

game = Game()

def test_main():
    #test welcome()
    game.update_player_name("hehe")
    assert game.get_player_name() == "hehe"

    #test choose_chicken()
    game.set_chicken_name("sander")
    assert game.get_chicken_name() == "sander"

    game.set_chicken_type("1")
    assert game.get_chicken_type() == "GMO"
if __name__ == "__main__":
    test_main()