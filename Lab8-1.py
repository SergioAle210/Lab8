import numpy as np
import matplotlib.pyplot as plt
from termcolor import colored


def mostrar_instrucciones():
    print(colored("\n--- Instrucciones de Uso ---", "cyan", attrs=["bold"]))
    print(
        "Este programa te permite graficar y comparar el crecimiento de múltiples términos."
    )
    print(
        "Puedes ingresar términos como polinomios, exponenciales y logaritmos con diferentes bases."
    )
    print(colored("Ejemplos de términos válidos:", "yellow"))
    print(colored("  - Polinomios:", "green"), "'0.001 * x**3', '0.025 * x'")
    print(colored("  - Exponenciales:", "green"), "'2**x', '1.5**x'")
    print(colored("  - Logaritmos:", "green"))
    print("      - Base natural:", colored("'np.log(x)'", "yellow"))
    print(
        "      - Otra base:",
        colored("'np.log(x) / np.log(base)'", "yellow"),
        "(por ejemplo, base 2 es 'np.log(x) / np.log(2)')",
    )
    print(
        "Puedes configurar el rango máximo de x y la escala de los ejes x e y en el menú principal."
    )
    print(
        "Además, puedes cargar funciones desde el archivo 'terminos_dom.txt' para graficarlas directamente.\n"
    )


def mostrar_configuracion_actual(max_x, escala_x, escala_y, max_y):
    print(colored("\n--- Configuración Actual ---", "cyan", attrs=["bold"]))
    print(colored(f"Rango máximo de x: {max_x}", "yellow"))
    print(colored(f"Escala del eje x: {escala_x}", "yellow"))
    print(colored(f"Escala del eje y: {escala_y}", "yellow"))
    print(colored(f"Rango máximo de y (si está definido): {max_y}", "yellow"))


def obtener_numero_funciones():
    while True:
        try:
            num = int(
                input(
                    colored(
                        "¿Cuántas funciones quieres comparar? (Ejemplo: 2, 3, 4, etc.): ",
                        "yellow",
                    )
                )
            )
            if num > 0:
                return num
            else:
                print(colored("Por favor, ingresa un número positivo.", "red"))
        except ValueError:
            print(colored("Entrada no válida. Ingresa un número entero.", "red"))


def obtener_termino(prompt):
    while True:
        termino = input(colored(prompt, "yellow"))
        if termino.strip():  # Verifica si no está vacío o solo tiene espacios
            return termino
        else:
            print(
                colored(
                    "Error: El término no puede estar vacío. Inténtalo de nuevo.", "red"
                )
            )


def cargar_terminos_desde_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as file:
            terms = [line.strip() for line in file if line.strip()]
            print(
                colored(
                    f"{len(terms)} términos cargados desde '{nombre_archivo}'", "green"
                )
            )
            return terms
    except FileNotFoundError:
        print(colored(f"Error: No se encontró el archivo '{nombre_archivo}'.", "red"))
        return []


def obtener_rango_x():
    while True:
        try:
            max_x = float(
                input(
                    colored(
                        "Ingrese el valor máximo para x (Ejemplo: 10000, 100000000): ",
                        "yellow",
                    )
                )
            )
            if max_x > 0:
                return max_x
            else:
                print(
                    colored(
                        "Por favor, ingresa un valor positivo para el rango de x.",
                        "red",
                    )
                )
        except ValueError:
            print(colored("Entrada no válida. Ingresa un número.", "red"))


def obtener_rango_y():
    while True:
        try:
            max_y = float(
                input(
                    colored(
                        "Ingrese el valor máximo para y o deja en blanco para automático: ",
                        "yellow",
                    )
                )
                or "inf"
            )
            if max_y > 0 or max_y == float("inf"):
                return max_y
            else:
                print(
                    colored(
                        "Por favor, ingresa un valor positivo para el rango de y.",
                        "red",
                    )
                )
        except ValueError:
            print(colored("Entrada no válida. Ingresa un número.", "red"))


def seleccionar_escala_eje(eje):
    while True:
        escala = (
            input(
                colored(
                    f"Seleccione la escala para el eje {eje} ('linear' o 'log'): ",
                    "yellow",
                )
            )
            .strip()
            .lower()
        )
        if escala in ["linear", "log"]:
            return escala
        else:
            print(
                colored(
                    "Entrada no válida. Por favor, ingrese 'linear' o 'log'.", "red"
                )
            )


