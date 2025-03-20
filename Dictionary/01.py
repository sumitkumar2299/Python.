# order is important is in list but not in dictionary 

chai_types = {"masala":"spicy","ginger":"zesty","green":"mild",}
print(chai_types);

print(chai_types["masala"]);

print(chai_types.get("ginger"));
print(chai_types.get("gingera"));

chai_types["green"] = "fresh";
print(chai_types);

for chai in chai_types:
    print(chai);

for chai in chai_types:
    print(chai,chai_types[chai]);

# we can also do iteration in this way. 
for key,value in chai_types.items():
    print(key,value);

if "masala" in chai_types: 
    print("i have masala chai");

print(len(chai_types));

# adding key, values in dictionary 

chai_types["earl grey"] = "citrus"
print(chai_types);

# remove 
chai_types.pop("ginger");
print(chai_types);

# removing key,value pair from the last 

chai_types.popitem();
print(chai_types);

# another way of remove 

del chai_types["green"];
print(chai_types);

chai_types_copy = chai_types.copy();
print(chai_types_copy);


# dictionary inside dictionary 

tea_shops = {
    "chai":{"masala":"spicy","ginger":"zesty"},
    "tea":{"green":"mild","black":"strong"}
}
print(tea_shops);
print(tea_shops["chai"]);
print(tea_shops["chai"]["ginger"]);

squared_num = {x:x**2 for x in range(6)}
print(squared_num);

squared_num.clear()
print(squared_num.clear());


# creating dictionary from list 

keys = ["masala","ginger","lemon"];
default_value = "delicious"
new_dict = dict.fromkeys(keys,default_value);
print(new_dict);