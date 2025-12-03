import random
data=[]
print('WELCOME SIR/MAM')
print('HOW ARE YOU ')
print('1...code/2...decode')
while True:
 n1=int(input('Enter here....'))
 if n1==1:
  w=input('Enter your words...')
  print(w)
  if len(w)<=3:
      print(n1[::-1])
  else:
   a='abcdefghijklmopqrstuvwxyzABCDEFGHIJKLMOPQRSTUVWXYZ'
   for i in range(3):
      h=(random.choice(a))
      s=(''.__add__(h))
      print(s)
   b='abcdefghijklmopqrstuvwxyzABCDEFGHIJKLMOPQRSTUVWXYZ'
   for i in range(3):
      h1=(random.choice(b))
      s1=(h1)
 print(s+w+s1)
 if n1==2:
     w=input('Enter Code..')
     if len(w)<=3:
         print(n1[::-1])
     else:
        p=w[3:]
        x=p[:-3]
        print(x)
