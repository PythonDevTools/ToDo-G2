# ToDo Grupo 2

## Distribución de ramas
- **main**: producción
- **develop**: desarrollo


## Levantar el proyecto localmente
```py
# Clonar proyecto
git clone https://github.com/PythonDevTools/ToDo-G2.git
cd ToDo-G2

# Creación de entorno variable
>> python3 -m venv venv

# Activación en Windows
>> venv\Script\activate

# Activación en Linux
>> source venv/bin/activate

# Instalación de las librerías
>> pip install -r requirements.txt

# Levantamos el proyecto con Uvicorn
>> uvicorn main:app --reload
```

## Tests
```py
>> pytest
```
