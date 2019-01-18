'''
Using dictionaries to translate a text
'''


mydictionary={'oranges':input ("some fruit"), 'bananas':input ("some other fruit or thing"), 'great':input ("an adjective"), 'smart':input("another objective")}

text ='I love oranges and bananas because they make me feel great ans smart'

# translation function with text and dictionary as parameters

def translate (text1, dict1):
    list_text1=text1.split()
    new_text=[]
    for word in list_text1:
        translation=dict1.get(word)
        new_text.append(translation if translation else word)
    return' '.join(new_text)

print(translate(text, mydictionary))
