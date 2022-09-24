import random
name = "Joe"
question = "Is this real life?"

list = ("Yes - definitely.", "It is decidedly so.", "Without a doubt.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "My sources say no.", "Outlook not so good.", "Very doubtful.")

answer = random.choice(list)
print(name, " asks: ", question)
print("Magic 8-Ball’s answer: ", answer)
