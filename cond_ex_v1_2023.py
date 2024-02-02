# Q: Programme a pay computation so that employees are offered 2.3x their fixed hourly wage for their working hours beyond 35 hours.

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

# Case1 where fhr > 35.0
if fhr > 35.0:
    bp = frt * fhr
    ep = (fhr - 35.0) * (frt * 0.5)
    tp = bp + ep
# Case2 where fhr <= 35.0
else:
    tp = fhr * frt
# Calculate total pay
print("Pay:", tp)
