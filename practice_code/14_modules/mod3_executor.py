
# case 01-------------------------
#from mod3_1 import *
#from mod3_2 import var1

#print(var1)

#case 02--------------------------
#import mod3_1
#import mod3_2

#print(mod3_1.var1, mod3_2.var1)

arg = '29'

if arg == '2':
	from mod3_2 import var1
else:
	from mod3_1 import var1

print(var1)
