# Generating a random number Lib to generate a Magic 8 Ball number
import random

# Ask the user a name and the question
name = input("What's your name? ")
question = input("Type your question get answer: ")
print("")

answer = ""

# Pseudorandom number generator (PRNG) from a range of 1-20
random_number = random.randint(1, 20)

# 10 affirmative answers
if random_number == 1:
  answer = "It is Certain."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Yes definitely."
elif random_number == 5:
  answer = "You may rely on it."
elif random_number == 6:
  answer = "As I see it, yes."
elif random_number == 7:
  answer = "Most likely."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
    answer = "Yes."
elif random_number == 10:
    answer = "Signs point to yes."

# 5 non-committal answers
elif random_number == 11:
    answer = "Reply hazy, try again."
elif random_number == 12:
    answer = "Ask again later."
elif random_number == 13:
    answer = "Better not tell you now."
elif random_number == 14:
    answer = "Cannot predict now."
elif random_number == 15:
    answer = "Concentrate and ask again."

# 5 negative answers
elif random_number == 16:
    answer = "Don't count on it."
elif random_number == 17:
    answer = "My reply is no."
elif random_number == 18:
    answer = "My sources say no."
elif random_number == 19:
    answer = "Outlook not so good."
elif random_number == 20:
    answer = "Very doubtful."
else:
  answer = "Error"

# Error handling in case of string from question and name is empty
if question == "":
  print("Hey! Ask me a question or I will not speak your future.")
else:
  if name == "":
    print("Question:", question)
  else:
    print(name, "asks:", question)
  print("Magic 8-Ball's answer:", answer)