import pyperclip

psw_print = []
psw_real = []

psw_count = len(psw_real) 

print("Welcome to password manager!")
print("You currrently have " + str(psw_count) + " passwords")
for pswp in psw_print:
    print(pswp)
psw_choice = input()
if psw_choice == "---":
    psw = psw_real[0]
    pyperclip.copy(psw)
    print("--- password copyed!")

