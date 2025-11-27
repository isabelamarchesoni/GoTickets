ARG PYTHON_VERSION=3.12-slim

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code

WORKDIR /code

COPY requirements.txt /tmp/requirements.txt
# Certifique-se de que 'gunicorn' está no requirements.txt (veja o item 3)
RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/
COPY . /code

ENV SECRET_KEY "Hqxab29Xkm5igsQiVTFv40LOMDLSslOmJfNH1puXpnSGmy2P3a"
RUN python manage.py collectstatic --noinput

EXPOSE 8000

# Usando Gunicorn para servir a aplicação WSGI na porta 8000
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]