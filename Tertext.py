import sys
from termcolor import colored
import random

# Color
if sys.platform == "linux" or sys.platform == "linux2":
    BB = "\033[34;1m"  # Blue Light
    YY = "\033[33;1m"  # Yellow Light
    GG = "\033[32;1m"  # Green Light
    WW = "\033[0;1m"   # White Light
    RR = "\033[31;1m"  # Red Light
    CC = "\033[36;1m"  # Cyan Light
    MM = "\033[35;1m"  # Magenta Light
    B = "\033[34;1m"   # Blue
    Y = "\033[33;1m"   # Yellow
    G = "\033[32;1m"   # Green
    W = "\033[0;1m"    # White
    R = "\033[31;1m"   # Red
    C = "\033[36;1m"   # Cyan
    M = "\033[35;1m"   # Magenta

    # Random Color
    rand = (BB, YY, GG, RR, CC)
    P = random.choice(rand)

def is_word_possible(word, letters):
    word_chars = list(word)
    for char in word_chars:
        if word_chars.count(char) > letters.count(char):
            return False
    return True

def find_possible_words(letters, wordlist):
    possible_words = []
    for word in wordlist:
        if len(word) >= 3 and is_word_possible(word, letters):
            possible_words.append(word)
    return possible_words

def main():

    # Tertext Banner
    print(f"\n{P} #######{YY} ##################{P} #######{YY} ####################")
    print(f"{P}    #    ###### #####          #    ###### #    # #####")
    print(f"{P}    #    #      #    #         #    #       #  #    #")
    print(f"{P}    #    ###### #    #  ##     #    #####    ##     #")
    print(f"{P}    #    #      #####          #    #        ##     #")
    print(f"{P}    #    #      #   #          #    #       #  #    #")
    print(f"{P}    #    ###### #    #         #    ###### #    #   #")
    print(f"{YY}####################[{GG} TheDarkRoot{YY} ]####################\n")
    print(f"{GG}0{WW}{{======================{GG} INFO {WW}=======================}}0")
    print(f"{GG}|{YY} [{CC}={YY}]{WW} Name     {CC}:{WW} Tertext{GG}                              |")
    print(f"{GG}|{YY} [{CC}={YY}]{WW} Code     {CC}:{WW} Python{GG}                               |")
    print(f"{GG}|{YY} [{CC}={YY}]{WW} Version  {CC}:{WW} v1.0.0 (Alpha){GG}                       |")
    print(f"{GG}|{YY} [{CC}={YY}]{WW} Author   {CC}:{WW} TheDarkRoot{GG}                          |")
    print(f"{GG}|{YY} [{CC}={YY}]{WW} Email    {CC}:{WW} 7H3D4RKR007@gmail.com{GG}                |")
    print(f"{GG}|{YY} [{CC}={YY}]{WW} Github   {CC}:{WW} https://github.com/TheDarkRoot{GG}       |")
    print(f"{GG}|{YY} [{CC}={YY}]{WW} Telegram {CC}:{WW} @TheDarkRoot (t.me/TheDarkRoot){GG}      |")
    print(f"{GG}|{YY} [{CC}={YY}]{WW} Team     {CC}:{WW} TurkHackTeam (www.turkhackteam.org){GG}  |")
    print(f"{GG}0{WW}{{===================================================}}0\n")

    while True:
        letters = input(CC+" Harfleri Girin:~# "+GG).lower()
        
        print()  # Bir satır boşluk bırakma
        
        if letters == 'q':
            print(RR+" Çıkış Yapılıyor\n")
            break
        
        if not letters:
            print(YY+" Hata: Lütfen harf girişi yapın.\n")
            continue
        
        with open("wordlist.txt", "r") as file:
            wordlist = [line.strip() for line in file]
        
        possible_words = find_possible_words(letters, wordlist)
        
        sorted_words = sorted(possible_words, key=len, reverse=True)
        
        max_word_length = max(len(word) for word in sorted_words)
        
        for i, word in enumerate(sorted_words, start=1):
            print(CC+f"{i: 03d}{RR}:{GG} {word.capitalize():{max_word_length}}")
        
        print()  # Bir satır boşluk bırakma

if __name__ == "__main__":
    main()
