import math
import random

# Start Screen
def main():

	# Print the game rules
	print("Welcome to the Game! Here are the rules:")
	print("- Choose any number between 1 and 50.")
	print("- If you guess the number correctly at your 1st attempt, you will get 10 times of money you bet.")
	print("- If you guess the number correctly at the 2nd attempt, you will get 5 times of money you bet.")
	print("- If you guess the number correctly at the 3rd attempt, you will get 3 times of money you bet.")
	print("- If you do not guess the number correctly within three attempts, you will lose your betting amount.")
	print("")

	name = input("Please enter your name:")

	# Get the initial balance
	while True:
		balance = int(input("Please enter your initial balance:"))
		if not balance > 0:
			print("Balance must be greater than 0. Please try again")
		else:
			break
	
	# Start the game
	play_round(name, balance)

def play_round(name, balance):
	print()

	bet = 0

	# Enter the betting amount
	while True:
		bet = int(input("Enter bet (Balance=" + str(balance) +  "):"))
		if bet < 0:
			print("Bet must be greater than 0.")
		elif bet > balance:
			print("Not enough balance")
		else:
			break

	print("All right, lets play!")

	# Remove the bet from the player balance
	new_balance = balance - bet

	# Generate the answer
	answer = random.randint(1, 50)
	
	# True if the player guessed the correct answer
	won = False

	# Initilize the attempt counter
	attempt = 0

	# Guess loop
	while attempt <= 3:
		attempt += 1 # Increment attempt counter

		# Enter the guess
		while True:
			guess = int(input("Guess an integer between 1 and 50:"))
			if guess < 1 or guess > 50:
				print("Your guess must be between 1 and 50")
			else:
				break
		
		if guess > answer:
			print("Your guess was to high")
		elif guess < answer:
			print("Your guess was to low")
		else:
			# If the guess was not to high, and not to low
			# it has to be right
			won = True

			# Break from the loop
			break
	
	# Check if the player guessed the right number
	if won:
		# Calculate the amount the player won
		amount = math.floor(10 / float(attempt)) * bet
		
		# Add the amount to the new balance of the player
		new_balance += amount

		print("Congratulation! You win " + str(amount) + "$")
	else:
		print("Sorry!! You lost your betting amount, " + str(bet) + "$")
		print("The number was " + str(answer))

	play_again(name, new_balance)

# Ask the player if they want to play again
def play_again(name, balance):
	print()

	# Check if the player is out of money
	if balance == 0:
		print("You are out of money,")
		print("Good bye.")
	# If not, ask them if they would like to play again
	elif input("Would you like to play again? [Y/n] ") == "n":
		print("All right,")
		print("Good bye.")
	# If they do, lets play
	else:
		play_round(name, balance)

main()



