age = 25;

if age < 13:
    print("child")
elif age < 20:
    print("teenager")
elif age < 60:
    print("adult");
else: 
    print("senior");

# program using taking input 
age = input("enter your age: ");
age_in_integer  = int(age);

if age_in_integer < 13:
    print("child")

elif age_in_integer < 20: 
    print("teenager")

elif age_in_integer < 60:
    print("adult")

else:
    print("senior");
