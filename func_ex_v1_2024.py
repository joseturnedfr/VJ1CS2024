# Q: Programme a pay computation so that employees are offered 2.3x their fixed hourly wage for their working hours beyond 35 hours.
# Adapted from cond_ex_v1_2023.py but with added objective to define a function in the new codes

def payc(hours, rate):
    #print("In payc", hours, rate)
    # Case1 where hours > 35.0
    if hours > 35.0:
    payb = rate * hours
    paye = (hours - 35.0) * (rate * 0.5)
    payt = payb + paye
    # Case2 where hours <= 35.0
    else:
    payt = hours * rate
    #print("returning", payt)
    return payt

# set variables for hours and rates
ohr = input("Hours: ")
ort = input("Rates: ")
# Convert var from str to flt (vv depending on input)
try:
    fhr = float(ohr)
    frt = float(ort)
# consider the case where the user input is non-numeric
except:
    print("Error, please enter numeric input")
    quit()

# set variable for defined function
vpc = payc(fhr, frt)

# Calculate total pay
print("Pay:", vpc)
