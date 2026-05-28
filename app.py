import streamlit as st
from pytrends.request import TrendReq
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(
    page_title="Google Trends Analysis",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Google Search Trends Analysis Dashboard")

st.write(
    "Compare Google search trends, analyze regions, and explore related queries."
)

# User input
keyword_input = st.text_input(
    "Enter keywords separated by commas",
    "Python, AI, Machine Learning"
)

if st.button("Analyze"):

    keywords = [
        k.strip()
        for k in keyword_input.split(",")
        if k.strip()
    ]

    try:
        pytrends = TrendReq(
            hl='en-US',
            tz=330
        )

        pytrends.build_payload(
            keywords,
            timeframe='today 5-y'
        )

        # Interest over time
        trend_data = pytrends.interest_over_time()

        if not trend_data.empty:

            st.subheader("Interest Over Time")

            fig = px.line(
                trend_data,
                y=keywords,
                title="Google Search Interest Over Time"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            # Download CSV
            csv = trend_data.to_csv().encode('utf-8')

            st.download_button(
                label="Download CSV",
                data=csv,
                file_name="google_trends.csv",
                mime="text/csv"
            )

        # Region Analysis
        st.subheader("Top Regions")

        region_data = pytrends.interest_by_region()

        if not region_data.empty:

            selected_keyword = st.selectbox(
                "Select keyword",
                keywords
            )

            top_regions = (
                region_data
                .sort_values(
                    by=selected_keyword,
                    ascending=False
                )
                .head(10)
            )

            st.dataframe(top_regions)

            fig_region = px.bar(
                top_regions,
                y=selected_keyword,
                title=f"Top Regions Searching {selected_keyword}"
            )

            st.plotly_chart(
                fig_region,
                use_container_width=True
            )

        # Related Queries
        st.subheader("Related Queries")

        related_queries = pytrends.related_queries()

        for keyword in keywords:

            st.markdown(f"### {keyword}")

            if (
                related_queries[keyword]
                and related_queries[keyword]["top"] is not None
            ):
                st.dataframe(
                    related_queries[keyword]["top"]
                )
            else:
                st.write(
                    "No related queries available."
                )

    except Exception as e:
        st.error(
            "Google Trends temporarily blocked requests. Please try again in a few seconds."
        )
