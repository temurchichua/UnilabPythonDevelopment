import nltk
from nltk.tokenize import sent_tokenize

text1 = """In the light, ride slow to my yellow diamond shining.
Like the Batman logo over Gotham, rock LA to Harlem.
If you say "get 'em Mike G" then I got 'em.
One man squadron, nigga I'm a problem.
From Briggs I got bars and plans to.
Pimp these Polish bitches into pop stars.
Humanity kills, we all suffer from insanity still.
And if I said it then it is or it's gonna be real.
OF 'til I OD and I probably will, uh"""

text2 = """What the fuck is caution?
Often I leave you flossin' and cause exes next to coffins.
Lost in translation, the dreams you chase.
Got you diving for the plates like you stealin' home base.
That's great, I'm home alone dreamin' of two on ones.
With Rihanna and Christina Milian, bring it on.
And Travis is in the closet organizing and hangin' the tramp."""

tokenized_text1 = sent_tokenize(text1)
tokenized_text2 = sent_tokenize(text2)

print("Left Brain:" )


for num, sent in enumerate(tokenized_text1):
    print (f"{num}-{sent}")


print("Mike G: ")

for num, sent in enumerate(tokenized_text2):
    print (f"{num}-{sent}")

print("MC Nino:")

while "OD" in tokenized_text1:
    print(tokenized_text1[5] + tokenized_text1[3] + tokenized_text1[12])
else:
    print(tokenized_text2[4] + tokenized_text2[1] + tokenized_text2[2])