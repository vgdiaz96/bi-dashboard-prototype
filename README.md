# Prototipo de Dashboard de BI (Streamlit)

Este repositorio contiene un prototipo de dashboard de Inteligencia de Negocios (BI) desarrollado con **Python y Streamlit**, utilizando **pandas** para el manejo de datos y **Plotly** para visualizaciones interactivas.

## Estructura del Proyecto

- `DashboardApp/`
  - `app.py` (archivo principal de la aplicación)
  - `pages/` (pantallas del dashboard en modo multipágina)
  - `data_processor.py` (módulo para carga y procesamiento de datos)
  - `requirements.txt` (dependencias de Python)

## Requisitos Previos

- Python 3.10 o superior (recomendado 3.11)
- Git (opcional, solo si vas a clonar el repositorio)

---

## Instalación y Ejecución (Windows / macOS / Linux)

### 1) Clonar el repositorio

```bash
git clone https://github.com/vgdiaz96/bi-dashboard-prototype.git
cd bi-dashboard-prototype/DashboardApp
```

---

### 2) Crear y activar un entorno virtual

#### En Windows (PowerShell o CMD):

```bash
python -m venv dashboard-env
dashboard-env\Scripts\activate
```

Si el comando `python` no funciona en Windows, prueba:

```bash
py -m venv dashboard-env
dashboard-env\Scripts\activate
```

#### En macOS / Linux:

```bash
python3 -m venv dashboard-env
source dashboard-env/bin/activate
```

Cuando el entorno esté activado, deberías ver algo como:

```
(dashboard-env)
```

---

### 3) Instalar dependencias

```bash
pip install -r requirements.txt
```

---

### 4) Ejecutar la aplicación

```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador en:

```
http://localhost:8501
```

---

## Notas Importantes

- Este proyecto está desarrollado con Streamlit (no utiliza npm ni NodeJS).
- Si aparece un error relacionado con columnas o datos faltantes, revisa que el archivo de datos esperado por `data_processor.py` exista y tenga la estructura correcta.
- Asegúrate de ejecutar todos los comandos desde la carpeta `DashboardApp`.

