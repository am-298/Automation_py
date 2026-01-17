# this checks whether the password is strong or not

import re

a  = input ("Enter your password : ")

if re.match(r'(^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&*])[A-Za-z\d@#$%^&*]{8,}$)',a) is not None:
    print ('Strong Password')
else:
    print ('Weak Password')
    