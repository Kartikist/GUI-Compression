inp = ['hi','bi','dsi']


#write show function common to all other functions with parameters if possible
def show():
    for i, value in enumerate(inp, start=1):
            print(f'{i}. {value}')
            
def edit():
    show()
    number = int(input('choose the number to edit: '))
    orig_val = (inp[number -1])
    new_val = input(f'Modify {orig_val}: ')
    inp[number -1] = new_val
    print( inp[number -1])

    
def done():
    show()
    number = int(input('choose the number to complete: '))
    inp.pop(number -1)
    print("Your updated list: ")
    for i, value in enumerate(inp, start=1):
            print(f'{i}. {value}')
    
while True:
    user = input("show, add, edit, done or exit: ").strip()
    # user= user.strip()
    
    match user:
        case 'add':
            adds = input('add to do: ')
            inp.append(adds)
            file = open('todos.txt','w')
            file.writelines(inp)
        case 'show':
            show()
        case 'edit':
            edit()
        case 'exit':
            break
        case 'done':
            done()
        case _:
            print('Look again')
            

    
    
print('bye')
         