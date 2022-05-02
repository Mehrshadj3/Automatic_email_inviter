#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

names = open('/Users/mehrshadjavadi/PycharmProjects/pycharm/day24/Input/Names/invited_names.txt','r')
names1 = names.readlines()







text = open('/Users/mehrshadjavadi/PycharmProjects/pycharm/day24/Input/Letters/starting_letter.txt','r' )

text1 = text.read()











for item in names1:
    stri = item.strip()
    thing = text1.replace('[name]', str(stri))
    print(thing)
    with open(f'./Output/ReadyToSend/letter_for_{stri}.txt','w') as ready_letter:
        ready_letter.write(thing)