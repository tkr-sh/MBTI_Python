from questions_mbti import question_about_mbti as FC # FC <=> Fonctions Cognitives 
import random
from os import system, name
import matplotlib.pyplot as plt
import numpy as np
import sys 



######################################################################################################
#     __  __  _  __  ___   __ __ _  __    __  ___   ___ _  _ __  _  ________ _  __  __  _  __        #
#    /  \|  \| |/  \| \ `v' /' _| /' _/  /__\| __| | __| || |  \| |/ _|_   _| |/__\|  \| /' _/       #
#   | /\ | | ' | /\ | |`. .'`._`| `._`. | \/ | _|  | _|| \/ | | ' | \__ | | | | \/ | | ' `._`.       #
#   |_||_|_|\__|_||_|___!_! |___|_|___/  \__/|_|   |_|  \__/|_|\__|\__/ |_| |_|\__/|_|\__|___/       #
######################################################################################################
def analysis(TI,TE,NI,NE,SI,SE,FI,FE):
    list_str_FUNC = ["Ti", "Te", "Ni", "Ne","Si", "Se", "Fi", "Fe"]
    list_FUNC = [TI,TE,NI,NE,SI,SE,FI,FE]

    MAX_FUNC = max(list_FUNC)
    MIN_FUNC = min(list_FUNC)
    def calcul_of_points(dom, aux, ter, inf, MAX, MIN):
        points = 100
        coef_dom = 2.25
        coef_aux = 5/3
        coef_ter = 4/3
        coef_inf = 1
        points -= (MAX - dom)*coef_dom
        # CALCULS AVEC DOM COMME REF
        """
        if aux > (1 - 0.2*(dom-MIN)/dom)*(dom):
            points -= abs((aux - (1 - 0.2*(dom-MIN)/dom)*dom)*coef_aux)
        elif aux < (1 - 0.3*(dom-MIN)/dom)*dom:
            points -= abs(((1 - 0.3*(dom-MIN)/dom)*dom - aux)*coef_aux)
        if ter > (1 - 0.45*(dom -MIN)/dom)*dom:
            points -= abs((ter -(1 - 0.45*(dom -MIN)/dom)*dom)*coef_ter)
        elif ter < (1 - 0.55*(dom -MIN)/dom)*dom:
            points -= abs(((1 - 0.55*(dom -MIN)/dom)*dom - ter)*coef_ter)
        if inf > (1 - 0.65*(dom -MIN)/dom)*dom:
            points -= abs((inf- (1 - 0.65*(dom -MIN)/dom)*dom)*coef_inf)
        elif inf < (1 - 0.75*(dom -MIN)/dom)*dom:
            points -= abs(((1 - 0.75*(dom -MIN)/dom)*dom - inf)*coef_inf)
        points +=300
        points /= 4
        return round(points,2)       
        """
        #CALCULS AVEC MAX COMME REF
        if aux > (1 - 0.2*(MAX-MIN)/MAX)*(MAX):
            points -= abs((aux - (1 - 0.2*(MAX-MIN)/MAX)*MAX)*coef_aux)
        elif aux < (1 - 0.3*(MAX-MIN)/MAX)*MAX:
            points -= abs(((1 - 0.3*(MAX-MIN)/MAX)*MAX - aux)*coef_aux)
        if ter > (1 - 0.45*(MAX -MIN)/MAX)*MAX:
            points -= abs((ter -(1 - 0.45*(MAX -MIN)/MAX)*MAX)*coef_ter)
        elif ter < (1 - 0.55*(MAX -MIN)/MAX)*MAX:
            points -= abs(((1 - 0.55*(MAX -MIN)/MAX)*MAX - ter)*coef_ter)
        if inf > (1 - 0.65*(MAX -MIN)/MAX)*MAX:
            points -= abs((inf- (1 - 0.65*(MAX -MIN)/MAX)*MAX)*coef_inf)
        elif inf < (1 - 0.75*(MAX -MIN)/MAX)*MAX:
            points -= abs(((1 - 0.75*(MAX -MIN)/MAX)*MAX - inf)*coef_inf)
        points +=300
        points /= 4
        return round(points,2)
    pINTP = calcul_of_points(TI,NE,SI,FE,MAX_FUNC,MIN_FUNC)
    pENTP = calcul_of_points(NE,TI,FE,SI,MAX_FUNC,MIN_FUNC)
    pINTJ = calcul_of_points(NI,TE,FI,SE,MAX_FUNC,MIN_FUNC)
    pENTJ = calcul_of_points(TE,NI,SE,FI,MAX_FUNC,MIN_FUNC)
    pISTP = calcul_of_points(TI,SE,NI,FE,MAX_FUNC,MIN_FUNC)
    pESTP = calcul_of_points(SE,TI,FE,NI,MAX_FUNC,MIN_FUNC)
    pISTJ = calcul_of_points(SI,TE,FI,NE,MAX_FUNC,MIN_FUNC)
    pESTJ = calcul_of_points(TE,SI,NE,FI,MAX_FUNC,MIN_FUNC)
    pINFP = calcul_of_points(FI,NE,SI,TE,MAX_FUNC,MIN_FUNC)
    pENFP = calcul_of_points(NE,FI,TE,SI,MAX_FUNC,MIN_FUNC)
    pINFJ = calcul_of_points(NI,FE,TI,SE,MAX_FUNC,MIN_FUNC)   
    pENFJ = calcul_of_points(FE,NI,SE,TI,MAX_FUNC,MIN_FUNC)
    pISFP = calcul_of_points(FI,SE,NI,TE,MAX_FUNC,MIN_FUNC)
    pESFP = calcul_of_points(SE,FI,TE,NI,MAX_FUNC,MIN_FUNC)
    pISFJ = calcul_of_points(SI,FE,TI,NE,MAX_FUNC,MIN_FUNC)
    pESFJ = calcul_of_points(FE,SI,NE,TI,MAX_FUNC,MIN_FUNC)
    all_points = [pINTP, pINTJ, pENTP, pENTJ, pISTP, pESTP, pESTJ, pISTJ,pINFP, pINFJ, pENFP, pENFJ, pISFP, pESFP, pESFJ, pISFJ]
    all_points_str = ["INTP", "INTJ", "ENTP", "ENTJ", "ISTP", "ESTP", "ESTJ", "ISTJ","INFP", "INFJ", "ENFP", "ENFJ", "ISFP", "ESFP", "ESFJ", "ISFJ"]
    
    # - Si la personne à que des fonctions Xi ou Xe, alors la probabilité qu'elle soit Exxx ou Ixxx est augmenté.
    pExtra = [pENTP,pESTP,pENTJ,pESTJ,pENFP,pESFP,pENFJ,pESFJ]
    pIntro = [pINTP,pISTP,pINTJ,pISTJ,pINFP,pISFP,pINFJ,pISFJ]
    # 4 fonctions 
    if NI > NE and FI > FE and TI > TE  and SI > SE:
        #pENTP -=5;pESTP -=5; pENTJ -=5;pESTJ -=5; pENFP -=5;pESFP -=5;pENFJ -=5;pESFJ -=5
        for fonct_extraverti in pExtra:
            fonct_extraverti -=5
    elif NI < NE and FI < FE and TI < TE  and SI < SE:
        #pINTP -=5;pISTP -=5; pINTJ -=5;pISTJ -=5; pINFP -=5;pISFP -=5;pINFJ -=5;pISFJ -=5
        for fonct_intro in pIntro:
            fonct_intro -=5
    # 3 fonctions + Xx / Xy < 0.75
    ilst = [TI,NI,SI,FI] # ilst <=> introverted List
    elst = [TE,NE,SE,FE] # elst <=> extraverted List
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if i != j and i != k and k != j:
                    if (ilst[i]<elst[i] and ilst[j]<elst[j] and ilst[k]<elst[k]) and (ilst[i]/elst[i]<0.75 and ilst[j]/elst[j]<0.75 and ilst[k]/elst[k]<0.75):
                        for fonct_intro in pIntro:
                            fonct_intro -=3
                    if (elst[i]<ilst[i] and elst[j]<ilst[j] and elst[k]<ilst[k]) and (elst[i]/ilst[i]<0.75 and elst[j]/ilst[j]<0.75 and elst[k]/ilst[k]<0.75):
                        for fonct_extraverti in pExtra:
                            fonct_extraverti -=3
    # ---------------------------------------------------------------------------------------------------------- #


    ordonned_list = sorted(all_points, reverse = True)
    ordonned_list_str = [""]*16
    for i in range(len(ordonned_list)):
        for j in range(len(ordonned_list)):
            if ordonned_list[i] == all_points[j]:
                print(all_points_str[j] +":"+str(ordonned_list[i])+"/100")
                ordonned_list_str[i] = all_points_str[j]
    if ordonned_list[1]/ordonned_list[0]>0.90:
        print(f"Les résultats entre {ordonned_list_str[0]} et {ordonned_list_str[1]} sont très serré.\nCependant vous affichez une légère préférence pour {ordonned_list_str[0]}\n{ordonned_list_str[2]} est également possible.\nPlus de détails sur la liste au dessus.")
    elif ordonned_list[1]/ordonned_list[0]<0.75:
        print(f"Avec quasi-certitude vous êtes {ordonned_list_str[0]}.\nPlus de détails sur la liste au dessus.")
    else:
        print(f"Nous pensons que vous êtes {ordonned_list_str[0]}.\nCependant {ordonned_list_str[1]} est également possible, mais moins probable.\n{ordonned_list_str[2]} est également possible.\nPlus de détails sur la liste au dessus.")




