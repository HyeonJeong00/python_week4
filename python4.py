fruit_dictionary={}

while True:
    fruit = input("Enter a fruit type (q to quit): ")
    
    if (fruit == "q"):
        break
    else:
        fruit_dictionary[fruit] = ""
        weight = input("Enter the weight in kg: ")
        fruit_dictionary[fruit]=weight
print(fruit_dictionary)