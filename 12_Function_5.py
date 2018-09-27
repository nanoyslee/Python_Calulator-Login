input_id = input("Please, enter your ID!\n")
def login(_id):
    members = ['nanoyslee', 'k8805', 'leezche']
    for member in members:
        if member == _id:
            return True
    return False

if login(input_id):
    print('Hello, '+input_id)
else:
    print('Who are you?')
