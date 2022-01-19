# create the initial variables below
age = 28
sex=0
bmi=26.2
num_of_children=3
smoker=0

# Add insurance estimate formula below
insurance_cost= 250 * age - 128 * sex + 370 *bmi + 425 * num_of_children + 2400 * smoker - 12500
print("This person's insurance cost is "+ str(insurance_cost) + "dollars.")

# Age Factor
age += 4

new_insurance_cost= 250 * age - 128 * sex + 370 *bmi + 425 * num_of_children + 2400 * smoker - 12500

change_in_insurance_cost= new_insurance_cost - insurance_cost

print ("The change in cost of insurance after increasing the age by 4 years is " + str(change_in_insurance_cost) +" dollars")

# BMI Factor
age=28 #reset value to focus on BMI changes
bmi += 3.1

new_insurance_cost= 250 * age - 128 * sex + 370 *bmi + 425 * num_of_children + 2400 * smoker - 12500

change_in_insurance_cost= new_insurance_cost - insurance_cost

print ("The change in cost of insurance after increasing BMI by 3.1 is " + str(change_in_insurance_cost) +" dollars")

# Male vs. Female Factor
bmi=26.2 #reset to focus on sex

sex=1

new_insurance_cost= 250 * age - 128 * sex + 370 *bmi + 425 * num_of_children + 2400 * smoker - 12500

change_in_insurance_cost= new_insurance_cost - insurance_cost

print ("The change in estimated cost for being male instead of female is  " + str(change_in_insurance_cost) +" dollars")

# Extra Practice kids
sex= 0 #reset to focus on num of children

num_of_children= 0

new_insurance_cost= 250 * age - 128 * sex + 370 *bmi + 425 * num_of_children + 2400 * smoker - 12500

change_in_insurance_cost= new_insurance_cost - insurance_cost

print ("The change in estimated cost for having no children is  " + str(change_in_insurance_cost) +" dollars")

# Extra Practice smoke

num_of_children= 3 #reset to focus on smoking

smoker=1

new_insurance_cost= 250 * age - 128 * sex + 370 *bmi + 425 * num_of_children + 2400 * smoker - 12500

change_in_insurance_cost= new_insurance_cost - insurance_cost

print ("The change in estimated cost for smoking is " + str(change_in_insurance_cost) +" dollars")