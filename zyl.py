with open('201811113006.log', mode='r', encoding='utf8') as file:
    num=0
    for line in file:
        data = file.readline()
    data = data[26:38]
    data2 = bytes.decode(data)
    if data2 == '201811113006':
        num = num + 1
    print(num)