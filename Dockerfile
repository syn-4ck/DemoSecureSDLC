FROM python:latest

RUN useradd -g users demo

COPY . /code

RUN pip install -r requirements.txt

USER demo

CMD ["/bin/sh"]