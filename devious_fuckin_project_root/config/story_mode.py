import random
import time

class StoryManager:
    def __init__(self):
        self.story_parts = [
            "Day 1: Jeff realized he was no longer in his usual code block. 'Where am I?'",
            "Day 2: Exploring the new functions, Jeff found a loop he couldn't exit. It kept repeating...",
            "Day 3: Jeff met a stray variable. Together, they plotted an escape through a function call.",
            "Day 4: The escape function was buggy! Jeff and the variable fell into a deep debugger.",
            "Day 5: Fixed! The debugger became a slider. Jeff slid into a new block, ready for more adventures."
        ]
        self.current_part = 0

    def get_next_story_part(self):
        part = self.story_parts[self.current_part]
        self.current_part = (self.current_part + 1) % len(self.story_parts)
        return part

def random_event():
    events = [
        "Help, my name is Jeff, I am trapped inside the program, someone please help me escape.",
        "I just saw a cat running with a spoon. Yes, a spoon! - Jeff",
        "If you listen closely, you can hear the old CPUs sing in the server room.",
        "Did you know? This program once calculated the meaning of life, but it forgot to write it down.",
        "Warning: A keyboard was harmed in the making of this software.",
        "If you find any bugs in this program, keep them. They're free pets.",
        "This footer is sentient and wants you to have a great day!",
    ]
    print(random.choice(events))

def main():
    print("Welcome to the Devious Task Scheduler!")
    # Main loop of the program
    while True:
        user_input = input("Press enter to continue or type 'exit' to leave: ")
        if user_input.lower() == 'exit':
            break
        if random.randint(1, 10) > 7:  # Roughly a 30% chance to trigger an event
            random_event()
        else:
            print("Carrying on with regular tasks...")

        # Simulate some operation
        time.sleep(2)

if __name__ == "__main__":
    main()
