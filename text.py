from chicken import Chicken

welcome_msg = "Welcome to KFC!\n"
def welcome_player():
    print(welcome_msg)

askname = "State your name: "
def prompt_player_name() -> str:
    name = input(askname)
    return name

gmo_desc = "1. GMO Chicken \nThe model chicken. Perfectly well-balanced in every aspect, feisty and aggressive. Ready to murder any chickens for your love.\n"
organic_desc = "2. Organic Chicken: \nRaised with the greenest grass, crystal clear water, and the best conditions all around. Tanky and right in the pink of health. Could and would block a bullet for you.\n"
ask_choice = "Your choice: "
def choose_chicken() -> tuple[str, str]:
    print(gmo_desc)
    print(organic_desc)
    choice = input(ask_choice)
    while choice not in "12":
        choice = input("Invalid choice, input 1 or 2: ")
    if choice == '1':
        ctype = 'Oganic'
    elif choice == '2':
        ctype = 'GMO'
    else:
        raise ValueError("Invalid choice")
    name = input("\nCongratulations on receiving your one and only {ctype} Chicken! What will their name be? \n")
    return ctype, name

def chicken_chosen(name: str) -> None:
    print(f"\n{name} pecks your face with affection.\n\n")

def prompt_valid_choice(options: list[str], prompt: str = "") -> str:
    """Prompt the user for a valid choice from a list of options"""
    if prompt:
        print(prompt)
    for i, choice in enumerate(options, start=1):
        print(f"{i}. {choice}")
    choice = input("Choose a number: ")
    while not choice.isdecimal() and 1 <= int(choice) <= len(options):
        print("Invalid choice.")
        choice = input("Choose a number: ")
    return options[int(choice) - 1]

def prompt_valid_range(start: int, end: int, prompt: str = "") -> int:
    """Prompt the user for a valid number within a range of numbers"""
    if prompt:
        print(prompt)
    choice = input(f"Enter number({start} - {end}): ")
    while not choice.isdecimal() or not start <= int(choice) <= end:
        print("Invalid number.")
        choice = input(f"Enter number({start} - {end}): ")
    return int(choice)

def prompt_y_or_n(prompt: str = "", default: str | None = None) -> str:
    """Prompt the user for a yes or no answer.
    If default is 'y' or 'n', an empty response will be treated as a default response.
    """
    if default and default.lower() == "y":
        options = "(Y/n)"
    elif default and default.lower() == "n":
        options = "(y/N)"
    else:
        options = "(y/n)"
    choice = input(f"{prompt} {options}: ")
    if default is None and choice.lower() not in "yn":
        print("Invalid choice.")
        choice = input(f"{prompt} {options}: ")
    return choice

def attack_report(report: dict) -> str:
    return f"{report['attacker_name']} ({report['attacker_hp']} HP) used {report['move_name']} on {report['defender_name']} ({report['defender_hp'] HP})! {report['defender_name']} took {report['damage_taken']} damage."

def day_header(day):
    return f"====== DAY {day} ======"

def show_fight_stats(chicken: dict, enemy: dict) -> None:
    print(f"Your Strength: {chicken['strength']}")
    print(f"Your Health: {chicken["health"]}")
    print(f"Enemy's Health: {enemy['health']}")


welcome_intro = "\nYou, {name}, have been selected to enter the renowned King of Fighting Chickens Tournament!!!!!! You have to fight your way through ruthless, savage chickens to become the CHAMPION, where you will be crowned KING of the chickens, and earn a grand prize.\n"

chicken_reminder = "{name}, please choose your chicken wisely: "

shop_message = "Welcome to Chicken Coop! What would you like to do?"
shop_options = ["Check price list", "Buy item", "Exit"]

coin_reminder = "If your coins remain negative at end of day 5, you lose."

intros = [
    # day 1
    "{cname} looks sad. You ask {cname} what’s wrong.\n{cname} says that his mother was kidnapped by another chicken.\nYou decide to find {cname}’s mother with him.\n\nThe two of you go on a journey into the unknown...\nSuddenly, a black figure blocks your way, and fog hinders your vision.\nA distinct smell invades your senses.\nThe fog clears to reveal who is standing in your way.\nIt is Chicken Broth!\n",
    # day 2
    "You continue along the path with {cname}...\nSuddenly, you hear thunderous footsteps. \nBefore you stood an army of chicken nuggets. \nThe chicken nuggets glared menacingly. ‘How dare you trespass our land! You shall be killed!'\n\n",
    # day 3
    "Although a bit battered, the both of you walk on further up a hill. \nYou see a long figure making its way towards you. \nIt is the tall and mighty chicken tender. \nStanding at almost 5m tall, the chicken tender used to be a key player in the NBCA (National Basketball Chicken Association) until an injury to its internal organs. \nThis sparked the chicken tender’s villain origin story. \n'I challenge you to a basketball match of death!'\n\n",
    # day 4
    "As you move on with your journey, you spot a deformed shadow. Upon closer inspection, the shadow is a massive piece of crispy fried chicken with a sticky layer of mayo slathered on each side. Despite its larger stature and width, the chicken seemed agile, prancing away. The chicken revealed itself to be none other than the famous Mcspicy, a renowned dancer. The Mcspicy looked at your measly (chicken name) and laughed, and said “I challenge you to a dance battle!”. ‘Karma’ by Jojo Siwa fades in.",
    # day 5
    "After an arduous journey, fighting all those types of chickens, {cname} has gained more skill, strength and health. After spotting a mysterious cave, you enter it, while being hit with a stench of steamed chicken. 'After all these days, I have found you. I’m sure you know why I’m here', your {cname} retorted. The steam chicken grimaced upon the sight of your puny looking {cname}. 'Do you really think you can defeat me? After all these years I have spent training to crush your family?'' {cname} looked quizzical. 'I guess they never told you, as expected… I’m your brother, our ‘father’ steamed me in an experiment and turned me into this! In an ‘accident’ your father died, and I swore I wouldn’t let you live happily either!'' Without any time to react, Steam Chicken attacked."
]
