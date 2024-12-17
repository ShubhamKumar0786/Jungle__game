
print( 'JUNGLE GAME ')
print('')

def start():
     print('''          GAME START
           
 The car has traveled 700 km, and there are two routes ahead.
           
           press 1 for left
           press 2 for right''')
     print('')
start()

def joy():
     q=int(input('''
                 press 1 game continue
                  press 2 for exit
                 enter number :'''))
     print('')
     if(q==1):
          start()
     if(q==1):
          game()
     elif(q==2):
          print('--------THANKS FOR PLAY GAME---------')
          


def game():
     x=int(input('enter number :'))
     print('')
     if(x==1):
         z=int(input(''' 
The car has traveled 40 km, and there are two routes ahead.
                
                press 1 for left
                press 2 for right
                enter number :'''))
         print('')
         if(z==1):
              print('THE BIG RIVER____GAME OVER_____')
              joy()
         elif(z==2):
              print('ANIMALS____GAME OVER_____')
              joy()

     elif(x==2):
          d=int(input('''
 The car has traveled 35 km, and there are two routes ahead.

                      press 1 for left
                      prees 2 for right
                      enter number :'''))
          if(d==1):
               v=int(input(''' 

The car has traveled 55 km, and there are two routes ahead. There is a stranger ahead
                      
                           press 1 for help
                           press 2 for don't help
                           enter number :'''))
               print('')
               if(v==1):
                    print('----YOU ARE WIN-------')
                    joy()
               elif(v==2):
                    print('BIG OCEAN______GAME OVER____')
                    joy()
          elif(d==2):
               print('ANIMAL TRAPS____GAME OVER_____')
               joy()

game()