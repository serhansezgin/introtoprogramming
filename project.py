import sys

brokoli = int(10)
ginger = int(10)
cucumber = int(5)
tomatoes = int(6)
banana = int(20)
nutella = int (50)
haselnuts = int (40)

apple = int(3)
cherry = int(3)
strawberry = int(3)
pear = int(2)
peach = int(3)
orange = int(5)

egg = int(20)
meat = int(25)
milk = int(30)
chicken = int(20)

def race_type_by_entered_number(a):
        
        if questions == 1:
            marathon = "semi"
            needed_km = int(5000)
            needed_calories = int(30000)
        elif questions == 2:
            marathon = "regular"
            needed_km = int(10000)
            needed_calories = int(60000)
        elif questions == 3:
            marathon = "ultra"
            needed_km = 40000
            needed_calories = int(240000)      
        else:
            print ("You must enter a number 1 and 3")    

        return print ("You selected", marathon, "marathon. \nYou will run",needed_km, "km at the race", "\nYou need", needed_calories, "calories for preparations" ) 



def daily_plan(b):
    
    if questions == 1:
        needed_calories = int(30000)
        planned_workouts = int(300)
        planned_duration = int(30)
        print("Based on your selection type:\nYour planned workouts", planned_workouts, "hours","\nYour planned duration:", planned_duration,"days")
        if diet_type == 1:
            vegetables_to_eat =   ginger + cucumber + tomatoes  + brokoli 
            fruits_to_eat = banana + orange + strawberry + apple + pear + peach + cherry
            return print("Your gained calories from eating daily:", vegetables_to_eat+fruits_to_eat)
        if diet_type == 2:
            vegetables_to_eat =   ginger + cucumber + tomatoes  + brokoli 
            fruits_to_eat = banana + orange + strawberry + apple + pear + peach + cherry
            proteins_to_eat = egg + meat + chicken + milk
            return print("Your gained calories from eating daily:", vegetables_to_eat+fruits_to_eat+proteins_to_eat)

    elif questions == 2:
        needed_calories = int(60000)
        planned_workouts = int(600)
        planned_duration = int(60)
        print("Based on your selection type:\nYour planned workouts", planned_workouts, "hours","\nYour planned duration:", planned_duration,"days")
        if diet_type == 1:
            vegetables_to_eat =   2*ginger + 2*cucumber + 2*tomatoes  + 2*brokoli 
            fruits_to_eat = 2*banana + 2*orange + 2*strawberry + 2*apple + 2*pear + 2*peach + 2*cherry
            return print("Your gained calories from eating daily:", vegetables_to_eat+fruits_to_eat)

        if diet_type == 2:
            vegetables_to_eat =   2*ginger + 2*cucumber + 2*tomatoes  + 2*brokoli 
            fruits_to_eat = 2*banana + 2*orange + 2*strawberry + 2*apple + 2*pear + 2*peach + 2*cherry
            proteins_to_eat = 2*egg + 2*meat + 2*chicken + 2*milk
            return print("Your gained calories from eating daily:", vegetables_to_eat+fruits_to_eat+proteins_to_eat)

    elif questions == 3:
        needed_calories = int(240000)      
        planned_workouts = int(1800)
        planned_duration = int(180)
        print("Based on your selection type:\nYour planned workouts", planned_workouts, "hours","\nYour planned duration:", planned_duration,"days")
        if diet_type == 1:
            vegetables_to_eat =   2*ginger + 2*cucumber + 2*tomatoes  + 2*brokoli 
            fruits_to_eat = 2*banana + 2*orange + 2*strawberry + 2*apple + 2*pear + 2*peach + 2*cherry
            return print("Your gained calories from eating daily:", vegetables_to_eat+fruits_to_eat)
        if diet_type == 2:
            vegetables_to_eat =   2*ginger + 2*cucumber + 2*tomatoes  + 2*brokoli 
            fruits_to_eat = 2*banana + 2*orange + 2*strawberry + 2*apple + 2*pear + 2*peach + 2*cherry
            proteins_to_eat = 2*egg + 2*meat + 2*chicken + 2*milk
            return print("Your gained calories from eating daily:", vegetables_to_eat+fruits_to_eat+proteins_to_eat)

    





 
try:

    questions = int(input("Please input which marathon type do you want to prepare: \n1 for semi marathon. \n2 for regular marathon. \n3 for ultra marathon. \nYour selection for marathon type: "))
    diet_type = int(input("Please input which diet type do you want to select: \n1 for fruits and vegetables. \n2 for fruits, vegetables and animal based foods.\nYour selection for diet: "))


    for i in range (1,3):
        if questions == i:
            print("You entered", i)
        
        elif i >= 4:
            print("you must enter a number between 1 and 3")
            sys.exit()

    for i in range (1,2):
                if diet_type == i:
                    print("You entered", i)
                elif i >= 3:
                    print("you must enter a number between 1 and 2")
                    break  



    def main():                  
        race_type_by_entered_number(i)
        daily_plan(i)     

    main()    


except:
        print("You must enter a number between 1 and 3")

    
    


          









    

    

    
     
    
    


