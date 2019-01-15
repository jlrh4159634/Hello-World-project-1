'''
i am using juan lib
'''

# from juanlibrary import distance3d
#
# #print(distance3d(0,0,4,3))
#
# print(distance3d(0,0,0,4,3,12))

#
# word= 'whateveryouwant'
# alist=list(word)
# print(alist)


word= 'supercalifragilisticexpialidocious'

alist=list (word)

print(alist)


#convert a list of characters into a word

new_word=''

n=len(alist)
for i in range(n):
    new_word=new_word+alist[i]

print(new_word)