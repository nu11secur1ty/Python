#!/usr/bin/python3

# array
print("### array\n")
a = ["magare", "kuche"]
kokaza = a[0]
print(kokaza)
print("\n")

# math
print("### math\n")
operation = 1+3
manga = 5+2
print(manga)


# associative array
print("###associative array\n")
room_num = {'John': 425, 'Liz': 212}
room_num['Isaac'] = 345
print(room_num)
print("\n")


### Dictionaries
print("### Dictionaries\n")
# Create empty dict Capitals
Capitals = dict()
# Fill it with some values
Capitals['Russia'] = 'Moscow'
Capitals['Ukraine'] = 'Kiev'
Capitals['USA'] = 'Washington'
Capitals['BG'] = 'Gosho'

Countries = ['Russia', 'France', 'USA', 'Russia', 'BG']

for country in Countries:
  # For each country from the list check to see whether it is in the dictionary Capitals
    if country in Capitals:
        print('The capital of ' + country + ' is ' + Capitals[country])
    else:
        print('The capital of ' + country + ' is unknown')
        
        

