# Build step #2: build the API with the client as static files
FROM python:3.8.16-alpine
WORKDIR /app

RUN mkdir ./api
COPY ./ ./api
RUN pip install --upgrade pip && \
    pip install -r ./api/requirements.txt

WORKDIR /app/api
EXPOSE 5000
#CMD ["gunicorn", "-b", ":5000", "api:app"]
CMD python3 db.py
CMD python3 main.py

