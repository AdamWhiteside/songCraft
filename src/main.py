import random
import nltk
from nltk import word_tokenize
from PyLyrics import *


# gathers lyrics for the specified song
def collect_lyrics(song_name, artist_name):
    return PyLyrics.getLyrics(artist_name, song_name)


# selects replacement lyrics of matching POS
def replace_lyrics(part_of_speech):
    better_words = [('golden', 'JJ'), ('enchanted', 'JJ'), ('iron', 'JJ'), ('diamond', 'JJ'), ('wooden', 'JJ'),
                    ('mine', 'NN'), ('cave', 'NN'), ('ore', 'NN'), ('enderman', 'NN'), ('zombie pigman', 'NN'),
                    ('pick', 'NN'), ('creeper', 'NN'), ('building', 'NN'), ('base', 'NN'), ('bow', 'NN'),
                    ('diamond', 'NN'), ('iron', 'NN'), ('spider', 'NN'), ('skeleton', 'NN'), ('zombie', 'NN'),
                    ('ender dragon', 'NN'), ('mobs', 'NNS'), ('ore', 'NNS'), ('endermen', 'NNS'),
                    ('zombie pigmen', 'NNS'), ('mines', 'NNS'), ('caves', 'NNS'),
                    ('creepers', 'NNS'), ('diamonds', 'NNS'), ('iron', 'NNS'), ('spider', 'NNS'), ('skeleton', 'NNS'),
                    ('zombie', 'NNS'), ('mining', 'VBG'), ('digging', 'VBG'), ('crafting', 'VBG')]

    random.shuffle(better_words)

    for i in range(len(better_words)):
        if better_words[i][1] == part_of_speech[1]:
            return better_words[i][0]
    return part_of_speech[0]


# randomly selects lyrics to be replaced
def process_lyrics(better_words):
    text = word_tokenize(better_words)
    lyrics = nltk.pos_tag(text)
    dictionary = {}

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
                temp1 = lyrics[i]
                if temp1 not in dictionary.keys():
                    lyrics[i] = lyrics[i][0]
                else:
                    lyrics[i] = dictionary[temp1]
    lyrics = [' '.join(lyrics)]
    return lyrics


song = input("Enter the song:\n")

artist = input("Enter the artist:\n")

print(process_lyrics(collect_lyrics(song, artist)))
