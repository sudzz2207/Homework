FROM python:3.11

WORKDIR /app
# COPY pipeline.py pipeline.py
COPY . /app
RUN pip install pandas sqlalchemy psycopg2
ENTRYPOINT [ "python", "pipeline.py", "processed_data.csv" ]