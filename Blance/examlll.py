def capToFront (word):
    s1=''
    s2=''
    for x in word :
        if x.isupper():
            s1=s1+x
        else:
            s2=s2+x
    return s1+s2




print(capToFront('hApPy'))
print(capToFront('moveMENT'))
print(capToFront('ahOrtCAKE'))