def beginning():
    code_or_test = True
    while code_or_test:
        code = input("Voulez-vous passez un test [T] ou entrez votre code [C]?\n>>>")
        if code.upper() not in ["T", 'C']:
            print("Je n'ai pas compris. Entrez C pour le code et T pour le test.")
        elif code == "C":
            code_nb = input("Entrez le code:\n")
            code_nb = code_nb.lower()
            Ti = 0; Ne = 0;Si = 0;Fe = 0; Te = 0; Ni = 0; Se = 0; Fi = 0
            all_func_list = [Ti,Te,Ni,Ne,Si,Se,Fi,Fe]
            for i in range(8): #640a0f4b32051419
                all_func_list[i] =int("0x"+str(code_nb[i*2:i*2+2]),16)
            code_or_test = False
            print(all_func_list)
            analysis(all_func_list[0], all_func_list[1], all_func_list[2], all_func_list[3],all_func_list[4], all_func_list[5], all_func_list[6], all_func_list[7])
            x = np.array(["Ti", "Te", "Ni", "Ne","Si", "Se", "Fi", "Fe"])                                                  #
            y = np.array([all_func_list[0], all_func_list[1], all_func_list[2], all_func_list[3],all_func_list[4], all_func_list[5], all_func_list[6], all_func_list[7]])                                                                  #                                                                                                                        #
            plt.bar(x,y, color=['#3480eb','#5b97eb', '#f2d00c','#ffe657', '#40b361','#59c979', '#c41837','#c9324e'])       #
            plt.show()                    
            sys.exit()
        elif code == 'T':
            code_or_test = not code_or_test



