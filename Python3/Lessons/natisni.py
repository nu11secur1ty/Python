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
        print("\n")
        

### Second example
print("### Second example\n")
city_population = {"New York City": 8550405, 
                   "Los Angeles": 3971883, 
                   "Toronto": 2731571, 
                   "Chicago": 2720546, 
                   "Houston": 2296224, 
                   "Montreal": 1704694, 
                   "Calgary": 1239220, 
                   "Vancouver": 631486, 
                   "Boston": 667137,
                   "Bulgaria": 12342347}
print(city_population["Bulgaria"])
print("\n")


print("### User input\n")
kuvsitive = input("Enter kuvsitive:")
print("Ti si: " + kuvsitive)
print("\n")

### Recursive
print("### Recursive\n")
def factorial(n):
    print("factorial has been called with n = " + str(n))
    if n == 1:
        return 1
    else:
        res = n * factorial(n-1)
        print("intermediate result for ", n, " * factorial(" ,n-1, "): ",res)
        return res	

print(factorial(5))
print("\n")
