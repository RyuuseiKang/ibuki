import os

f = open(os.path.dirname(os.path.abspath(__file__)) + "\oto.ini", 'r+', encoding='shift-jis')
wFile = open(os.path.dirname(os.path.abspath(__file__)) + "\oto_edited.ini", 'w', encoding='shift-jis')

overlap_increasement_value = float(input('overlap increasement: '))
# left_increasement_value = float(input('left increasement: '))

fixed_arr = ['が','ぎ','ぐ','げ','ご',
            'ざ','じ','ず','ぜ','ぞ',
            'だ','ぢ','づ','で','ど',
            'な','に','ぬ','ね','の',
            'は','ひ','ふ','へ','ほ',
            'ば','び','ぶ','べ','ぼ',
            'ぱ','ぴ','ぷ','ぺ','ぽ',
            'ま','み','む','め','も',
            'や','ゆ','よ','いぇ','ヴ',
            'ら','り','る','れ','ろ',
            'ラ','リ','ル','レ','ロ']

while True:
    line = f.readline().strip()
    if not line:
        break

    currentLine = line.split(',')

    value = currentLine[0].split('=')[1]

    for i in range(len(fixed_arr)):
        if (fixed_arr[i] in value):            
            overlap = currentLine[5]
            currentLine[5] = str(round(float(overlap) + overlap_increasement_value, 3))

            line = ','.join(currentLine)
            print(value + ', ' + overlap + ' -> ' + currentLine[5])
        
    wFile.write(line + '\n')

f.close()