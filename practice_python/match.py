from functions import show, edit, done
import time
now = time.strftime("%b %d, %Y %H:%M:%S")


inp = ['hi','bi','dsi']
def show():
    for i, value in enumerate(inp, start=1):
            print(f'{now}:{i}. {value}')
            
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
#write show function common to all other functions with parameters if possible

    
while True:
    user = input("show, add, edit, done or exit: ").strip()
    # user= user.strip()
    
    match user:
        case 'add':
            adds = input('add to do: ')
            adds = now + adds
            inp.append(adds)
        case 'show':
            show()
        case 'edit':
            try:
                edit()
            except ValueError:
                print("Enter a number only. Try again.")
                continue
                # user = input("show, add, edit, done or exit: ").strip()
                # edit()
        case 'exit':
            break
        case 'done':
            done()
        case _:
            print('Look again')
            

    
    
print('bye')
         