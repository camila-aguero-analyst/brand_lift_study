/* =====================================================
   05. CAMPAIGN DRIVERS
   Business Question: Which campaign elements drove stronger ad recall?
===================================================== */

SELECT
    creative_type,
    ROUND(100.0 * SUM(CASE WHEN ad_recall = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 1) AS ad_recall_rate
FROM survey_responses
WHERE exposed_group = 'Exposed'
GROUP BY creative_type
ORDER BY ad_recall_rate DESC;

SELECT
    device,
    ROUND(100.0 * SUM(CASE WHEN ad_recall = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 1) AS ad_recall_rate
FROM survey_responses
GROUP BY device
ORDER BY ad_recall_rate DESC;

SELECT
    frequency_bucket,
    ROUND(100.0 * SUM(CASE WHEN ad_recall = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 1) AS ad_recall_rate
FROM survey_responses
GROUP BY frequency_bucket
ORDER BY ad_recall_rate DESC;
