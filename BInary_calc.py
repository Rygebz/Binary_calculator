def convert(base, x):
    print(f"{base.capitalize()} value is:")
    print(eval(f"{base}(x)"))

options = {
    'bin': lambda x: convert('bin', x),
    'oct': lambda x: convert('oct', x),
    'hex': lambda x: convert('hex', x)
}

while True:
    choice = input("Enter Choice (bin/oct/hex): ")
    if choice in options:
        x = int(input("Enter decimal value: "))
        options[choice](x)
    else:
        print("Invalid choice. Please choose bin, oct, or hex.")
