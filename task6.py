'''
Balanced Brackets https://www.hackerrank.com/challenges/balanced-brackets/problem
'''

def hodi_for_balanced(hod):
    i=0
    while i < hod:
        string = input("введите набор символов:")
        listok = ' '.join(string).split()
        some_listok.append(listok)
        i+=1
    return some_listok

def Balanced_Brackets(some_listok):
    dict_Bracket = {1: '{', 2: '}', 3: '[', 4: ']', 5: '(', 6: ')'}
    i=0
    for list in some_listok:
        
        while 1:
            if len(some_listok[i])==1:
                print("NO")
                i+=1
                break
            if len(some_listok[i])<1:
                print("YES")
                i+=1
                break
            if some_listok[i][0] == dict_Bracket[1] and dict_Bracket[2] == some_listok[i][-1]:
                some_listok[i].pop(0) and some_listok[i].pop(-1)
                continue 
        
            elif some_listok[i][0] == dict_Bracket[3] and dict_Bracket[4] == some_listok[i][-1]:
                some_listok[i].pop(0) and some_listok[i].pop(-1)
                continue
        
            elif some_listok[i][0] == dict_Bracket[5] and dict_Bracket[6] == some_listok[i][-1]:
                some_listok[i].pop(0) and some_listok[i].pop(-1)
                continue
            else:
                print("NO")
                i += 1 
                break
    


hod = int(input('количество переборов: '))      
some_listok = []
some_listok = hodi_for_balanced(hod)
Balanced_Brackets(some_listok)