# ============================================================
# SEO CONTENT OPTIMIZER (AI/ML PROJECT)
# Student: Esha Fatima
# ============================================================

import streamlit as st
from seo_core import analyze_seo

st.set_page_config(page_title="SEO Optimizer", layout="centered")

st.title("🚀 SEO Content Optimizer")

content = st.text_area("Paste your content here:")
keyword = st.text_input("Enter your target keyword:")

if st.button("Analyze"):
    if content and keyword:
        result = analyze_seo(content, keyword)

        st.subheader("📊 Results")
        st.write(result)

        st.subheader("💡 Suggestions")
        for s in result["Suggestions"]:
            st.write("- " + s)
    else:
        st.warning("Please enter both content and keyword")