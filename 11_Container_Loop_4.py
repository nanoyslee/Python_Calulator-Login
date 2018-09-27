# input_id = input("Please, enter your ID!\n")
# real_nanoyslee = "nanoyslee"
# real_k8805 = "k8805"
# if real_nanoyslee == input_id:
#     print("Hello!, nanoyslee")
# elif real_k8805 == input_id:
#     print("Hello!, k8805")
# else:
#     print("Who are you?")

input_id = input("Please, enter your ID!\n")
members = ['nanoyslee', 'k8805', 'leezche']
for member in members:
    if member == input_id:
        print('Hello!, '+member)
        import sys
        sys.exit()
print('Who are you?')
