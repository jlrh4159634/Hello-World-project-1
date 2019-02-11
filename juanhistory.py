
#define a function to determine the winning percentage of a player

def rate_wins(dict, player):
    

#key=name of player, value is a tuple(#games played, #victories)

history={'Archy':(12,4), 'Betty': (10, 6)}
print(history)
print(history['Archy'])
print(history['Archy'][0])
print(history['Archy'][1])

print(history['Betty'])
print(history['Betty'][0])
print(history['Betty'][1])

#adding another entry to the dictionary
history['Carolina']=(15,5)
print(history)


rate_a= history['Archy'][1]/history['Archy'][0]
print(rate_a)

rate_a= history['Betty'][1]/history['Betty'][0]
print(rate_a)

rate_a= history['Carolina'][1]/history['Carolina'][0]
print(rate_a)


#delete an entry
del history['Carolina']
print(history)