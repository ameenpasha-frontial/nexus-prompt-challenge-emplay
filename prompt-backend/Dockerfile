FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# COPY ALL PROJECT FILES including backend/ folder
COPY . .

# run collectstatic (not required if you don't use Django static)
RUN python manage.py collectstatic --noinput || true

CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000"]