beginning()

def clear(): # Clear the Terminal
    _ = system('cls') if name == 'nt' else system('clear')

clear()
################
# SCORE DES FC # 
################
Ti_Te = 0 # Ti_Te < 100 <=> Ti ||| Ti_Te > 100 <=> Te
Ni_Ne = 0 # Ni_Ne < 100 <=> Ni ||| Ni_Ne > 100 <=> Ne
Si_Se = 0 # Si_Se < 100 <=> Si ||| Si_Se > 100 <=> Se
Fi_Fe = 0 # Fi_Fe < 100 <=> Fi ||| Fi_Fe > 100 <=> Fe
##################

###############
#     FC      #
###############
Ti = 0        #
Ne = 0        #
Si = 0        #
Fe = 0        #
Te = 0        #
Ni = 0        #
Se = 0        #
Fi = 0        #
###############


list_main_funct = ["T","N","S","F"]

##################################
# LISTE DES QUESTIONS NON FAITES #
##################################
T_quest = []                     #
N_quest = []                     #
S_quest = []                     #
F_quest = []                     #
##################################
All_quest = [T_quest,N_quest,S_quest,F_quest]  


def presentation(qst):
    Introvert_funct = list((qst).items())[0][1] # La phrase des fonctions introvertis
    Extravert_funct = list((qst).items())[1][1] # La phrase des fonctions Extraveris
    print("#"*50)
    print("#" + " " *11 + "1" + ' '*11+ '|' +' '*12 + '2' + " "*11+ "#")
    print("#"*50)
    len_str = True
    inc_var = 0 #An increasing variable
    while len_str:
        if len(Introvert_funct) - inc_var*23 >= 0 or len(Extravert_funct) - inc_var*23 >= 0:
            if len(Introvert_funct) - inc_var*23 < 23 and len(Extravert_funct) - inc_var*23 < 23:
                print("#"+Introvert_funct[inc_var*23:(inc_var+1)*23] + " "*min((23-(len(Introvert_funct) - inc_var*23)),23)+"|"+Extravert_funct[inc_var*23:(inc_var+1)*23] + " "*min(23-(len(Extravert_funct) - inc_var*23),23)+"#")
                print("#"*50)
                len_str = not len_str
            elif len(Introvert_funct) - inc_var*23 < 23:
                print("#"+Introvert_funct[inc_var*23:(inc_var+1)*23] + " "*min((23-(len(Introvert_funct) - inc_var*23)),23)+"|"+Extravert_funct[inc_var*23:(inc_var+1)*23]+'#')
            elif len(Extravert_funct) - inc_var*23 < 23:
                print('#'+Introvert_funct[inc_var*23:(inc_var+1)*23]+"|"+Extravert_funct[inc_var*23:(inc_var+1)*23] + " "*min(23-(len(Extravert_funct) - inc_var*23),23)+"#")
            else:
                print('#'+Introvert_funct[inc_var*23:(inc_var+1)*23]+'|'+Extravert_funct[inc_var*23:(inc_var+1)*23]+'#')
            inc_var+=1
    print("[---]    [--]    [-]    [0]    [+]    [++]    [+++]")




