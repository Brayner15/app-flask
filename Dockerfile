FROM python:3.11-slim

# Copiar los requisitos
COPY ./src/requirements.txt /code/requirements.txt
WORKDIR /code

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    libssl-dev \
    libffi-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependencias de Python
RUN pip install --no-cache-dir --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación y los archivos de modelo
COPY ./src/app /code/app

# Exponer el puerto 80
EXPOSE 80

# Comando para ejecutar la aplicación
CMD ["python", "/code/app/main.py"]
