str1 = input("Enter first string: ").casefold().replace(" ", "")
str2 = input("Enter second string: ").casefold().replace(" ", "")
str1_list = list(str1)
str1_list.sort()
str2_list = list(str2)
str2_list.sort()
print(str1_list == str2_list)