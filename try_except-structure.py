# From Coursera: https://www.coursera.org/learn/python
# Taught by: Charles Severance

# The try/except Structure

astr = 'Hello Bob'
try: # If the code in the try works, the expect is skipped
    istr = int(astr)
except: # If the code in the try fails, it jumps to the expect section
    istr = -1
print ('First', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print ('Second', istr)
