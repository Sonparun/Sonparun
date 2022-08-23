text1='anirachmingkhawn'
text2='thequickbrownfoxjumpover'
text3=''

lowerlist=[1]

textrange=len(text1)
for i in range(3,textrange):
    if lowerlist[-1] >= textrange:
        break
    lowerlist.append(lowerlist[-1]+i)

for i in range(0, textrange):
    text3+=text1[1].lower() if i in lowerlist else text1[i].upper()
    print(text3)