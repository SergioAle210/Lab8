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
        "Para cambiar el rango de x, modifica los valores en la línea de 'np.linspace' dentro del código.\n"
    )


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


def plot_comparison(terms):
    # Definir el rango de x
    x = np.linspace(1, 10000, 500)
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

    # Cambiar la escala del eje y a logarítmica para observar el crecimiento relativo
    plt.yscale("log")

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

    while True:
        print(colored("\n--- Menú Principal ---", "cyan", attrs=["bold"]))
        print(colored("1. Ingresar y comparar términos", "green"))
        print(colored("2. Ver instrucciones de uso", "yellow"))
        print(colored("3. Salir", "red"))

        opcion = input(colored("Seleccione una opción: ", "cyan", attrs=["bold"]))

        if opcion == "1":
            # Solicitar el número de funciones a comparar
            num_funciones = obtener_numero_funciones()

            # Solicitar cada término
            terms = []
            for i in range(num_funciones):
                term = obtener_termino(
                    f"Ingrese el término {i + 1} en términos de x (ejemplo: '0.001 * x**3'): "
                )
                terms.append(term)

            # Graficar los términos
            plot_comparison(terms)

        elif opcion == "2":
            mostrar_instrucciones()

        elif opcion == "3":
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
