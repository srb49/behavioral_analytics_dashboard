-- sql/schema.sql
CREATE TABLE IF NOT EXISTS user_analytics (
    customer_id VARCHAR(50) PRIMARY KEY,
    recency INTEGER,
    frequency INTEGER,
    monetary INTEGER,
    avg_order_value FLOAT,
    session_count INTEGER,
    avg_session_duration FLOAT,
    pages_viewed INTEGER,
    clicks INTEGER,
    campaign_response INTEGER,
    wishlist_adds INTEGER,
    cart_abandon_rate FLOAT,
    returns INTEGER,
    segment_label VARCHAR(50)
);