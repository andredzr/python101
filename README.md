# python101


Este es un proyecto de ejemplo.


### Instrucciones:

- Clonar este repo
- Crear imagen de docker
```
    docker build -t <nombre-imagen> .
```
- Correr imagen en modo developer (salir con [CTRL] + [C])
```
docker run -it -p 5000:5000 --rm --name <nombre-del-contenedor> <nombre-imagen>
```
- Correr imagen en modo servicio
```
docker run -p 5000:5000 -d  --name <nombre-del-contenedor> <nombre-imagen>
```