# List methods
dir(list)
list1 = ["apple", "grapes", "banana", "grapes"]
list1
list1.append("orange")
list1.clear()
list2 = list1.copy()
list2
print(id(list1),id(list2))
list1.count("grapes");
list1.extend(["gauva","pineapple"])
list1.index("banana")
list1.insert(2,"mango")
list1.pop(2)
list1.remove("grapes")
list1.reverse()
list1.sort(reverse=True)

# String methods
dir(str)
str1 = "héllo   wørLd"
str1.capitalize()
str1.casefold()
str1.center(21,"X")
str1.count("l")
str1.encode("ascii", errors="replace")
str1.endswith("Ld")
str1.expandtabs()
str1.find("lo")
str1.format()
str1.zfill(12)
str1.index("and")
str1.find("and")
str1.isalnum()
str1.join("helloworld")
str1.replace("hello", "hii")
str1.ljust(21,"q")
str1.split(" ")
str1.swapcase()
str1.strip()

# Set methods
set1 = {1,2,3,4,5,6}
set2 = {2,3,4,0}
set1.update([5])
set1.symmetric_difference(set2)
set1.isdisjoint(set2)
set2.issubset(set1)
set1.issuperset(set2)

# Dictionary methods
dir(dict)

x = ["name","age","rollno","phone"]
dict.fromkeys(x)

dt = {
    "name": "nishal",
    "age": 12,
    "phone": "30/12/2003"
}
dt
dt.get("class","not given")
dt.items()
dt.keys()
dt.pop("name")
dt.popitem()
dt.setdefault("class","not given")
dt.update({"name": "rajeev"})
dt.values()

# For loop test cases
x = [1,2,3,4,5]
even = []
for i in x:
    if(i%2 ==0):
        print(i)
        even.append(i)
even

str1 = "NishalNM072"
cap = []
small = []
num = []
for i in str1:
    if(i.islower()):
        small.append(i)
    elif(i.isupper()):
        cap.append(i)
    elif(i.isnumeric()):
        num.append(i)
print(cap,small,num)

x=4
for i in range(x+1):
    j = (x-i) * ' '
    print(j + i*"* ")

x = [-3,6,4,-8,7,1,2]
x.sort()
x.pop()