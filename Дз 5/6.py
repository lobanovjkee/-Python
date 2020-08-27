with open('text_6.txt', 'r', encoding='UTF-8') as text_6:
    context = text_6.readlines()
    idk = []
    points = []
    final_dict = {}
    for word in context:
        idk.append(word.split())
    for i in idk:
        final_dict[i[0]] = ''
        points.append(i[1:])
    for i in points:
        for j in i:
            if j == '-':
                i.remove(j)
    j = 0
    for i in final_dict:
        final_dict[i] = points[j]
        j += 1
    print(final_dict)