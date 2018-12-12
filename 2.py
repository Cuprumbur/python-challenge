dic = dict()
with open("data 2.txt",mode = 'r') as text_file:
    text=text_file.read()
    for i in text:
        exist = i in dic
        if (not exist):
            dic[i]= 1
        else:
            dic[i] += 1
            

for key, value in dic.items():
    print("{0} {1}".format(key,value))

print()
for key, value in dic.items():
    if (value == 1):
        print("{0} {1}".format(key,value))
# eilquty

#reorgonize

# equality = > next http://www.pythonchallenge.com/pc/def/eilquty.html
