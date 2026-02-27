import streamlit as st

# fake plugin logic
def generate_company_summary(company):
    return {
        "sector": "technology",
        "revenue": "383B USD",
        "analysis": f"{company} shows strong growth and health margins."
    }

st.title(" Finance Research Mini App")

company = st.text_input("Enter company name")

if company:
    data = generate_company_summary(company)

    st.subheader("Result")
    st.write("Sector:", data["sector"])
    st.write("Revenue", data["revenue"])
    st.write("Analysis:", data["analysis"])


