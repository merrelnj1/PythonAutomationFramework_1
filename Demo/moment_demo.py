import moment

x = moment.now()
print(x)
x = moment.now().strftime("%H-%M-%S_%d-%m-%Y")
print(x)
