cleaning_rate = 60
cavity_filling_rate = 200
x_ray_rate = 100
tax_rate = 0.15
discount_rate_1 = 0.05
discount_rate_2 = 0.1

patient_name = input("Enter patient's name: ")
cleaning_performed = input("Was cleaning performed? (y/n): ")
cleaning_performed = input("Was cavity-filling performed? (y/n): ")
x_ray_performed = input("Was X-Ray performed? (y/n): ")

total_bill = 0
# Calculate the cost of each service
if cleaning_performed == 'y':
    total_bill += cleaning_rate
if cleaning_performed == 'y':
    total_bill += cavity_filling_rate
if x_ray_performed == 'y':
    total_bill += x_ray_rate 

# Check if the patient is eligible for a discount
if total_bill > 200:
    total_bill *= (1 - discount_rate_1)
if total_bill > 300:
    total_bill *= (1 - discount_rate_2)

# Calculate the tax
tax = total_bill * tax_rate

# Add the tax to the total bill
total_bill += tax

# Print the receipt
print("Melanie Dental Clinic")
print("Patient Name:", patient_name)
print("Cleaning performed:", cleaning_rate)
print("Cavity filling performed:", cavity_filling_rate)
print("X-Ray performed:", x_ray_rate )
print("Total Bill:", total_bill)
