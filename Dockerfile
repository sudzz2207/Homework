FROM python:3.11
WORKDIR /app
COPY Testcervicalcancer.py Testcervicalcancer.py
COPY cervical-cancer_csv.csv cervical-cancer_csv.csv
COPY processed_cervicalcancer.csv processed_cervicalcancer.csv
RUN pip install pandas
RUN Testcervicalcancer.py cervical-cancer_csv.csv processed_cervicalcancer.csv
ENTRYPOINT ["bash"]