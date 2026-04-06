# for i in range(5):
#     print(i)

# for char in "hello":
#     print(char)

# nums=[10,20,30]

# for n in nums:
#     print(n)

# n=1

# if n==1:
#     print("Great")
# elif n==3:
#     print("Greatest")
# else:
#     print("greatsi")


# for i in range(10):
#     if i%2==0:
#         print(i,"even")


# with open("file.txt","r") as f:
#     d=f.read()
#     print(d)


# with open("file.txt","r") as f:
    
#     for line in f:
#         print(line.strip())
# CNT=0

# with open("file.txt","r") as f:
#     for line in f:
#         if "error" in line.lower():
#             print(line)
#             CNT=CNT+1

# print(CNT)


#1)
for i in range(10):
    if i%2==0:
        print(i,"even")

#2)
with open("file.txt","r") as f:
    for line in f:
        if "ERROR" in line:
            print("ALERT:",line)


#3)
with open("file.txt","r") as f:
    data=f.read()
    print(data)

#4)
cnt=0
with open("file.txt","r") as f:
    for line in f:
        if "ERROR" in line:
            print(line)
            cnt+=1
print(cnt)

#5)
with open("file.txt","r") as f:
    for i,line in enumerate(f,start=1):
        if "error" in line.lower():
            print(f"{i}:line")
