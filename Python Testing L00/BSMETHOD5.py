from turtle import position, st


string='Four score and seven years ago'
position=string.find('score')
if position != -1 :
    print('The word "seven" wasfound at index',position)
else :
    print('The word "seven" was not found')