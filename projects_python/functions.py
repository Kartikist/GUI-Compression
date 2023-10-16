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
     
if __name__ == "__main__":    
    inp = ['hi','bi','dsi']
