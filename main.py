# Import statements
import game

game = Game()

if __name__ == "__main__":
    game.welcome()
    game.choose_chicken()
    for day in range(1, 6):
        game.set_day(day)
        game.intro()
        while not game.day_is_over():
            choice = game.prompt_player()
            game.do(choice)
            game.display_result()
        game.debrief()
    game.ending()
    game.is_over()
