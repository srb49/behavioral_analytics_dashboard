-- sql/kpi_queries.sql

-- 1. High Value User Identification (using Checkpoint 1: RFM)
-- Purpose: Find users who spend a lot and visit often.
WITH UserScores AS (
    SELECT 
        Customer_ID,
        Monetary,
        Frequency,
        (Monetary * Frequency) AS Loyalty_Score
    FROM user_analytics
)
SELECT * FROM UserScores 
WHERE Loyalty_Score > (SELECT AVG(Loyalty_Score) FROM UserScores)
ORDER BY Loyalty_Score DESC;

-- 2. Engagement vs. Conversion Analysis
-- Purpose: See if longer sessions actually lead to more spending.
SELECT 
    CASE 
        WHEN Avg_Session_Duration < 5 THEN 'Short (0-5m)'
        WHEN Avg_Session_Duration BETWEEN 5 AND 15 THEN 'Medium (5-15m)'
        ELSE 'Long (15m+)' 
    END AS Session_Category,
    COUNT(*) as User_Count,
    AVG(Monetary) as Avg_Revenue
FROM user_analytics
GROUP BY 1;

-- 3. Campaign Effectiveness by Segment
-- Purpose: Which segments respond best to marketing?
SELECT 
    Segment_Label,
    SUM(Campaign_Response) as Total_Responses,
    CAST(SUM(Campaign_Response) AS FLOAT) / COUNT(*) as Response_Rate
FROM user_analytics
GROUP BY Segment_Label
ORDER BY Response_Rate DESC;