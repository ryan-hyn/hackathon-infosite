import math

sqft = int(input("enter the number of square feet: "))
MA_cost_per_sqft = sqft*333200
cost_per_sqft = MA_cost_per_sqft*43560
#cost_of_labor = pass
#cost_of_gc = pass
#cost_of_materials = pass
def hug():
    print("$"+str(round(cost_per_sqft,2))+" per square foot")
hug()