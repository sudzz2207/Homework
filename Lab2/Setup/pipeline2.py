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
    outcome_event_columns = ['outcome', 'datetime', 'sex', 'outcome_subtype', 'animal_id', 'outcome_subtype']
    fact_table_columns = ['outcome', 'outcome_subtype', 'animal_id']

    data_new['outcome'] = data_new.index + 1

    animal = data_new[animal_columns].drop_duplicates('animal_id', keep='first').reset_index(drop=True)
    unique_outcome_type = data_new[['outcome_type']].drop_duplicates().reset_index(drop=True)
    unique_outcome_type['outcome_subtype'] = unique_outcome_type.index + 1
    outcome_type = unique_outcome_type[['outcome_subtype', 'outcome_type']]

    outcome_subtype_map = dict(zip(unique_outcome_type['outcome_type'], unique_outcome_type['outcome_subtype']))
    data_new['outcome_subtype'] = data_new['outcome_type'].map(outcome_subtype_map)

    outcome_events = data_new[outcome_event_columns]

    outcome_events.reset_index(drop=True, inplace=True)

    fact_table = data_new[fact_table_columns]

    print('Data Transformed')
    return fact_table, animal, outcome_type, outcome_events

def load_data(transformed_data):
    print('Loading data...')

    fact_table, animal, outcome_type, outcome_events = transformed_data

    DATABASE_URL = "postgresql+psycopg2://sriram:ABCabc12345$@db:5432/shelter_hw"

    engine = create_engine(DATABASE_URL)

    animal.to_sql('animal', engine, if_exists='append', index=False)
    outcome_type.to_sql('outcome_type', engine, if_exists='append', index=False)
    outcome_events.to_sql('outcome_events', engine, if_exists='append', index=False)
    fact_table.to_sql('fact_table', engine, if_exists='append', index=False)

    print('Data Loading Completed')

if __name__ == '__main__':
    extracted_data = extract_data()
    
    transformed_data = transform_data(extracted_data)
    
    load_data(transformed_data)
