
import string
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from nltk.stem.wordnet import WordNetLemmatizer
lem = WordNetLemmatizer()
text="""" On May 29, 2020, a family of sunspots — dark spots that freckle the face of the Sun, representing areas of complex magnetic fields — sported the biggest solar flare since October 2017. Although the sunspots are not yet visible (they will soon rotate into view over the left limb of the Sun), NASA spacecraft spotted the flares high above them.

The flares were too weak to pass the threshold at which NOAA's Space Weather Prediction Center (which is the U.S. government's official source for space weather forecasts, watches, warnings and alerts) provides alerts. But after several months of very few sunspots and little solar activity, scientists and space weather forecasters are keeping their eye on this new cluster to see whether they grow or quickly disappear. The sunspots may well be harbingers of the Sun's solar cycle ramping up and becoming more active. 
As the Sun moves through its natural 11-year cycle, in which its activity rises and falls, sunspots rise and fall in number, too. NASA and NOAA track sunspots in order to determine, and predict, the progress of the solar cycle — and ultimately, solar activity. Currently, scientists are paying close attention to the sunspot number as it's key to determining the dates of solar minimum, which is the official start of Solar Cycle 25. This new sunspot activity could be a sign that the Sun is possibly revving up to the new cycle and has passed through minimum. 

However, it takes at least six months of solar observations and sunspot-counting after a minimum to know when it's occurred. Because that minimum is defined by the lowest number of sunspots in a cycle, scientists need to see the numbers consistently rising before they can determine when exactly they were at the bottom. That means solar minimum is an instance only recognizable in hindsight: It could take six to 12 months after the fact to confirm when minimum has actually passed. 

This is partly because our star is extremely variable. Just because the sunspot numbers go up or down in a given month doesn't mean it won't reverse course the next month, only to go back again the month after that. So, scientists need long-term data to build a picture of the Sun’s overall trends through the solar cycle. Commonly, that means the number we use to compare any given month is the average sunspot number from six months both backward and forward in time — meaning that right now, we can confidently characterize what October 2019 looks like compared to the months before it (there were definitely fewer sunspots!), but not yet what November looks like compared to that.

On May 29, at 3:24 a.m. EST, a relatively small M-class solar flare blazed from these sunspots. Solar flares are powerful bursts of radiation. Harmful radiation from a flare cannot pass through Earth's atmosphere to physically affect humans on the ground, however — when intense enough — they can disturb the atmosphere in the layer where GPS and communications signals travel. The intensity of this flare was below the threshold that could affect geomagnetic space and below the threshold for NOAA to create an alert.

Nonetheless, it was the first M-class flare since October 2017 — and scientists will be watching to see if the Sun is indeed beginning to wake up.

"""


def text_process(mess):
    """
    1. remove punc
    2. remove stop words
    3. return list of clean text words
    """

    nopunc = ''.join([char for char in mess if char not in string.punctuation])
    lem_words = []
    for word in word_tokenize(nopunc):
        lem_words.append(lem.lemmatize(word))

    return [word for word in lem_words if word not in stopwords.words('english')]


clean_text = text_process(text)
word_freq = FreqDist(clean_text)

word_freq.plot(10, title='Top 10 Most common Words in Text')
plt.show()

