import json 

DATA =[]
USER =[]

with open('todo.json') as f:
    DATA = json.load(f)

with open('user.json') as f:
    USER = json.load(f)

def resolve_holidays(id):
    print("Before :",USER)
    for i in range(len(USER)):
        if id == USER[i]['id']:
            USER.remove(USER[i])
            break
    with open('todo1.json', 'w') as f:
            json.dump(USER, f)
            
    return USER

        
print(resolve_holidays(1))