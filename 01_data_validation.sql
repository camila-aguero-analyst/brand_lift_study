/* =====================================================
   01. DATA VALIDATION
   Objective: Confirm the dataset size and review the survey population.
===================================================== */

SELECT COUNT(*) AS total_respondents
FROM survey_responses;

SELECT
    exposed_group,
    COUNT(*) AS respondents,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 2) AS percent_of_total
FROM survey_responses
GROUP BY exposed_group;
