# 23680049_CALCULADORA_TAP

## GUIA COMPLETA: Creación de una interfaz interactiva con Flet

Esta guia te enseñara paso a paso como diseñar una aplicación con Python y el framework Flet. Conoceremos a configurar tu entorno, diseñar un display dinámico y programar botones con estatica moderna para escribir números o limpiar la pantalla. 

## 1. Configuración del entorno de trabajo

Antes de comenzar a programar, es necesario dejar listas las herramientas fundamentales: el intérprete de Python, el framework Flet y una terminal funcional como Git Bash.

### Instalación de Python

Descarga Python desde el sitio oficial. Durante el proceso de instalación, activa la opción “Add Python to PATH”. Para comprobar que la instalación fue exitosa, abre la terminal y ejecuta el siguiente comando:
```
python --version 
# o si usas el lanzador de Python:
py --version
```
### Configuración de Git Bash

Debido a que la consola CMD puede quedarse corta con ciertos comandos más avanzados, utilizaremos Git Bash como alternativa. Durante su instalación, solo debes avanzar con el asistente presionando “Next” en cada paso. Al abrirlo, notarás una ventana parecida a la terminal de Linux, con colores que ayudan a identificar fácilmente las rutas y directorios.

## 2. Inicio del proyecto y creación del entorno virtual

Es recomendable generar un entorno virtual independiente para cada proyecto, ya que esto ayuda a prevenir choques entre dependencias y versiones de librerías.

Dirígete al Escritorio y crea una nueva carpeta:

```
cd Desktop
mkdir tap
cd tap
```

Genera y activa el entorno virtual:Al ejecutar este comando, se creará una carpeta llamada .venv con los archivos necesarios para aislar tu instalación de Flet.

```
python -m venv .venv
# Para activar el entorno en Git Bash:
source .venv/Scripts/activate
```

## 3. Instalación de Flet

Con el entorno activo (verás el prefijo (.venv) en la terminal), instalamos la librería:

```
pip install 'flet[all]'
```

Para verificar que todo salió bien y ver la versión de Flet obtenida, usa:

```
flet doctor
```

Para iniciar un proyecto base rápidamente, puedes usar flet create ., que generará una interfaz con un contador básico para probar que el motor gráfico funciona.

### 4. Construcción de la Calculadora TAP

Abre Visual Studio Code, selecciona tu carpeta tap y crea tu archivo main.py.

### Estructura Inicial y Configuración de Pantalla

Lo primero es importar la librería y definir la función principal. Determinamos un tamaño compacto de ventana para que luzca como una aplicación móvil.

```
import flet as ft 

def main(page: ft.Page):
    page.title = "Calculadora TAP"
    page.window_width = 250   # Ancho ajustado
    page.window_height = 450  # Alto ajustado
    page.padding = 20
```

### El Display (Pantalla de Visualización)

El display es un ft.Container que hereda propiedades de estilo de Flet. En este caso, usamos WHITE_60, un blanco con 60% de opacidad para un look moderno.

```
display = ft.Container(
        content=ft.Text("0", size=30),
        bgcolor=ft.Colors.WHITE_60,
        border_radius=8,
        alignment=ft.alignment.Alignment(1, 0), # Texto alineado a la derecha
        padding=10, 
        width=210, 
        height=70,
    )
```

### Organización mediante GridView

Usaremos un ft.GridView para ordenar los botones en una rejilla. Configuramos runs_count=3 para definir tres columnas.

```
grid = ft.GridView(
        runs_count=3,     # Tres columnas de botones
        spacing=10,       # Espacio entre botones
        run_spacing=10,   # Espacio entre filas
        width=210, 
        height=200, 
        expand=True
    )
```

## 5. Lógica de Programación (Funciones)
