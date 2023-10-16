counts = int(input("Enter count"))
lists = []
for i in range(counts):
    leng = input("Enter sentence: ")
    lists.append(leng)
    
for check in lists:
    if check.startswith("E"):
        print('Success')
    else:
        print("succ")
    

# op = len(leng)
# print(op)


# while True:
#     kartik = input("Enter name: ")
#     caps = kartik.capitalize()
#     print(caps)


