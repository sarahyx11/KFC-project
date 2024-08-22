# Import statements
from game import Game

game = Game()

if __name__ == "__main__":
    game.welcome()
    game.choose_chicken()
    for day in range(1, 6):
        game.set_day(day)
        npc = game.prep_day()
        while not game.enemy_beaten(npc):
            game.intro()
            npc = game.prep_day()
            while not game.fight_is_over(npc):
                game.print_stats(npc)
                choice = game.prompt_player()
                defence = game.do(choice, npc)
                game.npc_attacks(npc, defence)
                if game.fight_is_over(npc):
                    break
        game.debrief()
    game.ending()
    game.is_over()
    
