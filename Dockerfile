FROM python:3.11-alpine

COPY ./src/requirements.txt /code/requirements.txt
WORKDIR /code

RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir uvicorn && \
    pip install --no-cache-dir -r requirements.txt

COPY ./src/app /code/app

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]