#!/usr/bin/env python3

import nltk
from nltk.corpus import cmudict

cmudict = cmudict.dict()
apple_cmu = cmudict["airplane"][0]

def syllable_count(word_cmu):
    return len(list(y for y in word_cmu if y[-1].isdigit()))

def cmu_to_syllables(word_cmu):
    syllables = []
    for seg in word_cmu:
        print(seg)
        # start new syllable
        if seg[-1].isdigit():
            syllables.append([seg])
        else:
            syllables[-1].append(seg)

    return syllables

print(syllable_count(apple_cmu))
print(cmu_to_syllables(apple_cmu))