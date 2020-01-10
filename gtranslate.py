from googletrans import Translator
translator=Translator()

text = input("Enter the text you want to convert..\n")
choice = int(input("enter the choice \n1. Marathi\n2. Hindi\n3. Gujrati\n"))
dest = {}
if(choice == 1):
    dest["Marathi"] = "mr"
elif(choice == 2):
    dest["Hindi"] = "hi"
elif(choice == 3):
    dest["Gujrati"] = "gu"
else:
    print("Unsupported Language...")

for key, value in dest.items():
    print(translator.translate(text, dest=value).text)