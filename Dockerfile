FROM python:3.9.12-buster

WORKDIR /usr/src/app

COPY . .

RUN ls

RUN python -m pip install galois

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]

