# Write code below 💖
print('Q1) Do you like Dawn or Dusk?')
print('1) Dawn')
print('2) Dusk')
user1 =int(input('   Answer: '))
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0
if user1 == 1:
  Gryffindor += 1
  Ravenclaw += 1
elif user1 == 2:
  Hufflepuff += 1
  Slytherin += 1
else:
  Print('Wrong Input!')
print('Q2) When Im dead, I want people to remember me as:')
print('1) The Good')
print('2) The Great')
print('3) The Wise')
print('4) The Bold')
user2 = int(input('   Answer: '))
if user2==1:
  Hufflepuff+=2
elif user2==2:
  Slytherin+= 2
elif user2 == 3:
  Ravenclaw+= 2
elif user2==4:
  Gryffindor+= 2
else:
  Print('Wrong Input!')
print('Q3) Which kind of instrument most pleases your ear?')
print('1) The violin')
print('2) The trumpet')
print('3) The piano')
print('4) The drum')
user3 = int(input('   Answer: '))
if user3 == 1:
  Hufflepuff += 4
elif user3 == 2:
  Slytherin += 4
elif user3 == 3:
  Ravenclaw+= 4 
elif user3 == 4:
  Gryffindor += 4
else:
  Print('Wrong Input!')
print('The house with the most points!')
highest = max(Gryffindor,Ravenclaw,Slytherin,Hufflepuff)
if Gryffindor == highest:
  print('Gryffindor')
elif Ravenclaw == highest:
  print('Ravenclaw')
elif Slytherin == highest:
  print('Slytherin')
elif Ravenclaw == highest:
  print('Hufflepuff')
else: 
  print('Equal') 
