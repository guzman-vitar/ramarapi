# Ramarapi

*La api de Ramaro, un líder técnico diferente*

## Levantarla desde dockerhub

```shell
docker run -p 8888:8888 morgoth137/ramarapi-conda
```

## La api misma

Para ver su especificación entrar al endpoint `<ip>/docs`

### Registro, logueo y autorización

Para acceder a la api se precisa registrar un usuario y loguearse para realizar las requests.

#### Registro

Es en `<ip>/docs#/Fans/create_fan_fans_registro_post`.

Se le da `Try it out` y se reemplazan los campos `usuario`, `email` y `contraseña`:

![Registranding](/docs/registro.png "Registro")

Se le da `execute` y si todo va bien devuelve un código 200:

![](/docs/registro_answer.png)

#### Logueo

Con el usuario y la contraseña generados se ponen en `<ip>/docs#/Login/login_login_login_post`:

![](/docs/login_request.png)

Esta request devuelve un `token` que hay que usar para autorizarse, entonces copiátelo por favor.

![](/docs/login_answer.png)

#### Autorizacion

Con el token en el portapapeles dirigirse arriba al botón de `Authorize`, pegarlo clickear en `authorize` y luego `close`:

![](/docs/authorize_token.png)

Y con eso ya se puede acceder a toda la api hasta que expire el token y haya que reautorizarse (solo con `login`, no hay que registrarse de nuevo).



## Desarrollo Local

*Asegurarse de tener instalado [docker](https://docs.docker.com/engine/install/)*

Construir la imagen del [Dockerfile](/docker/Dockerfile):

```shell
docker build -f docker/Dockerfile
```

Levantar la imagen:

```shell
docker run -p 8888:8888 <imagen>
```

