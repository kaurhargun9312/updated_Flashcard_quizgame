# Ask the user for their name
user = input("Hi, Give a username for you: ")

# Save the username to a file for record-keeping
with open("quiz_users.txt", "a") as file:
    file.write(user + "\n")

print("PERFECT! ", user, " Lets start the quiz, BEST OF LUCK!! ")

# Easy level flashcards (general knowledge)
Flashcards = {
    "What color is the sky on a clear day?": "Blue",
    "How many legs does a spider have?": "8",
    "What is 5 + 3?": "8",
    "What fruit is known for keeping the doctor away if you eat one a day?": "Apple",
    "What do bees make?": "Honey",
    "Which planet do we live on?": "Earth",
    "What sound does a cow make?": "Moo",
    "How many days are in a week?": "7",
    "What is the opposite of hot?": "Cold",
    "What do you use to write on a blackboard?": "Chalk"
}

# Medium level flashcards (basic tech and Python)
Flashcards_med = {
    "What comes next in the pattern: 2, 4, 8, 16, ?": "132",
    "If a dozen eggs cost $6, what is the cost of 1 egg?": "0.5",
    "What number is 3 more than twice 4?": "11",
    "What is the missing number: 5, 10, __, 20, 25?": "15",
    "If you divide 30 by half and add 10, what do you get?": "70",
    "How many sides does a hexagon have?": "6",
    "Which number is both a square and a cube between 1 and 100?": "64",
    "Whats the result of: (5 + 3) * 2?": "16",
    "What number is 25precent of 80?": "20",
    "If a train moves at 60 km/h for 2 hours, how far does it go?": "120"
}


# Hard level flashcards (advanced programming/math)
Flashcards_hard = {
    "I am an odd number. Take away one letter and I become even. What am I?": "Seven",
    "A clock shows 3:15. What is the angle between the hour and minute hand?": "7.5",
    "What number comes next: 1, 1, 2, 3, 5, 8, ?": "13",
    "If a rope is cut into 4 equal parts, each is 2.5m long. What was the original length?": "10",
    "You see me once in a minute, twice in a moment, but never in a thousand years. What am I?": "M",
    "A bat and a ball cost $1.10 total. The bat costs $1 more than the ball. How much is the ball?": "0.05",
    "A farmer has 17 sheep. All but 9 run away. How many are left?": "9",
    "What is the square root of 144 + square root of 81?": "21",
    "If 2 pencils cost 8 cents, how much do 10 pencils cost?": "40",
    "What 3-digit number has digits that add up to 9 and is divisible by 9?": "117"
}


# Game loop – keeps running until user chooses to exit
while True:
    print("1. Easy \n 2. Medium \n 3. Hard \n 4. Exit")
    choice = input("Choose what level you want to play? ")
    choice = int(choice)

    # Easy level gameplay
    if choice == 1:
        Score = 0
        for Question, answer in Flashcards.items():
            user_answer = input(Question + " ")
            if user_answer.lower() == answer.lower():
                print("Correct you got it right :) ")
                Score += 1
            else:
                print("Oops wrong one!! ")
        print("Your Final Score is: " + str(Score) + " points")

        # Save Easy score to file
        with open("scores.txt", "a") as file:
            file.write(f"{user} - Easy: {Score} points\n")

    # Medium level gameplay
    elif choice == 2:
        Score_med = 0
        for question, answer in Flashcards_med.items():
            user_answer = input(question + " ")
            if user_answer.lower() == answer.lower():
                print("Correct! You got it right :)")
                Score_med += 1
            else:
                print("Oops, wrong one!!")
        print("Your Final Score is: " + str(Score_med) + " points")

        # Save Medium score to file
        with open("scores.txt", "a") as file:
            file.write(f"{user} - Medium: {Score_med} points\n")

    # Hard level gameplay
    elif choice == 3:
        Score_hard = 0
        for Question, answer in Flashcards_hard.items():
            user_answer = input(Question + " ")
            if user_answer.lower() == answer.lower():
                print("Correct you got it right :) ")
                Score_hard += 1
            else:
                print("Oops wrong one!! ")
        print("Your Final Score is: " + str(Score_hard) + " points")

        # Save Hard score to file
        with open("scores.txt", "a") as file:
            file.write(f"{user} - Hard: {Score_hard} points\n")

    # Exit option
    elif choice == 4:
        print("Thank you! Have a great day :) ")
        break

    # Catch invalid choices
    else:
        print("You selected a wrong option")
