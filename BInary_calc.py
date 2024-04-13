op = 1
chr(op)

def convert_and_prompt(base, x):
    print(f"{base.capitalize()} value is:")
    print(eval(f"{base}(x)"))

options = {
    'bin': lambda x: convert_and_prompt('bin', x),
    'oct': lambda x: convert_and_prompt('oct', x),
    'hex': lambda x: convert_and_prompt('hex', x)
}

while True:
    choice = input("Enter Choice (bin/oct/hex): ")
    if choice in options:
        x = int(input("Enter decimal value: "))
        options[choice](x)
    else:
        print("Invalid choice. Please choose bin, oct, or hex.")
