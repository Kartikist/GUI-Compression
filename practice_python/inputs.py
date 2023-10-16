prompt = "type a todo"
print(prompt + ": ")
inputs = []
count = int(input("count please: " ))
for i in range(count):
    ci = str(i)
    todo1 = input(prompt + ci)
    inputs.append(todo1)


print(inputs)