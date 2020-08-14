import random
import nltk
from nltk import word_tokenize
from PyLyrics import *


# gathers lyrics for the specified song
def collect_lyrics(song_name, artist_name):
    return nltk.pos_tag(word_tokenize(PyLyrics.getLyrics(artist_name, song_name)))


# selects replacement lyrics of matching POS
def replace_lyrics(part_of_speech):
    better_words = [('golden', 'JJ'), ('enchanted', 'JJ'), ('iron', 'JJ'), ('diamond', 'JJ'), ('wooden', 'JJ'),

                    ('golden', 'JJR'),

                    ('golden', 'JJS'),

                    ('mine', 'NN'), ('cave', 'NN'), ('ore', 'NN'), ('enderman', 'NN'), ('zombie pigman', 'NN'),
                    ('pick', 'NN'), ('creeper', 'NN'), ('base', 'NN'), ('bow', 'NN'),
                    ('diamond', 'NN'), ('iron', 'NN'), ('spider', 'NN'), ('skeleton', 'NN'), ('zombie', 'NN'),
                    ('ender dragon', 'NN'), ('ender portal', 'NN'), ('nether portal', 'NN'), ('dye', 'NN'),

                    ('Steve', 'NNP'), ('Alex', 'NNP'), ('Hero Brine', 'NNP'), ('Notch', 'NNP'),

                    ('Hero Brines', 'NNPS'),

                    ('mines', 'NNS'), ('caves', 'NNS'), ('mobs', 'NNS'), ('ore', 'NNS'), ('endermen', 'NNS'),
                    ('zombie pigmen', 'NNS'), ('mines', 'NNS'), ('caves', 'NNS'), ('creepers', 'NNS'),
                    ('diamonds', 'NNS'), ('iron', 'NNS'), ('spiders', 'NNS'), ('skeletons', 'NNS'), ('zombies', 'NNS'),
                    ('ender portals', 'NNS'), ('nether portals', 'NNS'), ('dyes', 'NNS'),

                    ('mined', 'VBD'), ('dug', 'VBD'), ('crafted', 'VBD'), ('built', 'VBD'), ('brewed', 'VBD'),
                    ('enchanted', 'VBD'), ('farmed', 'VBD'), ('hunted', 'VBD'), ('greifed', 'VBD'), ('smelted', 'VBD'),
                    ('cooked', 'VBD'), ('dyed', 'VBD'),

                    ('mined', 'VBN'), ('dug', 'VBN'), ('crafted', 'VBN'), ('built', 'VBN'), ('brewed', 'VBD'),
                    ('enchanted', 'VBD'), ('farmed', 'VBD'), ('hunted', 'VBD'), ('greifed', 'VBD'), ('smelted', 'VBD'),
                    ('cooked', 'VBD'), ('dyed', 'VBD'),

                    ('mining', 'VBG'), ('digging', 'VBG'), ('crafting', 'VBG'), ('building', 'VBG'), ('brew', 'VBD'),
                    ('enchanting', 'VBD'), ('farming', 'VBD'), ('hunting', 'VBD'), ('greifing', 'VBD'),
                    ('smelting', 'VBD'), ('cooking', 'VBD'), ('dyeing', 'VBD'),
                    ('mine', 'VBG'), ('dig', 'VBG'), ('craft', 'VBG'), ('build', 'VBG'), ('brewing', 'VBD'),
                    ('enchant', 'VBD'), ('farm', 'VBD'), ('hunt', 'VBD'), ('greif', 'VBD'), ('smelt', 'VBD'),
                    ('cook', 'VBD'), ('dye', 'VBD'),]

    random.shuffle(better_words)

    for i in range(len(better_words)):
        if better_words[i][1] == part_of_speech[1]:
            return better_words[i][0]
    return part_of_speech[0]


def frequency(word):
    fdist1 = nltk.FreqDist(word)
    return fdist1.most_common(10)


# randomly selects lyrics to be replaced
def process_lyrics(lyrics):
    fq = frequency(lyrics)
    dictionary = {}

    for i in range(len(fq)):
        temp1 = fq[i][0][1]
        if temp1 == "JJ" or temp1 == "NNP" or temp1 == "NN" or temp1 == "NNS" or temp1 == "VBG":
            if len(dictionary) < 4:
                dictionary[fq[i][0]] = replace_lyrics(fq[i][0])

    for i in range(len(lyrics)):
        if type(lyrics[i]) == tuple:
            check = random.getrandbits(3)
            if check > 4:
                temp = lyrics[i]
                if temp not in dictionary.keys():
                    dictionary[temp] = replace_lyrics(lyrics[i])
                    lyrics[i] = dictionary[temp]
                else:
                    lyrics[i] = dictionary[temp]
            else:
                temp2 = lyrics[i]
                if temp2 not in dictionary.keys():
                    dictionary[temp2] = lyrics[i][0]
                    lyrics[i] = dictionary[temp2]
                else:
                    lyrics[i] = dictionary[temp2]
    lyrics = [' '.join(lyrics)]
    lyrics = lyrics[0].replace(" \'", "\'")
    lyrics = lyrics.replace(" ,", ",")
    return lyrics


"""
song = input("Enter the song:\n")

artist = input("Enter the artist:\n")
"""


song = "back in black"

artist = "acdc"

print(process_lyrics(collect_lyrics(song, artist)))
