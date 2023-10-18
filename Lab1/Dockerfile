FROM python:3.11
WORKDIR /app
copy Testcervicalcancer.py Testcervicalcancer.py
copy cervical-cancer_csv.csv cervical-cancer_csv.csv
copy processed_cervicalcancer.csv processed_cervicalcancer.csv
RUN pip install pandas
RUN Testcervicalcancer.py cervical-cancer_csv.csv processed_cervicalcancer.csv
ENTRYPOINT ["bash"]