# Alex Serrano

## Lo de flash se trabajo dentro de la misma carpeta consumo_api

# taller13

## Creación de Servicio Web y Consumo vía Flask

### Revisar
- Ejemplo de servicios web con Django y Django-Rest [ejemplos]
- Ejemplo de consumo de servicios web desde flask [consumo-api]

### Ejemplos

* Usando requests (librería de python)

```

# GET
import requests
r = requests.get("http://127.0.0.1:8000/api/estudiantes/", auth=('user', 'passs'))
r.content

# POST
r = requests.post('http://127.0.0.1:8000/api/numerost/', data = {'estudiante':'http://127.0.0.1:8000/api/estudiantes/12/', 'telefono':'99999999', 'tipo'='principal' }, auth=('user', 'pass'))
print(r)

# PUT
r = requests.put('http://127.0.0.1:8000/api/numerost/26', data = {'estudiante':'http://127.0.0.1:8000/api/estudiantes/13/', 'telefono':'99999999', 'tipo':'principal' }, auth=('user', 'pass'))
print(r)

# DELETE
r = requests.delete('http://127.0.0.1:8000/api/numerost/26/', auth=('user', 'pass'))
print(r)
```


### Problemática

Dadas dos entidades:

* Edificio:
	* nombre
	* dirección
	* ciudad
	* tipo [residencial, comercial]

* Departamento
	* nombre completo del propietario
	* costo del departamento
	* número de cuartos
	* edificio

Nota: Un departamento pertenece a un edificio

### Tecnologías y herramientas:

- Base de datos Sqlite / Postgres (agregar en el readme, evidencias de las tablas en ambas BD)
  <img width="1913" height="1008" alt="pos_sql" src="https://github.com/user-attachments/assets/2abc5d1a-08b9-4bae-8798-2e5e585664c0" />
  <img width="1920" height="1080" alt="tablapoblada" src="https://github.com/user-attachments/assets/7f52adcd-5ff2-441d-b448-c5a02e261bd3" />
  <img width="1920" height="1080" alt="tablapoblada2" src="https://github.com/user-attachments/assets/392fb244-87a6-458e-bf60-20669f93ab1b" />


- Lenguaje Python
- Framework Django
- Django-Rest
- Flask
<img width="1913" height="1008" alt="Funcionamiento" src="https://github.com/user-attachments/assets/e02dd9a9-e6c7-48d3-bbb1-4c0fa2044e5f" />
<img width="1653" height="777" alt="funcionamientodelapideflask" src="https://github.com/user-attachments/assets/720f3683-ab8a-48e7-8aaf-0f2a6a58c5de" />
<img width="1913" height="1008" alt="sqlite" src="https://github.com/user-attachments/assets/36377cab-defd-43fd-b4d6-381028ab1052" />





### Tarea a realizar:

- Crear un proyecto de Django.
- Crear una aplicación en el proyecto en Django.
- Generar el modelo de la aplicación usando las entidades descritas.
- Activar la interfaz de administración de la aplicación de Django.
- A través de views/template presentar un menú para listar en tablas: Edificios, Departamentos (usar el template adjunto)
- Agregar servicios web que permitan lista; crear; actualizar y eliminar entidades (todas deben tener acceso con token)
- Crear una aplicación en Flask que permita:
	-	Listar Edificios haciendo uso de los servicios web creados en el proyecto de Django
	- Listar Departamentos haciendo uso de los servicios web creados en el proyecto de Django.
	- Crear Edificios haciendo uso de los servicios web creados en el proyecto de Django.
	- Crear Departamentos haciendo uso de los servicios web creados en el proyecto de Django.
