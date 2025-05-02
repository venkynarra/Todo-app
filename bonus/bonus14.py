from bonus.parsers14 import parse

feet_inches = input("enter feet and inches :") # converting fee and inches into meters

# this program is decoupling the output.seperating responsibilities , we add def parse


def convert(feet, inches):

    meters = feet * 0.3048 + inches * 0.0254
    return meters

feet_inches_tuple = parse(feet_inches)
print("fi", feet_inches_tuple)
result = convert(feet_inches_tuple[0], feet_inches_tuple[1])


if result< 1:

    print("kid is too small")
else:
    print("kid can use the slide")