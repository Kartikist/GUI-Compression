import json

with open('quiz_quest.json', 'r') as file:
    content = file.read()
    
    
data = json.loads(content)   
print(data)
score = 0

for question in data:
    
    print(question['Question'])
    for index, options in enumerate(question['Options'], start=1):
        print(index , '-', options)
    choice = int(input("enter right option: "))
    
    if choice == question['Correct']:
        score += 1
            
print(f"Your score is {score}/{len(data)}")
            
            
                
            
    