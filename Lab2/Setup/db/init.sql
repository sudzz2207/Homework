CREATE TABLE outcome (    
    animal_id VARCHAR,
    animal_name VARCHAR,
    ts TIMESTAMP,
    dob DATE,
    outcome_type VARCHAR,
    outcome_subtype VARCHAR,
    animal_type VARCHAR,
    age VARCHAR,
    breed VARCHAR,
    color VARCHAR,
    month VARCHAR,
    year INT,
    sex VARCHAR
);

CREATE TABLE animal (
    animal_id VARCHAR(20) PRIMARY KEY,
    breed VARCHAR(20),
    color VARCHAR(20),
    name VARCHAR(20),
    dob DATE,
    animal_type VARCHAR(20)
);

CREATE TABLE outcome_type (
    outcome_subtype INT PRIMARY KEY,
    outcome_type VARCHAR(20)
);

CREATE TABLE outcomes (
    outcome_event_id INT PRIMARY KEY,
    datetime TIMESTAMP,
    sex VARCHAR(20),
    outcome_subtype VARCHAR(20),
    animal_id VARCHAR(20),
    outcome_subtype VARCHAR,
    FOREIGN KEY (animal_id) REFERENCES animal(animal_id),
    FOREIGN KEY (outcome_subtype) REFERENCES outcome_type(outcome_subtype)
);

CREATE TABLE fact_table (
    animal_id VARCHAR(20) NOT NULL,
    outcome_subtype VARCHAR,
    outcome_event_id INT,
    FOREIGN KEY (animal_id) REFERENCES animal(animal_id),
    FOREIGN KEY (outcome_subtype) REFERENCES outcome_type(outcome_subtype),
    FOREIGN KEY (outcome_event_id) REFERENCES outcome_events(outcome_event_id)    
);
