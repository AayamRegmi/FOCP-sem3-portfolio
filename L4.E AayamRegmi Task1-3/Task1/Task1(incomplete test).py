#Beckett Pizza Plaza (BPP) 

def pizza_calc(npizza,delivery='n',tuesday='n', app='n'):
    
    '''Calculates the total price
       npizza:number of pizza
       delivery:home delivery flag
       tuesday:tuesday discount flag
       app:Order from app flag'''
    
    Avg_cost = 12.0 #Pizza cost
    delivery_cost=0
    price=(npizza*Avg_cost) 
   
    if delivery=='y':      #check if customer wants home delivery
        delivery_cost=2.5
        if npizza>=5:      #delivery charge 0 if pizzas is more than 4
            delivery_cost=0 
     

    if tuesday=='y': #check if it is tuesday
        price*=0.5    #apply discount if true 

    if app=='y':     #check if ordered from app
        price*=0.25

    price+=delivery_cost  #calculate final cost

    return round(price, 2)    #round off to 2 decimal place

#exception and error handling
def check_count(): 
    while True:
        try:
            npizza = int(input("How many pizzas ordered? "))
            if npizza < 0:
                raise ValueError("Number of pizzas should be a non-negative integer.")
            return npizza
        except ValueError:
            print("Error: Please provide a valid number for the number of pizzas.")

def check_deliv():
    while True:
        delivery = input("Is delivery required? ") 
        if delivery.lower() in ['y', 'n']:
            return delivery.lower()
        else:
            print("Error: Please provide 'y' or 'n' for the delivery option.")

def check_day():
    while True:
        tuesday = input("Is it Tuesday? ")
        if tuesday.lower() in ['y', 'n']:
            return tuesday.lower()
        else:
            print("Error: Please provide 'y' or 'n' for the Tuesday discount flag.")

def check_app():
    while True:
        app = input("Did the customer use the app? ")
        if app.lower() in ['y', 'n']:
            return app.lower()
        else:
            print("Error: Please provide 'y' or 'n' for the app flag.")

#Main calculator
print("BPP Pizza Price Calculator")
print("==========================")
# Main loop          
npizza = check_count()
delivery = check_deliv()
tuesday = check_day()
app = check_app()

bill = pizza_calc(npizza, delivery, tuesday, app)
print("Total Price: £", bill)