for funct in range(len(list_main_funct)):
    for j in range(1,len(FC[list_main_funct[funct]])+1):
        j = str(j)
        All_quest[funct] += [j]

def questions_test(lettre, fonction_intro, fonction_extra, diff):
    for i in range(0,10):
        if i<10:
            searching = True
        else:
            searching =False
        while searching: # Détermine un nombre aléatoire qui n'a pas été encore choisit
            nb_to_delete = random.randint(1,11)
            for j in range(len(All_quest[0])):
                try:
                    if All_quest[0][j] == str(nb_to_delete):
                        searching = not searching
                        del All_quest[0][j]
                except IndexError:
                    pass
        question = FC[lettre][str(nb_to_delete)]
        presentation(question)
        waiting = True
        while waiting:
            waiting=not waiting
            réponse = input("Votre réponse >").replace("[","").replace("]","")
            if len(réponse)>2:
                réponse = réponse[:3]
            if réponse[0] == '-':
                fonction_intro += len(réponse)*2.5 + 2.5
            elif réponse[0] == '+':
                fonction_extra += len(réponse)*2.5 + 2.5
            elif réponse[0]== '0':
                pass
            else:
                waiting=not waiting
                print("Je n'ai pas compris.")
        clear()
    return [fonction_intro,fonction_extra]

#Ti VS Te
[Ti, Te] = questions_test("T", Ti, Te, Ti_Te)
#Ni VS Ne
for funct in range(len(list_main_funct)):
    for j in range(1,len(FC[list_main_funct[funct]])+1):
        j = str(j)
        All_quest[funct] += [j]
[Ni, Ne] = questions_test("N", Ni, Ne, Ti_Te)
#Si VS Se
for funct in range(len(list_main_funct)):
    for j in range(1,len(FC[list_main_funct[funct]])+1):
        j = str(j)
        All_quest[funct] += [j]
[Si, Se] = questions_test("S", Si, Se, Ti_Te)
#Fi VS Fe
for funct in range(len(list_main_funct)):
    for j in range(1,len(FC[list_main_funct[funct]])+1):
        j = str(j)
        All_quest[funct] += [j]
[Fi, Fe] = questions_test("F", Fi, Fe, Ti_Te)
print(f"{Ti=} {Te=}\n{Ni=} {Ne=}\n{Si=} {Se=}\n{Fi=} {Fe=}\n")

Ti = int(Ti)
Te = int(Te)
Ni = int(Ni)
Ne = int(Ne)
Si = int(Si)
Se = int(Se)
Fi = int(Fi)
Fe = int(Fe)

all_func_list = [Ti,Te,Ni,Ne,Si,Se,Fi,Fe]

###########################################################################################
#                               C       O       D       E                                 #
###########################################################################################
code = "".join(                                                                           #
    str(hex(func))[2:4] if func > 16 else "0" + str(hex(func))[2:4]                       #
    for func in all_func_list                                                             #
).upper()                                                                                 #
print("Votre code est:", code,"\nGardez le si vous voulez revoir vos résultats")          #
###########################################################################################

analysis(Ti,Te,Ni,Ne,Si,Se,Fi,Fe)





################################################################################################################
#                                  P        L       O       T                                                  #
################################################################################################################
x = np.array(["Ti", "Te", "Ni", "Ne","Si", "Se", "Fi", "Fe"])                                                  #
y = np.array([Ti, Te, Ni, Ne,Si, Se, Fi, Fe])                                                                  #
                                                                                                               #
plt.bar(x,y, color=['#3480eb','#5b97eb', '#f2d00c','#ffe657', '#40b361','#59c979', '#c41837','#c9324e'])       #
plt.show()                                                                                                     #
################################################################################################################