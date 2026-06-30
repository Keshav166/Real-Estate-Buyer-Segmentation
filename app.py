import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(
    page_title="Real Estate Intelligence Dashboard",
    page_icon="🏠",
    layout="wide"
)

# ----------------------------
# LOAD DATA
# ----------------------------
df = pd.read_csv("final_df.csv")

# ----------------------------
# SIDEBAR FILTERS
# ----------------------------
st.sidebar.title("🎛 Filters")

segment = st.sidebar.multiselect(
    "Select Segment",
    df["segment"].unique(),
    default=df["segment"].unique()
)

client_type = st.sidebar.multiselect(
    "Client Type",
    df["client_type"].unique(),
    default=df["client_type"].unique()
)

country = st.sidebar.multiselect(
    "Country",
    df["country"].unique(),
    default=df["country"].unique()
)

filtered_df = df[
    (df["segment"].isin(segment)) &
    (df["client_type"].isin(client_type)) &
    (df["country"].isin(country))
]

# ----------------------------
# HEADER
# ----------------------------
st.title("🏠 Real Estate Buyer Segmentation Dashboard")
st.markdown("AI-powered segmentation, investment analysis & business decision insights")

st.markdown("---")

# ----------------------------
# KPI CARDS
# ----------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("👥 Total Buyers", len(filtered_df))
col2.metric("💰 Total Investment", f"${filtered_df['total_investment'].sum():,.0f}")
col3.metric("🏡 Avg Properties", round(filtered_df['total_properties'].mean(), 2))
col4.metric("⭐ Avg Satisfaction", round(filtered_df['satisfaction_score'].mean(), 2))

st.markdown("---")

# ----------------------------
# 🧠 DECISION INTELLIGENCE ENGINE
# ----------------------------
st.subheader("🧠 AI Business Decision Insights")

if len(filtered_df) > 0:

    best_segment = filtered_df.groupby("segment")["total_investment"].mean().idxmax()
    worst_segment = filtered_df.groupby("segment")["satisfaction_score"].mean().idxmin()
    high_value_customers = filtered_df[
        filtered_df["total_investment"] > filtered_df["total_investment"].median()
    ].shape[0]

    avg_investment_best = filtered_df[filtered_df["segment"] == best_segment]["total_investment"].mean()

    colA, colB = st.columns(2)

    with colA:
        st.info(f"""
📌 **Best Performing Segment:** {best_segment}  
📈 Avg Investment: ${avg_investment_best:,.0f}  

⚠️ **Needs Attention Segment:** {worst_segment}  
        """)

    with colB:
        st.info(f"""
💰 High Value Customers: {high_value_customers}  

📊 Total Segments Analyzed: {filtered_df["segment"].nunique()}  
        """)

    # ----------------------------
    # BUSINESS RECOMMENDATION BOX
    # ----------------------------
    st.success(f"""
💡 **Automated Recommendation**

✔ Focus marketing efforts on **{best_segment}** (highest investment potential).  
✔ Improve customer experience for **{worst_segment}** to increase satisfaction.  
✔ Target high-value customers with premium investment plans.
""")

else:
    st.warning("No data available for selected filters")

st.markdown("---")

# ----------------------------
# TABS FOR CLEAN UI
# ----------------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Segment Overview",
    "💰 Investment Analysis",
    "👤 Customer Insights",
    "📄 Dataset"
])

# ----------------------------
# TAB 1 - SEGMENTS
# ----------------------------
with tab1:
    st.subheader("Buyer Segment Distribution")

    fig, ax = plt.subplots()
    sns.countplot(data=filtered_df, x="segment", ax=ax)
    plt.xticks(rotation=30)
    st.pyplot(fig)

    st.markdown("### Segment-wise Summary")
    st.dataframe(filtered_df.groupby("segment").mean(numeric_only=True))

# ----------------------------
# TAB 2 - INVESTMENT
# ----------------------------
with tab2:
    st.subheader("Investment Distribution")

    fig, ax = plt.subplots()
    sns.boxplot(data=filtered_df, x="segment", y="total_investment", ax=ax)
    plt.xticks(rotation=30)
    st.pyplot(fig)

    st.markdown("### Avg Investment per Segment")
    st.dataframe(
        filtered_df.groupby("segment")["total_investment"].mean().sort_values(ascending=False)
    )

# ----------------------------
# TAB 3 - CUSTOMER INSIGHTS
# ----------------------------
with tab3:
    st.subheader("Age vs Investment Behavior")

    fig, ax = plt.subplots()
    sns.scatterplot(
        data=filtered_df,
        x="age",
        y="total_investment",
        hue="segment",
        ax=ax
    )
    st.pyplot(fig)

    st.subheader("Satisfaction by Segment")

    fig2, ax2 = plt.subplots()
    sns.barplot(data=filtered_df, x="segment", y="satisfaction_score", ax=ax2)
    st.pyplot(fig2)

# ----------------------------
# TAB 4 - DATASET (CLEAN COLLAPSIBLE)
# ----------------------------
with tab4:
    st.subheader("Data Explorer")

    with st.expander("📄 Click to view dataset"):
        st.dataframe(filtered_df, use_container_width=True)

# ----------------------------
# FOOTER
# ----------------------------
st.markdown("---")
st.markdown("🚀 Built with Streamlit | AI-Powered Real Estate Intelligence System")