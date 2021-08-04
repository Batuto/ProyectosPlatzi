import random


def generar_contrasena():
    characters = tuple((chr(i) for i in range(33,127)))
    # Create a tuple of characters from ! to ~ with the aid of a generator.
    password = ""
    while len(password) < 15:  # The lenght of the password is fixed.
        password += random.choice(characters)  # Append a random character.
    return password


def main():
    new_password = generar_contrasena()
    print(f"Tu nueva contraseña es: {new_password}")


if __name__ == '__main__':
    main()
