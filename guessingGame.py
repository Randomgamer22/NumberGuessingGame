import random


randomNumber = random.randint(1, 9)
actualNumber = random.randint(1, randomNumber)
print("Random Number Game")

while True:
	answer = int(input("Guess a number between 1 and 9: "))
	turns = 0

	if answer != randomNumber:
		if randomNumber > answer:
			print("Wrong number: Enter a number above:", answer)
			turns += 1
		if randomNumber < answer:
			print("Wrong number: Enter a number below:", answer)
			turns += 1

	if turns == 5:
		print("Sorry your turns are over")
		break

	if answer == randomNumber:
		print("Correct answer")
		break
