from numpy import *
import numpy as np
import random2
from array import *
import os
## to run the loop

class Daughter(object):
    def take_input(self):
        h = input('What is your name?')
        g = int(input('Enter the number of character you want to be in your baby name.'))
        f = input("Enter your spouse name.")
        #print("Among one thousand names, Possible baby names are")
        first_let = h[0]
        let_anywhere = f[0]

        #print(h,g)
        # Characters to generate the random word
        rest_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']
        i = 0
        while i < 10001:
            i = i + 1

            #List to carry the character
            my_char = []
            my_char_len = len(my_char)
            # List to carry the word after joining them
            word = []
            while my_char_len < g:
                my_char_len = my_char_len + 1
                pull = random2.choice(rest_char)
                my_char.append(pull)
            #print(my_char)
            # use of join built-in function to join the character in the my_char list and make a single word
            name = ("".join(my_char))
            word.append(name)
                #print('No name with letter',first_let)
            # print(word)
            # To create the file if not created and to apend the data in the file
            f1 = open("names.txt",'a+')
            if name[0] == first_let:
                f1.write("\n"+name)
                f1.close()
            else:
                pass

            # to read the data from the file
            f2 = open("names.txt",'r')
            content = f2.read()
        print(len(content))
            #return content
        print('These are the possible baby names.',content.upper())
        os.remove("names.txt")



x = Daughter()
x.take_input()
