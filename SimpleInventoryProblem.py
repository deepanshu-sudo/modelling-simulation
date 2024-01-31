from datetime import datetime, timedelta
from random import randint

# Define a function to generate demand
def generate_demand(lower_limit,upper_limit):
    # Demand in a day can be for any number of units between 0 and 99. Each equally probable.
    return randint(lower_limit,upper_limit)

# Define a function to simulate the inventory system
def simulate_inventory_system(reorder_point,reorder_qty,initial_stock,start_date,end_date):
    # Initialize the stock, units due, and total cost
    stock = initial_stock
    units_due = 0 
    total_cost = 0

    # Initialize the date and time
    current_date = start_date
    due_date = 0

    # Loop until the end date
    while current_date <= end_date:
        # If today is the due date, add the reorder qty to the current stock 
        if current_date == due_date:
            stock += reorder_qty
            units_due = 0

        # Generate Demand
        demand = generate_demand(0,99)

        # Check if demand is greater than stock
        if demand >= stock:
            # Add the shortage cost to the total cost
            total_cost += (stock * shortage_cost)
            # Set the stock to zero
            stock = 0
        else:
            # Reduce the stock by the demand
            stock -= demand
            # Add the carrying cost to the total cost
            total_cost += (stock * carrying_cost)

        # Check stock and place order if needed
        if stock + units_due <= reorder_point:
            units_due = reorder_qty
            total_cost += reorder_cost
            # There is a three day lag between order and arrival
            due_date = current_date + timedelta(days=3)

        # Increment the current date by one day
        current_date += timedelta(days=1)
    
    return total_cost


policies = [
    {"name": "Policy 1", "reorder_point": 125, "reorder_qty": 150},
    {"name": "Policy 2", "reorder_point": 125, "reorder_qty": 250},
    {"name": "Policy 3", "reorder_point": 150, "reorder_qty": 250},
    {"name": "Policy 4", "reorder_point": 175, "reorder_qty": 250},
    {"name": "Policy 5", "reorder_point": 175, "reorder_qty": 300}
]

# define the initial stock
initial_stock = 115

# define the costs
carrying_cost = 0.75
shortage_cost = 18
reorder_cost = 75

# Define the date and time
start_date = datetime.today()
end_date = start_date + timedelta(days=1000)

# Create an empty list to store the results
results = []

# Loop through the policies
for policy in policies:
    # Get the reorder point and reorder qty from the policy
    reorder_point = policy["reorder_point"]
    reorder_qty = policy["reorder_qty"]
    # Simulate the inventory system using the policy
    total_cost = simulate_inventory_system(reorder_point, reorder_qty, initial_stock, start_date, end_date)
    # Append the policy name and total cost to the results list
    results.append({"name": policy["name"], "total_cost": total_cost})

# sort the result by total cost in ascending order
results.sort(key=lambda x: x["total_cost"])

# print the results
for result in results:
    print(result["name"], "Total Cost: ",result["total_cost"])
