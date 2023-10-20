import pandas as pd
import psycopg2
from sqlalchemy import create_engine

def extract_data(source):
    return pd.read_csv("https://shelterdata.s3.amazonaws.com/shelter1000.csv")

def transform_data(data):
    print('Transforming data...')

    data_new = data.copy()
    data_new.fillna('Not Recorded', inplace=True)
    data_new.columns = [col.lower() for col in data_new.columns]

    animal_columns = ['animal_id', 'breed', 'color', 'animal_name', 'animal_type', 'dob']
    outcomes_columns = ['outcomes', 'datetime', 'sex', 'outcome_subtype', 'animal_id', 'outcome_subtype']
    fact_table_columns = ['outcomes', 'outcome_subtype', 'animal_id']

    data_new['outcomes'] = data_new.index + 1

    animal = data_new[animal_columns].drop_duplicates('animal_id', keep='first').reset_index(drop=True)
    unique_sex = data_new[['outcome_type']].drop_duplicates().reset_index(drop=True)
    unique_sex['outcome_subtype'] = unique_sex.index + 1
    sex = unique_sex[['outcome_subtype', 'outcome_type']]

    outcome_subtype_map = dict(zip(unique_sex['outcome_type'], unique_sex['outcome_subtype']))
    data_new['outcome_subtype'] = data_new['outcome_type'].map(outcome_subtype_map)

    outcomes = data_new[outcomes_columns]

    outcomes.reset_index(drop=True, inplace=True)

    fact_table = data_new[fact_table_columns]

    print('Data Transformed')
    return fact_table, animal, outcome_type, outcomes

def load_data(transformed_data):
    print('Loading data...')

    fact_table, animal, outcome_type, outcomes = transformed_data

    DATABASE_URL = "postgresql+psycopg2://sudha:asdf1234@0.0.0.0:5432/shelter"

    engine = create_engine(DATABASE_URL)

    animal.to_sql('animal', engine, if_exists='append', index=False)
    sex.to_sql('sex', engine, if_exists='append', index=False)
    outcomes.to_sql('outcomes', engine, if_exists='append', index=False)
    fact_table.to_sql('fact_table', engine, if_exists='append', index=False)

    print('Data Loading Completed')

if __name__ == '__main__':
    extracted_data = extract_data()
    
    transformed_data = transform_data(extracted_data)
    
    load_data(transformed_data)
