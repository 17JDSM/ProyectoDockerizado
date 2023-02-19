FROM python:3.10.10-alpine3.17 
# Definir imagen base

WORKDIR /app
# Especificar el directorio de trabajar en el contenedor

RUN apk update \
    && apk add --no-cache python3-dev \
    && pip install --upgrade pip
# 

COPY ./requirements.txt ./
# Copiar los archivos necesarios del proyecto al contenedor

RUN pip install -r requirements.txt
# Instalar dependencias

COPY ./ ./
# Agregar los archivos necesarios para ejecutar la aplicación dentro del contenedor de Docker.

EXPOSE 8000
# Expone el puerto para el servicio web

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
# Comando de inicio del contenedor
