/* =====================================================
   03. BRAND LIFT MEASUREMENT
   Business Question: Did campaign exposure improve key brand metrics?
===================================================== */

SELECT
    exposed_group,
    COUNT(*) AS respondents,
    ROUND(100.0 * SUM(CASE WHEN ad_recall = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 2) AS ad_recall_rate,
    ROUND(100.0 * SUM(CASE WHEN brand_awareness = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 2) AS brand_awareness_rate,
    ROUND(100.0 * SUM(CASE WHEN brand_favorability = 'Favorable' THEN 1 ELSE 0 END) / COUNT(*), 2) AS favorability_rate,
    ROUND(100.0 * SUM(CASE WHEN purchase_intent = 'Likely' THEN 1 ELSE 0 END) / COUNT(*), 2) AS purchase_intent_rate
FROM survey_responses
GROUP BY exposed_group;
