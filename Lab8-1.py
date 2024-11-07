import numpy as np
import matplotlib.pyplot as plt
from termcolor import colored


def mostrar_instrucciones():
    print(colored("\n--- Instrucciones de Uso ---", "cyan", attrs=["bold"]))
    print(
        "Este programa te permite graficar y comparar el crecimiento de dos términos."
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


def obtener_termino(prompt):
    # Función para solicitar un término hasta que el usuario ingrese algo válido
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


def plot_comparison(term1, term2):
    # Definir el rango de x
    x = np.linspace(1, 10000, 500)

    # Evaluar los términos utilizando eval
    try:
        y1 = eval(term1, {"x": x, "np": np})
        y2 = eval(term2, {"x": x, "np": np})
    except Exception as e:
        print(colored(f"Error al evaluar los términos: {e}", "red"))
        return

    # Crear el gráfico
    plt.figure(figsize=(12, 7))
    plt.plot(x, y1, label=f"Término 1: {term1}", color="dodgerblue", linewidth=2)
    plt.plot(x, y2, label=f"Término 2: {term2}", color="darkorange", linewidth=2)

    # Cambiar la escala del eje y a logarítmica para observar el crecimiento relativo
    plt.yscale("log")

    # Configuración del gráfico
    plt.xlabel("n", fontsize=12)
    plt.ylabel("Valor del término", fontsize=12)
    plt.title(
        "Comparación del crecimiento de dos términos",
        fontsize=16,
        color="purple",
        fontweight="bold",
    )
    plt.legend(fontsize=10)
    plt.grid(True, which="both", linestyle="--", linewidth=0.5, color="gray")
    plt.tight_layout()  # Ajusta el espaciado automáticamente para una visualización óptima

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
        print(colored("1. Ingresar y comparar dos términos", "green"))
        print(colored("2. Ver instrucciones de uso", "yellow"))
        print(colored("3. Salir", "red"))

        opcion = input(colored("Seleccione una opción: ", "cyan", attrs=["bold"]))

        if opcion == "1":
            # Solicitar al usuario los términos de la expresión
            term1 = obtener_termino(
                "Ingrese el primer término de la expresión en términos de x (ejemplo: '0.001 * x**3'): "
            )
            term2 = obtener_termino(
                "Ingrese el segundo término de la expresión en términos de x (ejemplo: '0.025 * x'): "
            )

            # Graficar los términos
            plot_comparison(term1, term2)

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
