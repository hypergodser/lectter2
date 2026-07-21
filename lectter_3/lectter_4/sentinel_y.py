
keep = 'y'


while keep == 'y':
 
    cost = float(input("Enter the item's wholesale cost: "))
    

    retail_price = wholesale_cost * 2.5
    
   
    print(f"Retail price: ${retail_price:.2f}")
    
   
    keep = input("Do you have another item? (Enter y for yes): ")

keep = ''