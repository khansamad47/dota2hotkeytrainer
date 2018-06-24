import json
import numpy
import readchar

DATA_FILE='data.json'
NUMBER_OF_ROUNDS=10

# Loading data
with open(DATA_FILE,'r') as data_file:
    data = json.load(data_file)

keys = numpy.random.choice(
    data["keys"],
    NUMBER_OF_ROUNDS,
)

count_success = 0
print ("="*70)
print ("DOTA2 HOTKEY TRAINER")
print ("TOTAL ROUNDS = %s" % NUMBER_OF_ROUNDS)
print ("ENTER '.' to quit.")
print ("="*70)
for i, key in enumerate(keys):
    print (("%s. PRESS '%s' KEY") % (i+1, key['string']))
    user_input = readchar.readkey()
    if user_input == '.':
        break
    if user_input == key['key']:
        count_success =  1 + count_success
        print ("CORRECT!")
    else:
        print (("WRONG! YOU PRESSED '%s'. THE CORRECT KEY"
            " IS '%s'.") % (user_input, key['key'])
        )

print ("="*70)
print (("SCORE %s of %s.") % (count_success, NUMBER_OF_ROUNDS))
print ("="*70)
