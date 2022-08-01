import json
import random

with open('classes.json','r') as f:
    data = json.load(f)


for i in range(1, 11):
    data1 = {'Class':f'{i}-A','Password': f'{random.randrange(1000000)}'}
    data2 = {'Class':f'{i}-B','Password': f'{random.randrange(1000000)}'}
    data3 = {'Class':f'{i}-C','Password': f'{random.randrange(1000000)}'}
    data4 = {'Class':f'{i}-D','Password': f'{random.randrange(1000000)}'}
    data.append(data1)
    data.append(data2)
    data.append(data3)
    data.append(data4)

with open('classes.json','w') as f:
    json.dump(data, f, indent=4)