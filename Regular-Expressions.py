# Notes from: https://www.dr-chuck.net/pythonlearn/slides/EN_us/Py4Inf-11-Regex.pdf

# Regular Expressions

import re
#--------------------------------------------------------------------------
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x) # [0-9]+ means one or more digits
                           #  + means repeats a character one or more times 

print (y) # ['2', '19', '42']

y = re.findall('[0-9]+',x)
print (y) # ['2', '1', '9', '4', '2']

#---------------------------------------------------------------------------
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+@\S+',x)
print (y) # ['stephen.marquard@uct.ac.za']
y = re.findall('^From.*?(\S+@\S+)',x) 
print (y) # ['stephen.marquard@uct.ac.za']
y = re.findall('^From (\S+@\S+)',x)
print (y) # ['stephen.marquard@uct.ac.za']

#---------------------------------------------------------------------------
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# find 'uct.ac.za'
# (1)
atpos = data.find('@')
print (atpos) # 21
sppos = data.find(' ',atpos)
print (sppos) # 31
host = data[atpos+1 : sppos]
print (host)  # uct.ac.za
# (2)
words = data.split() # ['From', 'stephen.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008']
email = words[1]
pieces = email.split('@')
print (pieces[1]) # # uct.ac.za
# (3)
import re
lin = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('@([^ ]*)',lin)
print (y)

y = re.findall('^From .*@([^ ]*)',lin)
print (y) 
