FROM python:3.10

WORKDIR /code

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# CMD [ "celery", "-A", "food_stories", "worker", "--beat", "--scheduler", "django", "--loglevel=info", ]