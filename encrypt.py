Alphabet='abcdefghijklmnopqrstuvwxyz'
def ShiftAlpha(key):
   if key>=len(Alphabet):
     print('INVALID KEY HIGHER THAN 24!!')
   else:
     return Alphabet[key:]+Alphabet[:key]
def encryptMessage(Shift,message):
    Output=''
    for x in message:
      current_Char=Shift.find(x.lower())
      if not current_Char==-1:
         if x.islower():
            Output+=Alphabet[current_Char]
         else:
             Output+=Alphabet[current_Char].upper()
      else:
          Output+=x
    return Output
message=input('Enter the line you want to encrypt:')
key=int(input('Enter the key encryption:'))
Shifted=ShiftAlpha(key)
print(Shifted)
print(encryptMessage(Shifted,message))