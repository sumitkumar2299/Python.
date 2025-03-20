chai = "lemon chai";
print(chai);

chai = "masala chai"
first_char = chai[0];
print(first_char);
slice_chai = chai[0:6];
print(slice_chai);
print(chai[-1]);


num_list = "0123456789";
print(num_list[:])
print(num_list[3:1])
print(num_list[:7])
print(num_list[0:7:2]);


chai = "Masala chai";
print(chai.lower());
print(chai.upper());


chai1 = "  masala chai   ";
print(chai1.strip());

chai = "lemon chai"
print(chai.replace("lemon","ginger"));
print(chai);

# converting string into list 
chai = "lemon,ginger,masala,mint";
print(chai.split());
print(chai.split(",  "))

chai = "masala chai";
print(chai.find("chai"));
# agar kuch nahi milega toh output -1 milega. 

chai = "masala chai chai chai";
print(chai.count("chai"));

chai_type = 'MASALA';
quantity = 2
order = "i ordered {} cups of {} tea";
print(order);
x = order.format(quantity, chai_type)
print(x);


# converting list into string 

chai_variety = ["lemon","masala","ginger"];
print(chai_variety);
print("".join(chai_variety));
print(" ".join(chai_variety))
print("-".join(chai_variety))


chai = "masala chai";
print(len(chai));
for letter in chai:
    print(letter);

chai = "he said, \"masala chai is awesome\"" 
print(chai);

chai = "masala\nchai"
print(chai)

chai = r"masala\nchai";
print(chai);


chai = "masala chai ";
# it finds the word masala is in chai or not. 
print("masala" in chai);
print("masalaa" in chai);



