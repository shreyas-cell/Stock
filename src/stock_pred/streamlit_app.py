import streamlit as st
import requests
import pandas as pd

# Data storage (cache)
@st.cache(allow_output_mutation=True)
def get_data():
    return []

def main():
    st.title("Investment Data Entry")

    # Input fields
    amount = st.number_input("Investment Amount", min_value=0.0)
    years = st.number_input("Investment Years", min_value=0.0)
    roi = st.number_input("ROI (Annual)", min_value=0.0)

    # Save button
    if st.button("Save Investment"):
        try:
            response = requests.post("http://127.0.0.1:5000/saveData", json={"amount": amount, "years": years, "roi": roi})
            print(f"Response status code: {response.status_code}")
            print(f"Response content: {response.content}")
            if response.status_code == 200:
                st.success(response.json()["message"])
                data = get_data()
                data.append([amount, years, roi])
            else:
                st.error("Failed to save data")
        except requests.exceptions.RequestException as e:
            st.error(f"Request failed: {e}")

    # Display saved data (if any)
    data = get_data()
    if data:
        st.subheader("Saved Investments")
        df = pd.DataFrame(data, columns=["Amount", "Years", "ROI"])
        st.dataframe(df)

if __name__ == '__main__':
    main()
