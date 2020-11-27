import random 
print("Welcome to the 'Rock' , 'Paper' , 'Scissor' Game.")
print("Only 10 attempts")
print("type 'r' for Rock\ntype 'p' for paper\ntype 's' for scissor ")
r = "Rock"
p = "Paper"
s = "Scissor"
values = ["r","p","s"]
your_score = 0
computer_score = 0
attempts = 0
while (attempts<=10):
   value = str(input("Choose 'Rock' , 'Paper' or 'Scissor' : "))
   value = value.lower()
   computer = random.choice(values)

   if value == 'r' and computer == 's':
        print(f"You win\nYou : {r} and computer : {s}") 
        your_score = your_score+1  
        print("Your Score : ",your_score)
        print("Computer Score : ",computer_score)
        attempts = attempts+1
     
   elif value == 'r' and computer == 'p':
        print(f"Computer win\nYou : {r} and computer : {p}") 
        computer_score = computer_score+1  
        print("Your Score : ",your_score)
        print("Computer Score : ",computer_score)
        attempts = attempts+1

   elif value == 'r' and computer == 'r':
        print(f"Tie\nYou : {r} and computer : {r}")   
        print("Your Score : ",your_score)
        print("Computer Score : ",computer_score)
        attempts = attempts+1
    
   elif value == 'p' and computer == 'r':
        print(f"You Win \nYou : {p} and computer : {r}") 
        your_score = your_score+1   
        print("Your Score : ",your_score)
        print("Computer Score : ",computer_score)
        attempts = attempts+1

   elif value == 'p' and computer == 's':
        print(f"Computer Win \nYou : {p} and computer : {s}")
        computer_score = computer_score+1  
           
        print("Your Score : ",your_score)
        print("Computer Score : ",computer_score)
        attempts = attempts+1

   elif value == 'p' and computer == 'p':
        print(f"Tie \nYou : {p} and computer : {p}")   
        print("Your Score : ",your_score)
        print("Computer Score : ",computer_score)
        attempts = attempts+1

   elif value == 's' and computer == 'r':
        print(f"Computer Win \nYou : {s} and computer : {r}") 
        computer_score = computer_score+1  
          
        print("Your Score : ",your_score)
        print("Computer Score : ",computer_score)
        attempts = attempts+1

    
   elif value == 's' and computer == 'p':
        print(f"You Win \nYou : {s} and computer : {p}") 
        your_score = your_score+1   
        print("Your Score : ",your_score)
        print("Computer Score : ",computer_score)
        attempts = attempts+1

    
    
   elif value == 's' and computer == 's':
        print(f"Tie \nYou : {s} and computer : {s}")   
        print("Your Score : ",your_score)
        print("Computer Score : ",computer_score)
        attempts = attempts+1


   else :
       print("Invalid Input")
       print("Your Score : ",your_score)
       print("Computer Score : ",computer_score)
       attempts = attempts+1
       
       
       
       break
print("attempts over")
print(f"Your Score : {your_score}\nComputer Score : {computer_score}")

    
       

    
        

        
     
    
    

    

