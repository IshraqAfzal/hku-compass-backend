FROM --platform=linux/amd64 python:3.9-alpine

ENV PYTHONUNBUFFERED 1
ENV PATH="/scripts:${PATH}"

WORKDIR /code

COPY ./app/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app/ /code/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8081"]