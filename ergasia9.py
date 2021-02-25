import re

from collections import Counter

string = open('').read() #συμπληρώστε μέσα στο open τον τίτλο του αρχείου κείμενου που θέλετε να επεξεργαστείτε

new_str = re.sub(r'[^a-zA-Z ]+', '', string)

#print (new_str)

open('b.txt', 'w').write(new_str)

list1=[]

list1[:0]=new_str

list2 = (list(map(str, map(ord, list1)))) #μετατροπή σε ascii

#print(list2)

test_list = [int(i) for i in list2] #μετατροπή κάθε var σε int

#print(test_list)

test_list = [i for i in test_list if i % 2 == 1] #κρατάω μονούς αριθμούς

#print (test_list)

list3 = [str(i) for i in test_list]

#print(list3)

listToStr = ' '.join(map(str, list3))

#print (listToStr)

string2 = (new_str.lower())

print (string2)

z = len(string2)

res = {}

for keys in string2:
    res[keys] = res.get(keys, 0) + 1 #πόσες φορές χρησιμοποιήται το καθε γράμμα

#print (res)

listfor=[]

listfor[:0]=string2

finalist = list(res)

#print (finalist)

l = [0] * len(finalist)

for i in range(0,len(finalist)): #υπολογισμός αριθμού των φορών που χρησιμοποιήται το κάθε γράμμα και πέρασμα του αριθμού σε καινούρια λίστα
    for j in range(0,len(listfor)):
        if finalist[i] == listfor[j]:
            l[i] = l[i]+1

#print(listfor)

print(' ')

#print(finalist)
print(' ')
#print(l)

mpara = "*"

for p in range(0,len(finalist)):
    s = ((l[p]/len(listfor))*100)

    g = int(s)

    if s != g:
        g = g+1

    print(finalist[p],":", mpara * g)
