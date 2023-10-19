--1
SELECT animal_type, COUNT(DISTINCT animal_id) AS animal_count
FROM animal
GROUP BY animal_type;

--2
SELECT COUNT(DISTINCT animal_id) AS "Animals with more than 1 Outcome"
FROM outcome
GROUP BY animal_id
HAVING COUNT(*) > 1;

--3
SELECT
    TO_CHAR(datetime, 'Month') AS month_name,
    COUNT(*) AS month_count
FROM outcome
GROUP BY TO_CHAR(datetime, 'Month')
ORDER BY month DESC
LIMIT 5;

--4
SELECT
    age_category,
    COUNT(*) AS count
FROM (
    SELECT
        CASE
            WHEN age_in_years < 1 THEN 'Kitten'
            WHEN age_in_years > 10 THEN 'Senior Cat'
            ELSE 'Adult'
        END AS age
    FROM (
        SELECT
            a.animal_type,
            DATE_PART('year', AGE(o.datetime, a.date_of_birth)) AS age_in_years
        FROM
            animal AS a
            JOIN outcomes AS o ON a.animal_id = o.animal_id
            JOIN outcome_type AS ot ON ot.outcome_type_id = o.outcome_type_id
        WHERE
            ot.outcome_type = 'Adopted' AND a.animal_type = 'Cat'
    )
) AS age_categories
GROUP BY age_category;

--5.
SELECT
    date(datetime) AS "Date",
    COUNT(*) AS "Daily Outcomes",
    SUM(COUNT(*)) OVER (ORDER BY date(datetime)) AS "Cumulative Total Outcomes"
FROM outcomes
GROUP BY date(datetime)
ORDER BY date(datetime);
