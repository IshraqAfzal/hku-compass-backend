FROM python:3.9

ENV PIP_ROOT_USER_ACTION=ignore

WORKDIR /build

COPY ./requirements.txt /build/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /build/requirements.txt

COPY ./app /build/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]