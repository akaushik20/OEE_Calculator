import streamlit as st
def main():
    # Set the page configuration
    st.set_page_config(page_title="Streamlit App Example", layout="wide")

    # Sidebar for navigation
    st.sidebar.title("Navigation")
    st.sidebar.write("Use the sidebar to navigate through the app.")

    # Main content area
    st.title("OEE Calculator")
    st.write("This tools help to calculate OEE (Overall Equipment Effectiveness)")

    # Input fields for OEE calculation
    st.subheader("Input Data")
    demand_annual = st.number_input("Demand Per Annum: ", min_value=0.0, max_value=3000000.0, value=30000.0, step=1.0)
    production = st.number_input("Production Per Day: ", min_value=0.0, max_value=30000.0, value=240.0, step=0.1)
    scheduled_time = st.number_input("Scheduled Time(3 shifts, 8 hours): ", min_value=0.0, max_value=30.0, value=20.0, step=0.1)
    oee_loss = st.number_input("OEE Loss Target(Assumption) %: ", min_value=0.0, max_value=1.00, value=0.15, step=0.1)
    
    st.text("All Time: 24*60 = 1440 Minutes")

    st.button("Calculate OEE", key="calculate_oee")

if __name__ == "__main__":
    main()