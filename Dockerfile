FROM python:latest

RUN useradd -g users demo

COPY . /code

RUN pip install -r /src/requirements.txt

USER demo

CMD ["/bin/sh"]
