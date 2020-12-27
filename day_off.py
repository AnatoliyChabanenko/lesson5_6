c={
    1: 'Monaday',
    2: 'tuesday',
    3: 'wednesday',
    4: 'thursday',
    5: 'friday',
    6: 'saturday',
    7: 'sunday',

}
mydict_k=dict.keys(c)
mydict_i=dict.values(c)
dicor = dict(zip(mydict_i, mydict_k))
print(dicor)
