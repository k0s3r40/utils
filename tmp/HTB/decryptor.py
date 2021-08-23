import re

alphabet = r'abcdef\147\150\151\152\153\l\155\156\o\160\161\162\163\tu\166\167\170\171\172\101\102\103\104\105\106\107\110\111\112\113\114\115\116\117\120\121\122\123\124\125\126\127\130\131\132\0123456789'

data = alphabet.split('\\')
final_data = []
for i in data:
    if i.isalpha():
        for x in i:
            final_data += x
    else:
        final_data.append(i)
import string
print(final_data)
with open('G_unfcked.txt') as f:
    new_data = f.read()
    print(string.ascii_lowercase + string.ascii_uppercase)
    for index, value in enumerate(final_data):
        if len(value) ==3:
            new_data = new_data.replace(f'\{value}', (string.ascii_lowercase + string.ascii_uppercase)[index])
    new_data = new_data.replace('\\40', ' ')
    # new_data = new_data.replace('\\\\\\\\w', '\w')
    print(new_data)
    with open('G_replaces.txt', 'w') as g:
        g.write(new_data)