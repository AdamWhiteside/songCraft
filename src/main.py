import random
import nltk
from nltk import word_tokenize
from PyLyrics import *
from tkinter import *


def speak():
    pass


# gathers lyrics for the specified song
def collect_lyrics(song_name, artist_name):
    return nltk.pos_tag(word_tokenize(PyLyrics.getLyrics(artist_name, song_name)))


# selects replacement lyrics of matching POS
def replace_lyrics(part_of_speech):
    better_words = [('gold', 'JJ'), ('enchanted', 'JJ'), ('iron', 'JJ'), ('diamond', 'JJ'), ('wooden', 'JJ'),

                    ('mine', 'NN'), ('cave', 'NN'), ('ore', 'NN'), ('enderman', 'NN'), ('zombie pigman', 'NN'),
                    ('pick', 'NN'), ('creeper', 'NN'), ('base', 'NN'), ('bow', 'NN'),
                    ('diamond', 'NN'), ('iron', 'NN'), ('spider', 'NN'), ('skeleton', 'NN'), ('zombie', 'NN'),
                    ('ender dragon', 'NN'), ('ender portal', 'NN'), ('nether portal', 'NN'), ('dye', 'NN'),

                    ('Steve', 'NNP'), ('Alex', 'NNP'), ('Hero Brine', 'NNP'), ('Notch', 'NNP'), ('Minecraft', 'NNP'),

                    #('Hero Brines', 'NNPS'),

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
                    ]

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
            if len(dictionary) < 4 and len(fq[i][0][0]) > 2:
                dictionary[fq[i][0]] = replace_lyrics(fq[i][0])

    for i in range(len(lyrics)):
        if type(lyrics[i]) == tuple:
            check = random.getrandbits(3)
            if check > 4 and len(lyrics[i][0]) > 2:
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


main = Tk()
main.title("songCraft")

#main.geometry("400x400")
#GUIFrame = Frame(main)


v1 = StringVar()
v2 = StringVar()
text = StringVar()
text.set(" ")

l1 = Label(main, text="Enter Song Title", justify=CENTER)
l2 = Label(main, text="Enter Artist Name", justify=CENTER)
e1 = Entry(main, textvariable=v1, justify=CENTER)
e2 = Entry(main, textvariable=v2, justify=CENTER)
l3 = Label(main, textvariable=text, justify=CENTER, wraplength=300)


def onclick():
    song = v1.get()
    artist = v2.get()
    #song = "back in black"
    #artist = "acdc"
    text.set(process_lyrics(collect_lyrics(song, artist)))


b1 = Button(main, text="Remix", command=onclick, justify=CENTER)


r1 = l1.pack(padx=5, pady=5, side=TOP)
r2 = e1.pack(padx=5, pady=5, side=TOP)
r1 = l2.pack(padx=5, pady=5, side=TOP)
r2 = e2.pack(padx=5, pady=5, side=TOP)
r4 = l3.pack(padx=5, pady=5, side=BOTTOM)
r3 = b1.pack(padx=5, pady=5, side=BOTTOM)



main.mainloop()


"""
song = input("Enter the song:\n")

artist = input("Enter the artist:\n")


song = "back in black"

artist = "acdc"

songText = (process_lyrics(collect_lyrics(song, artist)))
"""