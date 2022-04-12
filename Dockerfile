FROM python:3.9.12-slim-buster

WORKDIR /usr/src/app

COPY . .

RUN apt update && apt install tk -y

RUN python -m pip install galois

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]

