


import pickle

# #define a function to determine the winning percentage of a player
#
# def rate_wins(dict, player):
#
#
# #key=name of player, value is a tuple(#games played, #victories)
#
# history={'Archy':(12,4), 'Betty': (10, 6)}
# print(history)
# print(history['Archy'])
# print(history['Archy'][0])
# print(history['Archy'][1])
#
# print(history['Betty'])
# print(history['Betty'][0])
# print(history['Betty'][1])
#
# #adding another entry to the dictionary
# history['Carolina']=(15,5)
# print(history)
#
#
# rate_a= history['Archy'][1]/history['Archy'][0]
# print(rate_a)
#
# rate_a= history['Betty'][1]/history['Betty'][0]
# print(rate_a)
#
# rate_a= history['Carolina'][1]/history['Carolina'][0]
# print(rate_a)
#
#
# #delete an entry
# del history['Carolina']
# print(history)
#



def rate_of_winning(dict, player):
    rate=dict[player][1]/dict[player][0]
    return print('The rate of winning for player', player, 'is', round(rate, 2))

history={'Archy':(12,4), 'Betty': (10, 6)}
#
#Create a file and write on it
file_p3=open('historypickle,p', 'wb')
pickle.dump(history, file_p3)
file_p3.close()


file_p3 = open('historypickle,p', 'rb')
history  = pickle.load(file_p3)
file_p3.close()
print(history)
history['Cora']=(100, 80)
print (history)



# rate_of_winning(history,"Archy")
# rate_of_winning(history,"Betty")
#
# history['Clara']=(100,80)
# print(history)
# for key in history.keys():
#     rate_of_winning(history, key)


for key in history.keys():
    rate_of_winning(history, key)