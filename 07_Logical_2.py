input_id = input("Please, enter your ID!\n")
input_pw = input("Please, enter your Password!\n")
real_id = "nanoyslee"
real_pw = "11"
if real_id == input_id:
    if real_pw == input_pw:
        print("Hello!")
    else:
        print("Wrong Password")
else:
    print("ID Not Exist")
