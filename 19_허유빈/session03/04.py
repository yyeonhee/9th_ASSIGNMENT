dictionary = {}
# key = 0
# value = 0

while True :
    print("===insert===")
    key = input("key >> ")
    value = input("value >> ")
    dictionary[key] = (value)

    if key == "cake" :
        print("===result===")
        print(dictionary.values())
        break 