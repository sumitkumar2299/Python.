x = 2;
y = 5;
z = 7;
print(x+y);

# important => priority table remember, operator precedence table. 



print((x+y)*z);

z = int(2.23);
print(z);

z = float(10);
print(z);

z = "chai" + "code";
print(z);



x = 2;
y = 5;
z = 7;
print (x,y,z);
x = x+1;
y = y*2;
z = z+5;
print(x,y,z);
print(y%2);
print(z**2);


result = 1/3.0;
print(result);


# learn about repr, string and print 

x = repr("chai");
y = str("chai");
print(x,y);
print("chai");



x = 1<2;
print(x);

y = 5.0 == 5.0;
print(y);

z = 4.0 != 5.0;
print(z);


# chained comparison 

x = 2;
y = 3;
z = 4;

w = x<y<z;
print(w);


import math 
z = math.floor(3.5);
print(z);
w = math.floor(-2.5);
print(w);
x = math.floor(6.5);
print(x);

print(math.trunc(2.8));
print(math.trunc(-2.8));


# python ke pass number precision almost infinite hai.

print(9999999999999999999999+1);
print(2**20)

# complex numbers
print((2+1j)*3);

# octal base number 

# octal literal
print(0o20); 
# hexal literal
print(0xFF);
# binary literals 
print(0b1000);

print(oct(64));
# if i want to get the octal value of 64 then we can get in this way. 
print(int("64",8));


# bitwise operation -> you have to read about bitwise operation. 


import random 
print(random.random());

print(random.randint(1,10));

l1 = ["sumit","rahul","krishna","deshratna"];
print(random.choice(l1));
random.shuffle(l1);
print(l1);



# most important 

print(0.1+0.1+0.1);
print(0.1+0.1+0.1-0.3)

# in the second line we get 5.551115123125783e-17 but this is not true. to resolve this we can do this 
# decimal import context for detail.
from decimal import Decimal
print(Decimal('0.1')+Decimal("0.1")+Decimal("0.1")-Decimal("0.3"));

from fractions import Fraction
myFraction = Fraction(2,7);
print(myFraction);



# set in numbers
setone = {1,2,3,4};
print(setone & {1,3});


print(type(True))

# true == 1 and false == 0
print(True+4);

print(round(0.6));
print(round(0.5));
print(round(-0.5));