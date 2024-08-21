from chicken import Chicken

welcome = "Welcome to KFC!\n"
askname = "State your name: "
ask_choice = "Your choice: "

welcome_intro = "\nYou, {0}, have been selected to enter the renowned King of Fighting Chickens Tournament!!!!!! You have to fight your way through ruthless, savage chickens to become the CHAMPION, where you will be crowned KING of the chickens, and earn a grand prize.\n"

chicken_reminder = "{0}, please choose your chicken wisely: "
gmo_desc = "1. GMO Chicken \nThe model chicken. Perfectly well-balanced in every aspect, feisty and aggressive. Ready to murder any chickens for your love.\n"
organic_desc = "2. Organic Chicken: \nRaised with the greenest grass, crystal clear water, and the best conditions all around. Tanky and right in the pink of health. Could and would block a bullet for you.\n"

intros = [
    # day 1
    "{0} looks sad. You ask {0} what’s wrong.\n{0} says that his mother was kidnapped by another chicken.\nYou decide to find {0}’s mother with him.\n\nThe two of you go on a journey into the unknown...\nSuddenly, a black figure blocks your way, and fog hinders your vision.\nA distinct smell invades your senses.\nThe fog clears to reveal who is standing in your way.\nIt is Chicken Broth!\n",
    # day 2
    "You continue along the path with {0}...\nSuddenly, you hear thunderous footsteps. \nBefore you stood an army of chicken nuggets. \nThe chicken nuggets glared menacingly. ‘How dare you trespass our land! You shall be killed!'\n\n",
    # day 3
    "Although a bit battered, the both of you walk on further up a hill. \nYou see a long figure making its way towards you. \nIt is the tall and mighty chicken tender. \nStanding at almost 5m tall, the chicken tender used to be a key player in the NBCA (National Basketball Chicken Association) until an injury to its internal organs. \nThis sparked the chicken tender’s villain origin story. \n'I challenge you to a basketball match of death!'\n\n",
    # day 4
    "As you move on with your journey, you spot a deformed shadow. Upon closer inspection, the shadow is a massive piece of crispy fried chicken with a sticky layer of mayo slathered on each side. Despite its larger stature and width, the chicken seemed agile, prancing away. The chicken revealed itself to be none other than the famous Mcspicy, a renowned dancer. The Mcspicy looked at your measly (chicken name) and laughed, and said “I challenge you to a dance battle!”. ‘Karma’ by JoJo Siwa fades in.",
    # day 5
    "After an arduous journey, fighting all those types of chickens, your {0} has gained more skill, strength and health. After spotting a mysterious cave, you enter it, while being hit with a stench of steamed chicken. “After all these days, I have found you. I’m sure you know why I’m here”, your {0} retorted. The steam chicken grimaced upon the sight of your puny scrawly looking {0}. “Do you really think you can defeat me? After all these years I have spent training to crush your family?” {0} looked quizzical.“ I guess they never told you, as expected… I’m your brother, our ‘father’ steamed me in an experiment and turned me into this! In an ‘accident’ your father died, and I swore I wouldn’t let you live happily either!” without time to think through, Steam Chicken attacked."
]

attack_list = [
    # day 1
    [{"name": "Kick", "atk": 10, "def": 0}, {"name": "Dodge", "atk": 2, "def": 8}],
    # day 2
    [{"name": "Kick", "atk": 15, "def": 0}, {"name": "Dodge", "atk": 2, "def": 8}],
    # day 3
    [{"name": "Dribble", "atk": 15, "def": 5}, {"name": "Shoot", "atk": 20, "def": 0}],
    # day 4
    [{"name": "Dougie", "atk": 22, "def": 3}, {"name": "Dab", "atk": 25, "def": 0}],
    # day 5
    [{"name": "Roast", "atk": 25, "def": 5}, {"name": "Soy Sauce", "atk": 30, "def": 0}]
]

# [name, health, [{attack_name, lower_range, upper_range}]]
enemy_data = [
    # day 1
    {"enemy_name": "Chicken Broth", "enemy_health": 40, "enemy_attacks": [{"attack_name": "Hot Soup", "atk": 12}, {"attack_name": "Steam", "atk": 10}]},
    # day 2
    {"enemy_name": "Chicken Nugget", "enemy_health": 50, "enemy_attacks": [{"attack_name": "Hot Oil", "atk": 15}, {"attack_name": "Spices", "atk": 17}]},
    # day 3
    {"enemy_name": "Chicken Tender", "enemy_health": 70, "enemy_attacks": [{"attack_name": "Slam Dunk", "atk": 20}, {"attack_name": "3 Pointer", "atk": 23}]},
    # day 4
    {"enemy_name": "McSpicy", "enemy_health": 100, "enemy_attacks": [{"attack_name": "Plie", "atk": 25}, {"attack_name": "Glissade", "atk": 27}]},
    # day 5
    {"enemy_name": "Steam Chicken", "enemy_health": 190, "enemy_attacks": [{"attack_name": "Cook", "atk": 40}, {"attack_name": "Steam", "atk": 45}]}
]