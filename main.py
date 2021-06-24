import pikepdf
from tqdm import tqdm
from itertools import product
import string
from datetime import datetime
from datetime import date
import smtplib, ssl


def time(): # function return current time and date. We will need this later to see when current index is done.
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    today = date.today()
    d = today.strftime("%d/%m/%Y")
    return f"{current_time}; {d}"


def password_generator(index):
    password_ab = set() # set where we collect all options with specifyed first two letters (for one index 14 million combinations)

    all = string.ascii_letters + string.digits
    keywords1 = [a + b for a, b in product(all, repeat=2)] # all combinations for first two letters ( with index we specify which we will use later in pikepdf.open)
    keywords2 = {a + b + c + d for a, b, c, d in product(all, repeat=4)} # all combinations for other 4 letters
    for i in keywords2: #here we generate passwords with specify index
        pass_w = keywords1[index] + i
        password_ab.add(pass_w)

    passwords = {line.strip() for line in password_ab} #preperation for to use set() later in function

    file = open("status.txt", "a", encoding="utf-8") # wre create a file that collect data of our process
    for password in tqdm(passwords, "lock.pdf"): #specify file name
        try:
            # open PDF file
            with pikepdf.open("lock.pdf", password=password) as pdf: #we are using pikepdf libery to chack our password
                # Password decrypted successfully, break out of the loop
                print("[+] Password found:", password)  #password found printed
                file.write(f"At {time()} i found password \npassword is: {password}\n\n")
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as server:
                    server.login("[***]", "[***]") #you need to use your own credentials that program send you message about password
                    server.sendmail("[***]", "[***]", password) # first specify your email and then to where your password should be send
                break
        except pikepdf._qpdf.PasswordError as e:
            # wrong password, just continue in the loop
            continue
    file.write(f"    password generator:({index}); first two letters: ---{keywords1[index]}--- chacked at  {time()}\n") #status update; that you know which combinations computer already chacked


