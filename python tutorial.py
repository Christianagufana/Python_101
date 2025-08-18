# variable = [string,float,interger,float,boolean]
# strings
First_name = ' bro'
food = ' pizza'
email= ' fake.me@gmail.com'
school= ' kenyatta university'
school1= ' ku'
company=' LG'
print(f'hello my name is{First_name}.')
print(f'I was admitted in{school} or better known as{school1}.')
print(f'I genuinely like{food}.')
print(f'my email is{email}')
print(f'I like it when it rains')
print (f'the company{company} makes fridges and electronics.') 
# integers
age=20
num_of_people=100
Quantity=4
print(f'I am {age} yrs old')
print(f'I want to eat {Quantity} samosas')
print(f'At school my class had atleast {num_of_people} students')
print(f'at{school1} I saw {Quantity} people.')
print(f'so am eating{food} at{school} my {Quantity} friends might come.')
# floatpoint
price = 200.50 
points = 4.6
distance = 5.5
print(f'the price of that is {price} ksh.')
print(f'I ran {distance} km')
print(f'At{school} I got {points} which means I passed ')
#boolean
is_student = False
if is_student:
    print('you are a student')
else:print('you are not student')
is_online = False
if is_online:
  print('You are online') 
else: print('You are offline')
is_open = True
if is_open:
   print('It is open')
else:
   print('it is not open')
is_posted = True
if is_posted:
   print('It is posted')
else:
   print('It is free')
is_for_sale = True 
if is_for_sale: 
   print('The property is for sale')
else: 
   print('This property is not for sale')
is_busy = True
if is_busy:
   print('Working')
else: print('Is free')
I_am = True
if I_am:
   print('Budhaa is present') 
else:
   print('Budhaa is lost')
# typecasting = the process of converting a variable from one data type to another
name = 'Khristos'
Year = 2005
Gpa = 4.0 

print(type(name))
print(type(Year))
print(type(Gpa))
print(type(is_online))
 
Gpa = int(Gpa)
print(Gpa)