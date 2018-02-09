sentence = input("Enter Sentence\t").split(" ")

dic = {}

for i in sentence:

    if i in dic.keys():
        dic[i] += 1

    else:
        dic[i] = 1

print(dic)