tea_varities = ["black","green","oolong","white"]
print(tea_varities);
print(tea_varities[0]);
print(tea_varities[1]);
print(tea_varities[-1]);
print(tea_varities[1:3]);
print(tea_varities[:2]);
print(tea_varities[2:]);
print(len(tea_varities));

tea_varities[3] = "herbal";
print(tea_varities);
tea_varities[1:2] = ["lemon"]
print(tea_varities);
tea_varities[1:3] = ["green","masala"];



tea_varities = ["black","green","oolong","white"]
print(tea_varities[1:1]);

tea_varities[1:1] = ["test","test"];
print(tea_varities);
print(tea_varities[1:2]);
print(tea_varities[1:3]);
tea_varities[1:3] = []
print(tea_varities);


tea_varities = ["black","green","oolong","white"]
for tea in tea_varities:
    print(tea);

for tea in tea_varities:
    print(tea,end="-");

if "oolong" in tea_varities:
    print("i have oolong tea");

tea_varities.append("oolong2");
print(tea_varities);

if "nothing" in tea_varities:
    print("i don't have this type of tea");


tea_varities.pop();
print(tea_varities);

tea_varities.remove("green");
print(tea_varities);

tea_varities.insert(1,"green");
print(tea_varities);

tea_varities_copy = tea_varities.copy()


squared_num = [x**2 for x in range(10)];
print(squared_num);

cube_num = [y**3 for y in range(5)]
print(cube_num);