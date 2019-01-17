'''
i am using juan lib


Using dictionaries to translate a text
'''

text = "My favorite fruits are oranges and bananas , because they make me feel great and smart"

list_text=text.split(' ')


mydictionary={'oranges':'naranjas', 'bananas':'platanos', 'great':'grandioso', 'smart':'inteligente'}

for i in range(len(list_text)):
    for key in mydictionary.keys():
        if list_text[i]==key:
            list_text.remove(list_text[i])
            list_text.insert(i, mydictionary[key])

print(list_text)

#put back the list of words into a text
newtext=''
for word in list_text:
    newtext= newtext+' '+word

print(newtext)




# #how to get all the keys in a dictionary
#
# print(mydictionary.keys())
#
# #how to print the values in a dictionary
#
# print(mydictionary.values())
# print (mydictionary['oranges'])

