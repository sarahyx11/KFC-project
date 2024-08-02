# Import statements
import ...

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

    colours = {"white": "\x1b[0m", "red": "\x1b[31m", "green": "\x1b[32m", "yellow":  "\x1b[33m", "blue": "\x1b[34m", "purple": "\x1b[35m"}
    
