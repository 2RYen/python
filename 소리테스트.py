import  winsound        #winsound = 주파수

sound = {'do':261, 're':293, 'mi':329, 'fa':349, 'sol':391, 'ra':440, 'si':493}

melody = ['ra', 'sol', 'fa', 'sol', 'ra', 'ra', 'ra', 'sol', 'sol', 'sol', 'ra', 'ra', 'ra', 'ra', 'sol', 'fa', 'sol', 'ra', 'ra', 'ra', 'sol', 'sol', 'ra', 'sol', 'fa'] 

dual = [2,3,4,3, 3,3,2,3, 3,2,3,3, 2,2,3,4, 3,3,3,3, 4,4,2,4,2]

sing = zip(melody, dual)

for i,r in sing:
    print('melody=',i)
    winsound.Beep(sound[i],1000//r)
# winsound.Beep(sound[i],1000//r)
