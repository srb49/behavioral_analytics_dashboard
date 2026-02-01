import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

st.set_page_config(page_title="Behavioral Analytics Dashboard", layout="wide")

def get_data(query):
    conn = sqlite3.connect('data/analytics.db')
    # Use chunksize or direct read
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

st.title("📈 Behavioral Analytics Dashboard")

# --- DEBUGGING STEP ---
# Let's see what the columns actually are
check_df = get_data("SELECT * FROM user_analytics LIMIT 1")
# st.write(check_df.columns.tolist()) # Uncomment this to see columns on the web app

try:
    # --- SIDEBAR FILTERS ---
    st.sidebar.header("Filter Data")
    
    # Get unique segments
    segments_df = get_data("SELECT DISTINCT Segment_Label FROM user_analytics")
    
    # Using the first column found regardless of exact casing
    col_name = segments_df.columns[0] 
    segments = segments_df[col_name].unique().tolist()
    
    selected_segment = st.sidebar.multiselect("Select Segments", options=segments, default=segments)

    # --- QUERYING FILTERED DATA ---
    # We use tuple formatting for the SQL IN clause
    if not selected_segment:
        st.error("Please select at least one segment.")
    else:
        # Create a safe string for the IN clause: ('Segment1', 'Segment2')
        segment_list_str = str(tuple(selected_segment)) if len(selected_segment) > 1 else f"('{selected_segment[0]}')"
        
        # Build the query without backslashes inside the f-string
        query = f"SELECT * FROM user_analytics WHERE {col_name} IN {segment_list_str}"
        
        df_filtered = get_data(query)

        # --- KEY METRICS ---
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Users", len(df_filtered))
        with col2:
            # We use .get() to avoid KeyErrors if the case is slightly different
            monetary_col = 'Monetary' if 'Monetary' in df_filtered.columns else 'monetary'
            st.metric("Avg Monetary", f"${df_filtered[monetary_col].mean():.2f}")
        with col3:
            pages_col = 'Pages_Viewed' if 'Pages_Viewed' in df_filtered.columns else 'pages_viewed'
            st.metric("Avg Pages Viewed", f"{df_filtered[pages_col].mean():.1f}")

        # --- CHART ---
        fig = px.pie(df_filtered, names=col_name, values=monetary_col, hole=0.4, title="Revenue by Segment")
        st.plotly_chart(fig, use_container_width=True)

except Exception as e:
    st.error(f"Error: {e}")
    st.write("Current columns in DB:", check_df.columns.tolist())


def get_sql_query(file_path):
    with open(file_path, 'r') as f:
        return f.read()

# Usage in your dashboard:
if st.checkbox("Show Campaign Effectiveness"):
    # We pull query #3 from our file (you'd usually split these or use specific markers)
    # For now, let's just run a specific part or the whole file
    conn = sqlite3.connect('data/analytics.db')
    df_kpi = pd.read_sql_query("SELECT Segment_Label, SUM(Campaign_Response) as Responses FROM user_analytics GROUP BY 1", conn)
    st.bar_chart(df_kpi.set_index('Segment_Label'))