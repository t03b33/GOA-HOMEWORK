
name = input("What's your name?")
age = int(input("How old are you?"))

print("Hey ", name, ", You are ", age, " years old.")

#--------------------------------------------------------

a = int(input("Number 1:"))
b = int(input("Number 2:"))

print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)

#--------------------------------------------------------

a = input("Str input 1:")
b = input("Str input 2:")

print(a==b)
print(a!=b)
print(a<b)
print(a>b)

#--------------------------------------------------------

user_string1 = input("enter a string 1")
user_string2 = input("enter a string 2")
user_string3 = input("enter a string 3")

list = [user_string1, user_string2, user_string3]
sorted_list = sorted(list)

print(sorted_list)

#--------------------------------------------------------

long = max(sorted_list)
short = min(sorted_list)

print("Longest string:", long, "Shortest string:", short)

#--------------------------------------------------------

user_lower_string1 = user_string1.lower()
user_lower_string2 = user_string2.lower()
user_lower_string3 = user_string3.lower()

lower_list = [user_lower_string1, user_lower_string2, user_lower_string3]
sorted_lower_list = sorted(lower_list)

print(sorted_lower_list)

#--------------------------------------------------------

string1 = input("Input a string")
string2 = input("Input a string")
string3 = input("Input a string")

print(string1 < string2 and string2 < string3)

#--------------------------------------------------------

sum = 0

for i in range(3, 25):
    sum = sum + i

print(sum)

#--------------------------------------------------------