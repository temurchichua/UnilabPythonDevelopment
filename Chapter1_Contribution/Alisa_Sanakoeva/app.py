from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

text = """
"Excuse me" the ant said, "what is this for?".

"What is what for" I said.

"This great black and white expanse I'm standing on now." It tapped the book with a little black leg.

"Look, you wouldn't understand even if I explained it to you."

"That might be so" the ant said,
"But though I am very small, I am also very curious and I don't want to turn to dust having known nothing at all.
So if you would, please, what is this for?"

"""

sent_tokens = sent_tokenize(text)

print("Tokenized sentences of the text:")
for num, sent in enumerate(sent_tokens):
    print(f'{num}. {sent}')

sentence_num = int(input("Enter the number of the sentence you want to tokenize:\n>>> "))
word_tokens = word_tokenize(sent_tokens[sentence_num])

print(f"tokens of the sentence '{sent_tokens[sentence_num]}': ")

for num, word in enumerate(word_tokens, 1):
    print (f'{num}. {word}')

answer = input("Would you like to see a frequency distribution graph?\n>>> ")

if answer.lower() == "yes":
    num = int(input("Top how many tokens?\n>>> "))
    fdist = FreqDist(word_tokenize(text))
    fdist.plot(num)
    print("There you go")
    plt.show()
elif answer.lower() == "no":
    print("Okay then,")
else:
    print("It was a yes or no question.")


print("Good luck with being a thing in the world.")