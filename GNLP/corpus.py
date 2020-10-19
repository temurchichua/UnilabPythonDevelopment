#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import string
import re
from logger import log
import pprint
# usage of counters : https://docs.python.org/2/library/collections.html
from collections import Counter
import pickle
from ftfy import fix_encoding

import copy
# emit a warning to the puny Humans
log.info('Welcome to the Georgian NLP toolset demo')

printable = set(string.printable)


def not_printable(word):
    """
    Checks if the string contains the printable symbols
    :param word:
    :return True or False:
    """
    for char in word:
        if char in printable:
            return False
    return True


def sizeof_fmt(file_size, suffix='B'):
    """
    Returns the Human Readable file volume unit from num
    :param suffix: default
    :param file_size: file size in integer
    :return:
    ref: https://stackoverflow.com/questions/1094841/reusable-library-to-get-human-readable-version-of-file-size
    """
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(file_size) < 1024.0:
            return "%3.1f%s%s" % (file_size, unit, suffix)
        file_size /= 1024.0
    return "%.1f%s%s" % (file_size, 'Yi', suffix)


class Corpus():
    def __init__(self, stop_words='stops.txt'):

        self.stop_words = set(line.strip() for line in open('stops.txt', encoding='utf-8'))
        self.sequence = []
        self.prepro_sequence = []
        self.tokens = []
        self.counted = {}

    def __repr__(self):
        dictionary = self.__dict__
        try:
            for e in ['stop_words', 'sequence', 'prepro_sequence', 'tokens', 'counted']:
                dictionary[e] = len(dictionary.get(e))
        except Exception as error:
            log.error(error)
        else:
            return pprint.pformat(dictionary, indent=4)

    @classmethod
    def from_file(cls, file_name):
        """collects all improtant data about file from file name and stores in attribute
        !!!needs to be separated in it's own class!!!"""
        cls.file_name = file_name
        cls.basedir = os.path.abspath(os.path.dirname(file_name))
        cls.path = os.path.join(cls.basedir, cls.file_name)
        cls.status = os.stat(cls.path)
        cls.file_size = sizeof_fmt(cls.status.st_size)
        return cls()

    def preprocess_text(self, text):
        """preprocess text for NLP tasks"""
        # Remove all the special characters
        text = re.sub(r'\W', ' ', str(text))
        # remove all single characters
        text = re.sub(r'\s+[a-zA-Z]\s+', ' ', text)
        # Remove single characters from the start
        text = re.sub(r'\^[a-zA-Z]\s+', ' ', text)
        # Substituting multiple spaces with single space
        text = re.sub(r'\s+', ' ', text, flags=re.I)
        # Removing prefixed 'b'
        text = re.sub(r'^b\s+', '', text)
        # Converting to Lowercase
        text = text.lower()
        # Lemmatization - missing
        tokens = text.split()
        # tokens = [ilem(word) for word in tokens]
        tokens = [word for word in tokens if not_printable(word)]
        tokens = [word for word in tokens if word not in self.stop_words]
        tokens = [word for word in tokens if len(word) > 3]

        self.tokens.extend(tokens)

        preprocessed_text = ' '.join(tokens)

        return preprocessed_text

    def file2sequence(self, preprocess=False):
        """"creates sequence of sentences from the file
        :if parameter preprocess = True:
        """
        try:
            log.info(f'ვიწყებ {self.file_name}-ის დამუშავებას')
        except Exception as e:
            log.error(
                'გთხოვთ file2seq მეთოდის გამოყენებამდე ობიექტში დაამატოთ სამუშაო ფაილი ობიექტზე from_file(<path>) მეთოდის გამოყენებით')

        try:
            with open(self.path, mode='r', encoding='utf-8') as text_file:
                for n, line in enumerate(text_file):
                    line = line.strip('\n')
                    self.sequence.append(line)

                text_file.close()
        finally:
            log.info(f'წინადადების რაოდენობა: {len(self.sequence)}')


        if preprocess:
            self.preprocess_sequence()


    def preprocess_sequence(self):
        """
        creates preprocessed copy of sequence stored in object using preprocess_text() method
        """
        for element in self.sequence:
            self.prepro_sequence.append(self.preprocess_text(element))

    def count_tokens(self):
        """counts occurrence of current word in whole corpus"""
        self.counted = Counter(self.tokens)

    def save_corpus(self, name='corpus'):
        data = copy.deepcopy(self)
        del data.stop_words
        with open(f'{name}.pickle', 'wb') as destination_file:
            # Step 3
            pickle.dump(data, destination_file, protocol=pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def load_corpus(name='corpus'):
        # Step 2
        with open(f'{name}.pickle', 'rb') as file_location:
            corp = pickle.load(file_location)
            return corp

    def edits1(self, word):
        "All edits that are one edit away from `word`."
        letters = 'აბგდევზთიკლმნოპჟრსტუფქღყშჩძწხჯჰ'
        splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        deletes = [L + R[1:] for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
        replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
        inserts = [L + c + R for L, R in splits for c in letters]
        return set(deletes + transposes + replaces + inserts)

    def known(self, words):
        """The subset of `words` that appear in the dictionary of counted words."""
        return set(w for w in words if w in self.counted)

    def edits2(self, word):
        """All edits that are two edits away from `word`."""
        return (e2 for e1 in self.edits1(word) for e2 in self.edits1(e1))

    def candidates(self, word):
        """Generate possible spelling corrections for word."""
        return self.known([word]) or self.known(self.edits1(word)) or self.known(self.edits2(word)) or [word]

    def probability(self, word):
        """Probability of `word`."""
        total = sum(self.counted.values())
        return self.counted[word] / total

    def correction(self, word):
        "Most probable spelling correction for word."
        return max(self.candidates(word), key=self.probability)

    def edit_candidates(self, word, assume_wrong=False, fast=True):
        """
        Generate possible spelling corrections for word.
        """

        if fast:
            ttt = self.known(self.edits1(word)) or {word}
        else:
            ttt = self.known(self.edits1(word)) or self.known(self.edits2(word)) or {word}

        ttt = self.known([word]) | ttt
        return list(ttt)

corp = Corpus()
corp.from_file("sample.txt")
corp.file2sequence(preprocess=True)
corp.count_tokens()

print(corp.correction("თბილასი"))
print(corp.edit_candidates("თბილასი"))
