import os

paht1 = 'd:\\11'
aa = os.listdir(paht1)
paht2 = 'd:\\22'
bb = os.listdir(paht2)

a = []
b = []
for file1 in aa:
    with open(f"d:\\11\\{file1}", encoding='utf-8') as pythonFile:
        content = pythonFile.readlines()
        a.extend(content)
for file2 in bb:
    with open(f"d:\\22\\{file2}", encoding='utf-8') as pythonFile:
        content2 = pythonFile.readlines()
        b.extend(content2)
print("*" * 10)
print(a)
print("*" * 20)
print(b)
print("*" * 30)
print(len(a))
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            print("两行内容一样")
            break
