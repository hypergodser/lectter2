
keep_going = 'y'


while keep_going == 'y':
 
    wholesale_cost = float(input("Enter the item's wholesale cost: "))
    

    retail_price = wholesale_cost * 2.5
    
   
    print(f"Retail price: ${retail_price:.2f}")
    
   
    keep_going = input("Do you have another item? (Enter y for yes): ")

keep_power = ''