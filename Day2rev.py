# # def greet():
# #     print("Hello")

# # greet()

# # def greet(name):
# #     print(f"Hi {name}. How are you?")

# # greet("Sagar")

# # def add(a,b):
# #     return a+b

# # print(add(1,2))


# def read_file(fil,keyword):
#     cnt=0
#     with open(fil,"r") as f:
#             for i,line in enumerate(f,start=1):
#                 if keyword in line.lower():
#                     print(f"{i}:",line)
#                     cnt+=1
#                 if cnt==3:
#                         break
#     return cnt


# read_file("file.txt","error")


# def name(name):
#       print(f"Hello",name)


# name("SAGAR")

# def sumnum(num1,num2):
#       return num1+num2


# res=sumnum(1,2)
# print(res)


# def refi(filename):
#       with open(filename,"r") as f:
#             fil=f.read()
#             print(fil)


# refi("file.txt")

# cntt=0
# def keyf(file,key):
#       cntt=0
#       matches=[]
#       key=key.lower()
#       with open(file,"r") as f:
#             for i,line in enumerate(f,start=1):
#                   if key.lower() in line.lower():
#                         cntt+=1 
#                         matches.append((i,line.strip()))
                         
#             return cntt,matches
            
# count,plo=keyf("file.txt","error")

# for i,line in plo:
#       print(f"Line {i}:{plo}")
      






def read_error(filename,keyword,limit=None,show=True):
    cnt=0
    lis=[]
    printed=0
    with open(filename,"r") as f:
        for i,line in enumerate(f,start=1):
            if keyword.lower() in line.lower():
                cnt+=1
                lis.append((i,line))
            if show:
                if limit is None or cnt <=limit:
                   print(f"Line{i}:{line}")
                   printed+=1

    return cnt,lis

count,line=read_error("file.txt",keyword='error',limit=1,show=True)
print(f"Total matches:",count)







