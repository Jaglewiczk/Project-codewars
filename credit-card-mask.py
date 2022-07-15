cc = "9823643897268347268476"

def maskify(cc):
    number_or_string = ""
    if len(cc) > 4:
        number_or_string += "#" * (len(cc) - 4) + cc[-4:]
    else:
        return cc
    return number_or_string

print(maskify(cc))