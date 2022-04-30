import os

f = open(os.path.dirname(os.path.abspath(__file__)) + "\oto.ini", 'r+', encoding='shift-jis')
wFile = open(os.path.dirname(os.path.abspath(__file__)) + "\oto_edited.ini", 'w', encoding='shift-jis')

print('prefix: ')
prefix = input()

print('suffix: ')
suffix = input()

while True:
    line = f.readline().strip()
    if not line:
        break

    str = line.split(',')

    head = str[0].split('=')

    str[0] = head[0] + '=' + prefix + head[1] + suffix

    line = ','.join(str)
    print(line)
    
    wFile.write(line + '\n')

f.close()