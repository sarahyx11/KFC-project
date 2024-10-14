# Import statements
from game import Game
import text

game = Game()


if __name__ == "__main__":
    text.welcome_player()
    player_name = text.prompt_player_name()
    game.update_player_name(player_name)
    chicken_type, chicken_name = text.choose_chicken()
    game.set_chicken(chicken_type, chicken_name)
    text.chicken_chosen(chicken_name)
    game.create_shop()
    for day in range(1, 6):
        game.set_day(day)
        print(text.day_header(day))
        enemy = game.create_enemy_of_the_day()
        game.fight(enemy)
        if enemy.is_dead():
            game.chicken_won_fight(enemy)
        elif game.chicken.is_dead():
            game.chicken_lost_fight(enemy)

        if str(day) in "134":
            game.go_shop()
        game.debrief()
    game.ending()
    game.is_over()
