import pikepdf
from tqdm import tqdm
from itertools import product
import string
from datetime import datetime
from datetime import date
import smtplib, ssl


def time(): # function print current time and date. We will need this later to see when current index is done.
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    today = date.today()
    d = today.strftime("%d/%m/%Y")
    return f"{current_time}; {d}"


def password_generator(index):
    password_ab = set() # set where we collect all options with specifyed first two letters (for one index 14 million combinations)

    all = string.ascii_letters + string.digits
    keywords1 = [a + b for a, b in product(all, repeat=2)] # all combinations for first tvo letters ( with index we specify which we eill use)
    keywords2 = {a + b + c + d for a, b, c, d in product(all, repeat=4)} # all combinations for other 4 letters

    for i in keywords2: #here we generate passwords with specify index
        pass_w = keywords1[index] + i
        password_ab.add(pass_w)

    passwords = {line.strip() for line in password_ab} #preperation for to use set() later in function

    file = open("status.txt", "a", encoding="utf-8") # wre create a file that collect data of our process
    for password in tqdm(passwords, "unlock.pdf"): #specify file name
        try:
            # open PDF file
            with pikepdf.open("unlock.pdf", password=password) as pdf: #we are using pikepdf libery to chack our password
                # Password decrypted successfully, break out of the loop
                print("[+] Password found:", password)  #password found print
                file.write(f"At {time()} i found password \npassword is: {password}\n\n")
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as server:
                    server.login("[***]", "[***]") #jou neef to use your oun credentials that program send you message abouth password
                    server.sendmail("[***]", "[***]", password) # first specify jour email and then to where your password should be send
                break
        except pikepdf._qpdf.PasswordError as e:
            # wrong password, just continue in the loop
            continue
    file.write(f"    password generator:({index}); first two letters: ---{keywords1[index]}--- chacked at  {time()}\n") #status update; that you know which kombinations computer already chacked



def variant1(): #this function call password_generator(index); read which combination of first two letters is next
    file = open("number1.txt", "r", encoding="utf-8").readlines() #open file that alerady exist in system in the same folder
    index = [x for x in file][0] #read first row (index)
    while index != 1000: #specify highest index for this spacific .py... this loop whrite where we are and add =+ 1 to index
        file = open("number1.txt", "w", encoding="utf-8") #here we rewrite the same file that we open (in case of closing program that when we start it agail he "knows" where he finished)
        file.write(f"{index}")
        file.close()
        index = int(index) # transfer str to int
        password_generator(index) #call previous function
        index = int(index) + 1 # add index += 1
