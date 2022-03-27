import itertools
import math
import numpy as np
import matplotlib.pyplot as plt
from os import system, name
import re
import random
import time

def clear(): # Clear the Terminal
    _ = system('cls') if name == 'nt' else system('clear')

list_func = ["Ti","Te","Si","Se","Ni","Ne","Fi","Fe"]
score = [60,40, 20, 55 , 40, 10, 30, 30 ] # Ti, Te, Si, Se, Ni, Ne, Fi, Fe


def main():
    response = ""
    while "C" not in response and "T" not in response:
        response = input("Do you want to enter a code OR do you want to do a test ? [C/T]\n>>>").upper()

    if response == "T": # Test
        score = test()
        analysis(score)
        plot(score)
        code = "".join(map(lambda l: hex(l).zfill(2)[2:4],score))
        print(f"If you want to see your results again, is here your code:\n{code}")

    else:
        code = "" #640a0f4b32051419
        while len(code) != 16:
            code = input("Enter the code:\n>>>")
            if len(code)!=16:
                print("This code isn't valid. Please verify the validity of the code")

        code = re.findall('..',code) # ["01","23","45","67",...]
        code = [*map(lambda e: int(e,16),code)] # Transform strings in Hexa to int
        analysis(code)
        plot(code)

    exit()


def test():
    score = [0]*8
    lang = ""
    while "fr" not in lang and "en" not in lang:
        lang = input("Do you want the test in English or French ? [en/fr]\n>>>").lower()
    if lang == "fr":
        from FR_questions_mbti import question_about_mbti as CF 
    else: 
        from ENG_questions_mbti import question_about_mbti as CF

    clear()
    questions = [*range(80)]
    choi = [["Ti","Te"],["Fi","Fe"],["Si","Se"],["Ni","Ne"]]
    while questions != []:
        n = random.choice(questions)
        asking = True
        while asking:
            asking = False
            print("The sentence is:")
            try:
                print('"'+CF["TFSN"[n//20]][str((1+(n%20//2)))][choi[(n)//20][n%2]]+'"\n')
            except Exception as e:
                print(e,n)
                time.sleep(100)
                

            try:
                note = int(input("Note this sentence from 0 to 10.\n>>>"))
                clear()
                asking = note < 0 or note > 10
                if asking:
                    print(f"The number should be between [0;10], not {note}")
            except ValueError:
                clear()
                print("This isn't a number")
                asking = True
        
        i = 0
        if n > 59:
            i = 4
        if 60 > n > 39:
            i = 2
        if 40 > n > 19:
            i = 6
        i+=n%2
        score[i] += note
        questions.remove(n)

    return score
    
 

def analysis(score):
    """
    
    Analysis a score
    score is [Ti, Te, Si, Se, Ni, Ne, Fi, Fe]
    
    """
    # Creating a New List 
    sort_score = [score[i]for i in range(8)]
    sort_score = sorted(sort_score)

    # Creating a list for Type and score type
    list_type = [
        ["IE"[i // 8] + "NS"[(i // 4) % 2] + "TF"[(i // 2) % 2] + "PJ"[i % 2], 500]
        for i in range(16)
    ]

    score_func = [[list_func[i],score[i]]for i in range(8)]

    # List of "Stack" of function by MBTI Type
    list_typofunc = [ ["Ti","Ne","Si","Fe"], # INTP
                    ["Ni","Te","Fi","Se"], # INTJ
                    ["Fi","Ne","Si","Te"], # INFP
                    ["Ni","Fe","Ti","Se"], # INFJ
                    ["Ti","Se","Ni","Fe"], # ISTP
                    ["Si","Te","Fi","Ne"], # ISTJ
                    ["Fi","Se","Ni","Te"], # ISFP
                    ["Si","Fe","Ti","Ne"], # ISFJ
                    ["Ne","Ti","Fe","Si"], # ENTP
                    ["Te","Ni","Se","Fi"], # ENTJ
                    ["Ne","Fi","Te","Si"], # ENFP
                    ["Fe","Ni","Se","Ti"], # ENFJ
                    ["Se","Ti","Fe","Ni"], # ESTP
                    ["Te","Si","Ne","Fi"], # ESTJ
                    ["Se","Fi","Te","Ni"], # ESFP
                    ["Fe","Si","Ne","Ti"]  # ESFJ
    ]

    # Coefficients of importance
    coef = [2, 1.5, 1.25, 1]
    # Calculates score for every MBTI type due to it's "proximity" with the "i-th" function
    for i, j in itertools.product(range(16), range(4)):
        #  sum(score_func[k][1] for k in range(8) if list_typofunc[i][j] == score_func[k][0]) <=> The score of "j-th" function of the "i-th" MBTI type
        list_type[i][1] -= abs(sort_score[7-j] - sum(score_func[k][1] for k in range(8) if list_typofunc[i][j] == score_func[k][0]))*coef[j]


    # Sorting MBTI type by there score
    final_score = sorted(list_type, key = lambda x: x[1])[::-1]

    # Doing the Sum of exponentiel for probability
    sumExp = sum( math.exp(final_score[i][1]/10) for i in range(16))

    # Probability list
    probability = [str(round(float(100 * math.exp(final_score[i][1]/10)/sumExp),2))+"%" for i in range(16)]

    # Final Print
    print("The Scores are:\n\t- "+"\n\t- ".join(final_score[i][0]+f" : {final_score[i][1]}pts <=> Probability of : {probability[i]}"   for i in range(16)))


def plot(score):
    """
    plot the score
    """
    ################################################################################################################
    #                                  P        L       O       T                                                  #
    ################################################################################################################
    x = np.array(list_func)                                                                                        #
    y = np.array(score)                                                                                            #
                                                                                                                   #
    plt.bar(x,y, color=['#3480eb','#5b97eb','#40b361','#59c979', '#f2d00c','#ffe657', '#c41837','#c9324e'])        #
    plt.show()                                                                                                     #
    ################################################################################################################


if __name__ == "__main__":
    main()
