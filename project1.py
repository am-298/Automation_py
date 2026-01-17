import re

filepath = "" #write your file path

pattern = re.compile(r'(?:\d{3}-\d{3}-\d{4})|(?:\d{10})|(?:\d{5}-\d{5})|(?:\+\d{2}-\d{5}-\d{5})')
pattern2 = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+[\.a-z{2,4}]')
with open(filepath,'r') as file:
    data = file.read()
    result= pattern.findall(data)
    email= pattern2.findall(data)

for i in result:
    print("Phone Number : ", i)

for j in email:
    print("Email Address : ", j)
    