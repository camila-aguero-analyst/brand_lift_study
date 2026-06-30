/* =====================================================
   04. BRAND LIFT CALCULATION
   Objective: Calculate exposed minus control lift in percentage points.
===================================================== */

WITH metrics AS (
    SELECT
        exposed_group,
        100.0 * SUM(CASE WHEN ad_recall = 'Yes' THEN 1 ELSE 0 END) / COUNT(*) AS ad_recall_rate,
        100.0 * SUM(CASE WHEN brand_awareness = 'Yes' THEN 1 ELSE 0 END) / COUNT(*) AS brand_awareness_rate,
        100.0 * SUM(CASE WHEN brand_favorability = 'Favorable' THEN 1 ELSE 0 END) / COUNT(*) AS favorability_rate,
        100.0 * SUM(CASE WHEN purchase_intent = 'Likely' THEN 1 ELSE 0 END) / COUNT(*) AS purchase_intent_rate
    FROM survey_responses
    GROUP BY exposed_group
)

SELECT
    ROUND(MAX(CASE WHEN exposed_group = 'Exposed' THEN ad_recall_rate END)
        - MAX(CASE WHEN exposed_group = 'Control' THEN ad_recall_rate END), 1) AS ad_recall_lift_pts,

    ROUND(MAX(CASE WHEN exposed_group = 'Exposed' THEN brand_awareness_rate END)
        - MAX(CASE WHEN exposed_group = 'Control' THEN brand_awareness_rate END), 1) AS brand_awareness_lift_pts,

    ROUND(MAX(CASE WHEN exposed_group = 'Exposed' THEN favorability_rate END)
        - MAX(CASE WHEN exposed_group = 'Control' THEN favorability_rate END), 1) AS favorability_lift_pts,

    ROUND(MAX(CASE WHEN exposed_group = 'Exposed' THEN purchase_intent_rate END)
        - MAX(CASE WHEN exposed_group = 'Control' THEN purchase_intent_rate END), 1) AS purchase_intent_lift_pts
FROM metrics;
