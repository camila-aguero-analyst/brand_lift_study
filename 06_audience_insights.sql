/* =====================================================
   06. AUDIENCE INSIGHTS
   Business Question: Which audience segments responded most positively?
===================================================== */

SELECT
    age_group,
    ROUND(100.0 * SUM(CASE WHEN ad_recall = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 1) AS ad_recall_rate,
    ROUND(100.0 * SUM(CASE WHEN brand_awareness = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 1) AS brand_awareness_rate,
    ROUND(100.0 * SUM(CASE WHEN brand_favorability = 'Favorable' THEN 1 ELSE 0 END) / COUNT(*), 1) AS favorability_rate,
    ROUND(100.0 * SUM(CASE WHEN purchase_intent = 'Likely' THEN 1 ELSE 0 END) / COUNT(*), 1) AS purchase_intent_rate
FROM survey_responses
GROUP BY age_group
ORDER BY age_group;

SELECT
    gender,
    ROUND(100.0 * SUM(CASE WHEN purchase_intent = 'Likely' THEN 1 ELSE 0 END) / COUNT(*), 1) AS purchase_intent_rate
FROM survey_responses
GROUP BY gender
ORDER BY purchase_intent_rate DESC;

SELECT
    region,
    ROUND(100.0 * SUM(CASE WHEN brand_awareness = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 1) AS brand_awareness_rate
FROM survey_responses
GROUP BY region
ORDER BY brand_awareness_rate DESC;
