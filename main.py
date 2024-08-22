# Import statements
from game import Game

game = Game()

if __name__ == "__main__":
    game.welcome()
    game.choose_chicken()
    game.create_shop()
    for day in range(1, 6):
        game.set_day(day)
        game.intro()
        npc = game.prep_day()
        while not game.enemy_beaten(npc):
            npc = game.prep_day()
            while not game.fight_is_over(npc):
                game.print_stats(npc)
                choice = game.prompt_player()
                game.do(choice, npc)
                defence = game.do(choice, npc)
                game.npc_attacks(npc, defence)
                if game.fight_is_over(npc):
                    break
            game.fight_over_message(npc)
            
        if str(day) in "134":
            game.go_shop()
        game.debrief()
    game.ending()
    game.is_over()
    