def seleccionar_archivo():
    while True:
        print(
            colored(
                "\nSeleccione el archivo para cargar los términos:",
                "cyan",
                attrs=["bold"],
            )
        )
        print(colored("1. terminos_dom.txt", "yellow"))
        print(colored("2. terminos_dom_ordenados.txt", "yellow"))
        opcion = input(colored("Seleccione una opción (1 o 2): ", "cyan"))

        if opcion == "1":
            return "terminos_dom.txt"
        elif opcion == "2":
            return "terminos_dom_ordenados.txt"
        else:
            print(colored("Opción no válida. Por favor, seleccione 1 o 2.", "red"))


def plot_comparison(terms, max_x, escala_x, escala_y, max_y):
    # Definir el rango de x con el valor máximo seleccionado por el usuario
    x = np.linspace(1, max_x, 500)
    colors = [
        "dodgerblue",
        "darkorange",
        "forestgreen",
        "crimson",
        "purple",
        "brown",
        "teal",
        "gold",
        "slateblue",
        "tomato",
        "olive",
        "indigo",
    ]

    # Crear el gráfico
    plt.figure(figsize=(12, 7))

    # Evaluar y graficar cada término
    for i, term in enumerate(terms):
        try:
            y = eval(term, {"x": x, "np": np})
            plt.plot(
                x,
                y,
                label=f"Término {i + 1}: {term}",
                color=colors[i % len(colors)],
                linewidth=2,
            )
        except Exception as e:
            print(colored(f"Error al evaluar el término '{term}': {e}", "red"))
            return

    # Configurar las escalas de los ejes
    plt.xscale(escala_x)
    plt.yscale(escala_y)

    # Aplicar límite al eje y si se definió un máximo
    if max_y != float("inf"):
        plt.ylim(top=max_y)

    # Configuración del gráfico
    plt.xlabel("n", fontsize=12)
    plt.ylabel("Valor del término", fontsize=12)
    plt.title(
        "Comparación del crecimiento de múltiples términos",
        fontsize=16,
        color="purple",
        fontweight="bold",
    )
    plt.legend(fontsize=10)
    plt.grid(True, which="both", linestyle="--", linewidth=0.5, color="gray")
    plt.tight_layout()

    # Mostrar el gráfico
    plt.show()


def menu():
    print(
        colored(
            "¡Bienvenido al Comparador de Crecimiento de Términos!",
            "magenta",
            attrs=["bold"],
        )
    )
    mostrar_instrucciones()

    # Valores por defecto
    max_x = 1000000000
    escala_x = "linear"
    escala_y = "log"
    max_y = float("inf")  # Sin límite máximo para y por defecto

    while True:
        print(colored("\n--- Menú Principal ---", "cyan", attrs=["bold"]))
        print(colored("1. Configurar rango máximo de x", "blue"))
        print(colored("2. Configurar escala del eje x", "blue"))
        print(colored("3. Configurar escala del eje y", "blue"))
        print(colored("4. Configurar rango máximo de y", "blue"))
        print(colored("5. Ingresar y comparar términos", "green"))
        print(colored("6. Cargar términos desde archivo", "green"))
        print(colored("7. Ver instrucciones de uso", "yellow"))
        print(colored("8. Salir", "red"))

        opcion = input(colored("Seleccione una opción: ", "cyan", attrs=["bold"]))

        if opcion == "1":
            max_x = obtener_rango_x()

        elif opcion == "2":
            escala_x = seleccionar_escala_eje("x")

        elif opcion == "3":
            escala_y = seleccionar_escala_eje("y")

        elif opcion == "4":
            max_y = obtener_rango_y()

        elif opcion == "5":
            # Mostrar configuración actual antes de graficar
            mostrar_configuracion_actual(max_x, escala_x, escala_y, max_y)

            # Solicitar el número de funciones a comparar
            num_funciones = obtener_numero_funciones()

            # Solicitar cada término
            terms = []
            for i in range(num_funciones):
                term = obtener_termino(
                    f"Ingrese el término {i + 1} en términos de x (ejemplo: '0.001 * x**3'): "
                )
                terms.append(term)

            # Graficar los términos con la configuración seleccionada
            plot_comparison(terms, max_x, escala_x, escala_y, max_y)

        elif opcion == "6":
            # Seleccionar el archivo a cargar
            archivo = seleccionar_archivo()
            terms = cargar_terminos_desde_archivo(archivo)
            if terms:
                mostrar_configuracion_actual(max_x, escala_x, escala_y, max_y)
                plot_comparison(terms, max_x, escala_x, escala_y, max_y)

        elif opcion == "7":
            mostrar_instrucciones()

        elif opcion == "8":
            print(
                colored(
                    "Saliendo del programa. ¡Hasta pronto!", "magenta", attrs=["bold"]
                )
            )
            break

        else:
            print(
                colored(
                    "Opción no válida. Por favor, seleccione una opción del menú.",
                    "red",
                )
            )


# Ejecutar el programa
menu()
