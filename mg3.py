import pikepdf
from tqdm import tqdm
from itertools import product
import string
from datetime import datetime
from datetime import date
import smtplib, ssl

from main import time
from main import password_generator

def variant3(): #this function call password_generator(index); read which combination of first two letters is next
    file = open("number3.txt", "r", encoding="utf-8").readlines() #open file that alerady exist in system in the same folder
    index = [x for x in file][0] #read first row (index)
    while index != 3000: #specify highest index for this spacific .py... this loop whrite where we are and add =+ 1 to index
        file = open("number3.txt", "w", encoding="utf-8") #here we rewrite the same file that we open (in case of closing program that when we start it agail he "knows" where he finished)
        file.write(f"{index}")
        file.close()
        index = int(index) # transfer str to int
        password_generator(index) #call previous function
        index = int(index) + 1 # add index += 1





