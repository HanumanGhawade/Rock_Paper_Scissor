import random

rock = '''                                88         
                                  88         
                                  88         
8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8   
88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"    
88         8b       d8 8b         8888[      
88         "8a,   ,a8" "8a,   ,aa 88`"Yba,   
88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a  

                                        '''

paper = '''
8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,  
88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8  
88       d8 ,adPPPPP88 88       d8 8PP""""""" 88          
88b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88          
88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88          
88                     88                                 
88                     88   '''
scissor = '''                                        

.d8888b  .d8888b888.d8888b .d8888b  .d88b. 888d888.d8888b  
88K     d88P"   88888K     88K     d88""88b888P"  88K      
"Y8888b.888     888"Y8888b."Y8888b.888  888888    "Y8888b. 
     X88Y88b.   888     X88     X88Y88..88P888         X88 
 88888P' "Y8888P888 88888P' 88888P' "Y88P" 888     88888P' 
'''
choice = int(input("what do you want choose ? type 0 for rock,1 for paper ,2 for scissor\n "))
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
else:
    print(scissor)
print("computer choice:")
comp_choice = random.randint(0, 2)
if comp_choice == 0:
    print(rock)
elif comp_choice == 1:
    print(paper)
else:
    print(scissor)
if choice == comp_choice:
    print("both are win")
elif choice == 0 and comp_choice == 2:
    print("You Win")
elif choice == 1 and comp_choice == 2:
    print(" You lose")
elif choice == 2 and comp_choice == 0:
    print("you lose")
elif choice == 0 and comp_choice == 1:
    print(" you lose")
elif choice == 1 and comp_choice == 0:
    print("you win")
elif choice == 2 and comp_choice == 1:
    print("you win")

