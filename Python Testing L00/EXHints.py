from tkinter.ttk import Separator


inputmsg=input('In put string you want to modify words: ')
print(inputmsg.split())
sepatatewords=inputmsg.split()
print("separate words")
for i in sepatatewords:
    print(i)
print('Modify each words')
print(len(sepatatewords))
for j in range(len(sepatatewords)):
    sepatatewords[j]='G'+sepatatewords[j]
    print(sepatatewords[j])
print(sepatatewords)
print(" ".join(sepatatewords),)





