
def Positive(frase):
    not_index = frase.find('not')
    bad_index = frase.find('bad')
    frase = frase[0 : not_index] + 'good' + frase[ bad_index + 3: ]
    return print(frase) 


Positive("This dinner is not tha bad!")
Positive("Honestly, not today nor yesterday was it bad outside")