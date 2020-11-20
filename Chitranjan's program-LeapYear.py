a= input("Enter A Year:")
if(a%4==0):
 if(a%100==0):
  if(a%400==0):
   print a,'is a leap year'
  else: print 'Not a leap year'
 else: print 'Not a leap year' 
else: print 'Not a leap year'
