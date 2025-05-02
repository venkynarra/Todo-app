feet_inches = input("enter feet and inches :") # converting fee and inches into meters

# this program is decoupling the output.
def convert(feet_inches):
    parts = feet_inches.split('.')
    feet = float(parts[0])
    inches = float(parts[1])

    meters = feet * 0.3048 + inches * 0.0254
    return meters

meters = convert(feet_inches)


if meters < 1:

    print("kid is too small")
else:
    print("kid can use the slide")