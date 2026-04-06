likp=[10,20,30]


# print(len(likp))
# print(likp[1])
# print(likp[-1])
# print(sum(likp))
print(max(likp))

for i in likp:
    print(i)


data = [(1, "error here"), (5, "disk error"), (10, "timeout"),(10, "failed"),(6, "disks error"),(7, "dics error")]
newd=[]
key="error"
# cnt=0

def lis(keyword,list):
    for line_name,datas in list:
        if keyword.lower() in datas.lower():
            # cnt+=1
             newd.append((datas))

    return newd[-3:]

dlp=lis(key,data)
print(dlp)

line="2026-04-06 10:04:55 ERROR Disk full"
print(line.split(" ")[2])