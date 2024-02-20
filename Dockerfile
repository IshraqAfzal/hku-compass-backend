FROM --platform=linux/amd64 python:3.9-alpine

WORKDIR /build

COPY ./requirements.txt /build/requirements.txt

RUN pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /build/requirements.txt

COPY ./app/ /build/

EXPOSE 8081

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8081"]