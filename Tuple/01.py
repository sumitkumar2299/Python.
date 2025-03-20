# list = mutable => modify
# tuple = imutable => no modification

tea_types = ("black","green","oolong")
print(tea_types);
print(tea_types[0]);
print(tea_types[1:]);
# tea_types[0] = "lemon";
# this will not change because of tuples are immutable. 

# print(tea_types);

print(len(tea_types))
more_tea = ("herbal","earlgrey")
all_tea = more_tea + tea_types;
print(all_tea);


if "green" in all_tea:
    print("i have green tea");

more_tea = ("herbal","earlgrey","herbal");
print(more_tea);
print(more_tea.count("herbal"));


print(tea_types);
(black,green,oolong) = tea_types;
print("black");