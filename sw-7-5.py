content_A = ''
content_B = ''

with open('./static/sw-7-5-1.txt', 'r') as file:
    content_A = file.read()

with open('./static/sw-7-5-2.txt', 'r') as file:
    content_B = file.read()

with open('./static/sw-7-5-1.txt', 'w') as file:
    file.write(content_B)

with open('./static/sw-7-5-2.txt', 'w') as file:
    file.write(content_A)