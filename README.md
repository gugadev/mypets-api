<h1 align="center">Pets API</h1>

<p align="center">
  <img
    src="https://i.imgur.com/DkHuWRa.jpg"
    height="256"
    width="256"
    style="border-radius: 100%"
  />
</p>

<p align="center">Código fuente del tutorial <a href="https://goo.gl/DA5k36">"Creando una API con Sanic y Records"</a></p>

---

## Preparación

Antes de empezar, es necesario preparar el entorno usando [pipenv](). Para esto, necesitamos instalar las dependencias:

```bash
pipenv install
```

Una vez hecho esto ya podemos acceder al entorno virtual:

```bash
pipenv shell
```

## Generar base de datos

Por defecto, la aplicación usa SQLite (en caso se use otro motor, actualizar el archivo *config/db.json* e instalar el driver correspondiente). Por tal razón, es necesario generar la base de datos con el siguiente comando:

```bash
records --url=sqlite:///pets.db 'sql/create.sql'
```
