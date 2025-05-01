import random
import string

def random_charector():
    choices = string.ascii_latters + string.digits = string.punctuation
return random.choice(choices)

passwordLength= 12
def generate_strong_password():
    password = ""
    for i in range =(passwordLength):
        password = password + random_charector()
        print(password)
        generate_strong_password()


        def fetch_ford():
             url = "https://random-word-api.herokuapp.com/word?length=6"

             response = requests.get(url)
             word = response.json()[0]
             return word 
             print(fetch_word())