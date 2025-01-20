str1 = input("Enter the string: ")
str1 = str1.casefold()
str_new = ""
for x in str1:
    if(x.isalnum()):
        str_new = str_new + x
print(str_new == str_new[::-1])