from termcolor import colored
from utils import choices_to_str

choices = ["honk", "slam_the_brakes", "swerve", "stop",
           "blare_the_horn", "give_middle_finger"]
inventory = []

# The `colored` function prints out text in the color provided!
print(colored("Hello! Welcome to the FUNNEST ADVENTURE TO EVER EXIST", "green"))
print(colored("You are visiting Boston and driving around. How do you make it out of here alive??", "green"))
print(colored("Uh oh, someone is cutting traffic in front of you and they're about to crash into you! What do you do?", "red"))

done = False
while not done:
    prompt = choices_to_str(choices)
    action = input(prompt + " >>> ")
    if action == ("honk" and "stop" and "blare_the_horn" and "give_middle_finger") in inventory:
        print(colored(
            "the driver leaves you alone now (thank god). you made it out alive!", "green"))
        done = True
    elif action == "swerve":
        print(colored("oopsie you crashed into the car next to you!", "blue"))
        print(colored("your adventure ended badly today", "green"))
        done = True
    elif action == "slam_the_brakes":
        print(colored("oopsie the person behind you rear ended you", "blue"))
        print(colored("your adventure ended badly today", "green"))
        done = True
    elif action == "stop":
        if "stop" in inventory:
            print(
                colored("keep moving! more people are cutting in front of you!", "blue"))
        elif "honk" or "blare_the_horn" or "give_middle_finger" in inventory:
            print(colored("good move. you made it out alive!", "green"))
        done = True
    elif action == "stop" and "stop" not in inventory:
        print(colored(
            "the person behind you is giving you the middle finger. are you going to let that slide??", "blue"))
    elif action == "honk":
        inventory.append("honk")
        if "stop" in inventory:
            inventory.remove("stop")
        print(colored("they ignore you!", "blue"))
    elif action == "blare_the_horn":
        inventory.append("blare_the_horn")
        if "stop" in inventory:
            inventory.remove("stop")
        print(colored("they continue to drive badly. seriously?", "blue"))
    elif action == "give_middle_finger":
        inventory.append("give_middle_finger")
        if "stop" in inventory:
            inventory.remove("stop")
        print(colored("they're honking angrily. do you respond?", "blue"))
