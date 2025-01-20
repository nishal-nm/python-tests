num_names = input("Enter the Number: ")
num_list = num_names.replace("-", " ").casefold().split()
num_list = [x for x in num_list if x != "and"]
digits = {
    "zero": 0,
    "one":1, 
    "two":2, 
    "three": 3, 
    "four": 4, 
    "five": 5, 
    "six": 6, 
    "seven": 7, 
    "eight": 8, 
    "nine":9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90,
    "thousand": 1000,
    "million": 1000000
}


def converter(num_list):
    value = 0
    res = 0
    for num in num_list:
        if(num == "hundred"):
            value *= 100
        elif(num in ["thousand", "million"]):
            res += value * digits[num]
            value=0
        else:
            value += digits[num]

    res += value

    return res

print(converter(num_list))