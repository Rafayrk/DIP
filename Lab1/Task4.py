sentence = input("Enter Sentence\t")
alp = 0
digit = 0
for i in sentence:
    if i.isalpha():
        alp+=1
    else:
        digit+=1
print("Digits:"+str(digit)+" Alphabets:"+str(alp))