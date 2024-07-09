"""
I ventured into functions in my code, which seemed like an 
excellent way to make my code more functional. At first, 
I had trouble understanding how they worked, but I think it worked. 
I presented it to two of my children, and they felt motivated to finish the game. 
It was an enriching experience for all three of us 
I also included the if __name__ == '__main__': script as a good programming practice 
to separate reusable functions from those of the main program
"""

import time

def introduction():
    """Introduce the player to the game and ask for their name."""
    name = input("Before we start, we need to know your name: ")
    print("\nWelcome, " + name + ", to your adventure in a magical world.")
    time.sleep(1)
    print("You find yourself in a realm full of wonders and dangers.")

    return name

def quest_decision(name):
    """Ask the player if they want to embark on the epic quest."""
    print("\nAn ancient prophecy speaks of two mystical stones that, when united, "
          "will bring balance and prosperity to the realm.")
    time.sleep(1)
    print("These stones are hidden in the realms of Etheria and Mystara.")
    print("\nWould you like to embark on this epic quest?")
    print("Yes / No")

    do = input('<<< ').lower()
    if do == 'yes' or do == 'y':
        print("\nExcellent choice, brave adventurer!")
        print("Now, choose in which realm you would like to begin your quest: Etheria or Mystara.")

        return choose_realm(name)
    else:
        print("\n" + name + ", you have decided not to embark on this adventure. Perhaps another time!")

def choose_realm(name):
    """Ask the player to choose between the realms of Etheria and Mystara."""
    print(f"\n{name}, you must now choose to explore either Etheria or Mystara.")
    realm_choice = input('<<< ').lower()

    if realm_choice == 'etheria':
        return explore_etheria(name)
    elif realm_choice == 'mystara':
        return explore_mystara(name)
    else:
        print("\nInvalid choice. Please choose either Etheria or Mystara.")
        return choose_realm(name)

def explore_etheria(name):
    """Handle the player's choices and events in the realm of Etheria."""
    print(f"\n{name}, you have chosen to explore Etheria, the realm of magic and mysteries.")
    time.sleep(1)
    print("You find yourself in the City of Storms, where the first stone is rumored to be hidden.")
    time.sleep(1)
    print("You can search the ancient library or venture into the enchanted forest.")
    print("Where would you like to go first? Library / Forest")

    location_choice = input('<<< ').lower()

    if location_choice == 'library':
        return explore_library(name)
    elif location_choice == 'forest':
        return explore_forest(name)
    else:
        print("\nInvalid choice. Please choose either Library or Forest.")
        return explore_etheria(name)

def explore_library(name):
    """Handle the player's choices and events in the ancient library of Etheria."""
    print(f"\n{name}, as you enter the library, you encounter a wise old mage named Merlin.")
    time.sleep(1)
    print("Merlin offers his assistance and shares information about the location of the first stone.")
    time.sleep(1)
    print("He gives you a magical map that will guide you to the stone. Good luck on your journey!")

    print(f"\n{name}, do you want to continue your search in Mystara? (Yes/No)")

    continue_choice = input('<<< ').lower()
    if continue_choice == 'yes' or continue_choice == 'y':
        print(f"\n{name}, your bravery is admirable. You embark on Mystara for the second stone.")
        time.sleep(1)
        print("On the way, you face challenges and make new allies.")
        time.sleep(1)
        print("Finally, you find the second stone and unite both, fulfilling the prophecy.")
        print("You are the hero the realm has been waiting for!")
    else:
        print(f"\n{name}, you have decided not to continue your quest in Mystara. Thank you for playing!")

def explore_forest(name):
    """Handle the player's choices and events in the enchanted forest of Etheria."""
    print(f"\n{name}, as you venture into the enchanted forest, you encounter magical creatures and challenges.")
    time.sleep(1)
    print("After overcoming the trials, you discover an ancient altar where the first stone is gleaming.")
    print("You have successfully found it. Do you want to search for the stone in Mystara now? (Yes/No)")

    continue_choice = input('<<< ').lower()
    if continue_choice == 'yes' or continue_choice == 'y':
        print(f"\n{name}, you decide to expand your search in the realm of Mystara.")
        time.sleep(1)
        print("Exciting challenges and new discoveries await you.")
        time.sleep(1)
        print("Finally, you find the second stone and unite both, fulfilling the prophecy.")
        print("You are the hero the realm has been waiting for!")
    else:
        print(f"\n{name}, you decide not to continue your quest in Mystara. Thank you for playing!")

def explore_mystara(name):
    """Handle the player's choices and events in the realm of Mystara."""
    print(f"\n{name}, you have chosen to explore Mystara, the realm of nature and hidden secrets.")
    time.sleep(1)
    print("You find yourself in the City of Shadows, where the first stone is said to be hidden.")
    time.sleep(1)
    print("You can investigate the ancient cave or venture into the Valley of Whispers.")
    print("Where would you like to go first? Cave / Valley")

    location_choice = input('<<< ').lower()

    if location_choice == 'cave':
        return explore_cave(name)
    elif location_choice == 'valley':
        return explore_valley(name)
    else:
        print("\nInvalid choice. Please choose either Cave or Valley.")
        return explore_mystara(name)

def explore_cave(name):
    """Handle the player's choices and events in the ancient cave of Mystara."""
    print(f"\n{name}, while exploring the ancient cave, you encounter underground creatures and puzzles.")
    time.sleep(1)
    print("At the end of the cave, you discover the first stone shining on an ancient altar.")
    print("You have successfully found it. Do you want to search for the stone in Etheria now? (Yes/No)")

    continue_choice = input('<<< ').lower()
    if continue_choice == 'yes' or continue_choice == 'y':
        print(f"\n{name}, you decide to venture now into the realm of Etheria.")
        time.sleep(1)
        print("Exciting wonders and magical challenges await you.")
        time.sleep(1)
        print("Finally, you find the second stone and unite both, fulfilling the prophecy.")
        print("You are the hero the realm has been waiting for!")
    else:
        print(f"\n{name}, you decide not to continue your quest in Etheria. Thank you for playing!")

def explore_valley(name):
    """Handle the player's choices and events in the Valley of Whispers in Mystara."""
    print(f"\n{name}, while venturing into the Valley of Whispers, you hear mysterious whispers and encounter ancient guardians.")
    time.sleep(1)
    print("After overcoming the trials, you reach the center of the valley, where you find the first stone guarded by the goddess of nature.")
    print("You have successfully found it. Do you want to search for the stone in Etheria now? (Yes/No)")

    continue_choice = input('<<< ').lower()
    if continue_choice == 'yes' or continue_choice == 'y':
        print(f"\n{name}, you decide to expand your search in the realm of Etheria.")
        time.sleep(1)
        print("New wonders and magical challenges await you.")
        time.sleep(1)
        print("Finally, you find the second stone and unite both, fulfilling the prophecy.")
        print("You are the hero the realm has been waiting for!")

if __name__ == "__main__":
    player_name = introduction()
    quest_decision(player_name)
