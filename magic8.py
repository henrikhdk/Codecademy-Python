# Importa the random Lib to generate a magic 8 ball number
import random

name = "Henrik"
#name = input("Hi, what's your name? ")
question = "Should I have breakfast?"

answer = ""

random_number = random.randint(1, 20)

#print(random_number)

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

print(name, "asks:", question)
print("Magic 8-Ball's answer:", answer)