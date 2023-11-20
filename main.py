import os


if __name__ == "__main__":
    while True:
        # Esta linea limpia la consola, si no la quieres limpiar borrala
        # Igual con la linea 1 "import os"
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-----------------------------------------------")
        print("DNA-Toolkit v0.1")
        print("Please, select an option:")
        print("1 - Create new DNA chain")
        print("2 - Save DNA chain")
        print("3 - Load DNA from disk")
        print("4 - List all DNA info")
        print("5 - Delete DNA info")
        print("6 - Operations with DNA")
        print("7 - Exit")
        # Mete la logica del paso 3
        print("-----------------------------------------------")

        option = int(input("Please enter a number:"))
        
        match option:
            case 1:
                print("Option 1 - Create new DNA chain selected")
                # Aquí puedes agregar la lógica para crear una nueva cadena de ADN
            case 2:
                print("Option 2 - Save DNA chain selected")
                # Aquí puedes agregar la lógica para guardar la cadena de ADN
            case 3:
                print("Option 3 - Load DNA from disk selected")
                # Aquí puedes agregar la lógica para cargar la cadena de ADN desde el disco
            case 4:
                print("Option 4 - List all DNA info selected")
                # Aquí puedes agregar la lógica para listar toda la información de ADN
            case 5:
                print("Option 5 - Delete DNA info selected")
                # Aquí puedes agregar la lógica para eliminar la información de ADN
            case 6:
                print("Option 6 - Operations with DNA selected")
                # Aquí puedes agregar la lógica para realizar operaciones con la cadena de ADN
            case 7:
                print("Option 7 - Exit selected")
                # Aquí puedes agregar la lógica para salir del programa
                exit()
            case _:
                print("Invalid option. Please enter a valid number.")
