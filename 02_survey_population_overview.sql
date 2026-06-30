/* =====================================================
   02. SURVEY POPULATION OVERVIEW
   Objective: Understand respondent distribution by device, age, and creative.
===================================================== */

SELECT
    device,
    COUNT(*) AS respondents,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 2) AS percent_of_total
FROM survey_responses
GROUP BY device
ORDER BY respondents DESC;

SELECT
    age_group,
    COUNT(*) AS respondents
FROM survey_responses
GROUP BY age_group
ORDER BY age_group;

SELECT
    creative_type,
    COUNT(*) AS respondents
FROM survey_responses
GROUP BY creative_type
ORDER BY respondents DESC;
