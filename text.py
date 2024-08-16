from chicken import Chicken

welcome = "Welcome to KFC!\n"
askname = "State your name: "
ask_choice = "Your choice: "

welcome_intro = "\nYou, {0}, have been selected to enter the renowned King of Fighting Chickens Tournament!!!!!! You have to fight your way through ruthless, savage chickens to become the CHAMPION, where you will be crowned KING of the chickens, and earn a grand prize.\n"

chicken_reminder = "{0}, please choose your chicken wisely: "
gmo_desc = "1. GMO Chicken \nThe model chicken. Perfectly well-balanced in every aspect, feisty and aggressive. Ready to murder any chickens for your love.\n"
organic_desc = "2. Organic Chicken: \nRaised with the greenest grass, crystal clear water, and the best conditions all around. Tanky and right in the pink of health. Could and would block a bullet for you.\n"

intros = [
    "{0} looks sad. You ask {0} what’s wrong.\n{0} says that his mother was kidnapped by another chicken.\nYou decide to find {0}’s mother with him.\n\nThe two of you go on a journey into the unknown...\nSuddenly, a black figure blocks your way, and fog hinders your vision.\nA distinct smell invades your senses.\nThe fog clears to reveal who is standing in your way.\nIt is chicken broth!\n",
    "You continue along the path with {0}...\nSuddenly, you hear thunderous footsteps. \nBefore you stood an army of chicken nuggets. \nThe chicken nuggets glared menacingly. ‘How dare you trespass our land! You shall be killed!'\n\n",
    "Although a bit battered, the both of you walk on further up a hill. \nYou see a long figure making its way towards you. \nIt is the tall and mighty chicken tender. \nStanding at almost 5m tall, the chicken tender used to be a key player in the NBCA (National Basketball Chicken Association) until an injury to its internal organs. \nThis sparked the chicken tender’s villain origin story. \n'I challenge you to a basketball match of death!'\n\n"

    # add more intros here
]

attack_list = ["Choose option:\n1. Kick \n2. Dodge"]

# [name, health, [{attack_name, lower_range, upper_range}]]
enemy_data = [
    {"enemy_name": "Chicken Broth", "enemy_health": 40, "enemy_attacks": [{"attack_name": "Hot Soup", "lower_range": 10, "upper_range": 15}, {"attack_name": "Steam", "lower_range": 8, "upper_range": 13}]}
]