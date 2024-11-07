# Comparador de Crecimiento de Términos

Este programa en Python permite graficar y comparar el crecimiento de diferentes términos matemáticos, como polinomios, exponenciales y logaritmos. Está diseñado para ayudar a visualizar cómo crecen diferentes funciones en comparación entre sí, utilizando escalas lineales y logarítmicas.

## Características

- Comparación de términos matemáticos personalizados ingresados por el usuario.
- Carga de términos desde archivos de texto (`terminos_dom.txt` o `terminos_dom_ordenados.txt`).
- Configuración personalizada del rango de valores en el eje \( x \).
- Opciones de escalas lineales o logarítmicas en los ejes \( x \) y \( y \).
- Límite opcional para el rango de valores en el eje \( y \).

## Requisitos

Este programa requiere:

- Python 3.x
- Las bibliotecas `numpy`, `matplotlib` y `termcolor`

### Instalación de Dependencias

Para instalar las dependencias necesarias, puedes utilizar `pip`:

```bash
pip install numpy matplotlib termcolor
```

### Ejecución

Para ejecutar el programa, utiliza el siguiente comando en la terminal:

```bash
python lab8-1.py
```

## Uso del Programa

Al ejecutar el programa, se mostrará un menú interactivo con las siguientes opciones:

### Menú Principal

1. **Configurar rango máximo de x**:

- Permite establecer el valor máximo para el eje x, controlando el rango de valores que se graficarán en el eje horizontal.

2. **Configurar escala del eje x**:

- Permite seleccionar la escala para el eje x: `linear` (lineal) o `log` (logarítmica). Esta configuración es útil para visualizar más claramente los términos de crecimiento rápido.

3. **Configurar escala del eje y**:

- Permite seleccionar la escala para el eje y: `linear` o `log`. Usar una escala logarítmica puede ayudar a comparar términos con crecimiento muy diferente.

4. **Configurar rango máximo de y**:

- Permite establecer un valor máximo para el eje y. Esto es útil para limitar los valores altos en el eje y y hacer que las funciones con crecimiento más lento sean visibles.

5. **Ingresar y comparar términos**:

- Permite al usuario ingresar manualmente los términos a comparar en términos de x. Se puede ingresar una cantidad personalizada de términos y cada uno será graficado con la configuración actual.

6. **Cargar términos desde archivo**:

- Esta opción muestra un submenú donde el usuario puede elegir cargar términos desde uno de los dos archivos:
  - `terminos_dom.txt`: archivo con una lista de términos para comparar.
  - `terminos_dom_ordenados.txt`: archivo alternativo con otra lista de términos.
- El programa leerá los términos del archivo seleccionado y los graficará utilizando la configuración actual.

7. **Ver instrucciones de uso**:

- Muestra una breve explicación de cómo usar el programa y ejemplos de términos válidos.

8. **Salir**:

- Sale del programa.

### Ejemplos de Términos Válidos

A continuación, algunos ejemplos de términos matemáticos que puedes ingresar o encontrar en los archivos:

- Polinomios: `0.001 * x**3`, `0.025 * x`
- Exponenciales: `2**x`, `1.5**x`
- Logaritmos:
  - Base natural: `np.log(x)`
  - Otra base: `np.log(x) / np.log(2)` (logaritmo en base 2)

## Archivos de Términos

### `terminos_dom.txt`

Este archivo contiene una lista de términos matemáticos que pueden ser graficados directamente sin tener que ingresarlos manualmente. Los términos deben estar separados por líneas.

### `terminos_dom_ordenados.txt`

Este archivo contiene otra lista de términos, organizados de manera diferente a `terminos_dom.txt`. Puedes seleccionar este archivo si deseas comparar los términos en este orden alternativo.

## Ejemplo de Uso

1. **Ejecutar el programa**:

```bash
python lab8-1.py
```

2. **Configurar el Rango de x**:
   Selecciona la opción `1` en el menú para establecer un valor máximo para el eje x (por ejemplo, `10000`).

3. **Seleccionar Escala del Eje y**:
   Selecciona la opción `3` para elegir la escala logarítmica (`log`) o lineal (`linear`) para el eje y.

4. **Cargar Términos desde Archivo**:
   Selecciona la opción `6` y elige entre `terminos_dom.txt` y `terminos_dom_ordenados.txt`.

5. **Graficar**:
   Observa cómo crecen los términos comparados en la gráfica.

## Notas

- **Errores en la Evaluación**: Si se produce un error al evaluar un término (por ejemplo, por un término mal escrito), el programa mostrará un mensaje de error y te pedirá ingresar el término nuevamente.
- **Formato de los Términos**: Asegúrate de ingresar los términos en un formato que Python pueda interpretar. Utiliza `np.log(x)` para logaritmos y `x**2` para potencias, por ejemplo.
