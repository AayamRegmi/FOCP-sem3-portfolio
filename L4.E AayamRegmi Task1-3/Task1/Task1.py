def pizza_calc(npizza, delivery='n', tuesday='n', app='n'): 
    '''Takes in input number of pizza, delivery option, tuesday or not, and app purchase or not and returns the total bill'''
    
    avg_cost, delivery_cost = 12.0, 0 #standard values
    price = npizza * avg_cost
    
    #checks if y or n options to add charge or add discount to purchase
    if delivery == 'y':
        delivery_cost = 2.5 if npizza < 5 else 0

    if tuesday == 'y':
        price *= 0.5

    if app == 'y':
        price *= 0.75

    return round(price + delivery_cost, 2)

def get_input(prompt, options=['y', 'n']): #handles any error for delivery tuesday and app while the program is running
    '''Takes in prompt and checks if option is yes or no'''

    while True:
        user_input = input(prompt).lower()
        if user_input in options:
            return user_input
        print("Please answer 'Y' or 'N'.")


more=False


while True:
    print("BPP Pizza Price Calculator")
    print("==========================\n")

    # Check count 
    npizza = 0
    while npizza <= 0: #asks for number of pizza until valid postive value is given
        try:
            npizza = int(input("How many pizzas ordered? "))
            if npizza <= 0:
                print("Number of pizzas should be a positive integer.")
        except ValueError:
            print("Please provide a valid number for the number of pizzas.")

    delivery = get_input("Is delivery required? ")
    tuesday = get_input("Is it Tuesday? ")
    app = get_input("Did the customer use the app? ")

    bill = pizza_calc(npizza, delivery, tuesday, app)
    print(f"Total Price: £{bill}")

    more=get_input("calculate next order?")
    if more=='n':
        break