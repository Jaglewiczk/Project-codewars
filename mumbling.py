s = "jkbnsjdbvkjkjsndk"

def accum(s):
    app_list = []
    for count, letter in enumerate(s):
        app_list.append(letter.upper() + letter.lower()*(count))
    return "-".join(app_list)

print(accum(s))

