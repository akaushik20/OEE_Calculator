import streamlit as st
from helpers.functions import calculate_oee

def main():
    # Set the page configuration
    st.set_page_config(page_title="OEE Calculator", layout="wide")

    # Sidebar for navigation
    st.sidebar.title("Navigation")
    st.sidebar.write("Use the sidebar to navigate through the app.")

    # Main content area
    st.title("OEE Calculator")
    st.write("This tools help to calculate OEE (Overall Equipment Effectiveness)")

    # Input fields for OEE calculation
    st.subheader("Input Data")
    demand_annual = st.number_input("📈 Demand Per Annum: ", min_value=0.0, max_value=3000000.0, 
                                    value=30000.0, step=1.0,
                                    help="Enter the total annual demand for the product.")
    production = st.number_input("🏭 Production Per Day: ", min_value=0.0, max_value=30000.0, value=240.0, step=0.1)
    scheduled_time = st.number_input("⏱️ Scheduled Time(3 shifts, 8 hours): ", min_value=0.0, max_value=30.0, value=20.0, step=0.1)
    oee_loss = st.number_input("📉 OEE Loss Target(Assumption) %: ", min_value=0.0, max_value=1.00, value=0.15, step=0.1)
    
    
    st.text("All Time: 24*60 = 1440 Minutes")

    values = {
        "Demand Per Annum": demand_annual,
        "Production Per Day": production,
        "Scheduled Time(3 shifts, 8 hours)": scheduled_time,
        "OEE Loss Target(Assumption) %": oee_loss
    }

    calculate=st.button("Calculate OEE", key="calculate_oee")
    
    return calculate, values




if __name__ == "__main__":
    calculate_flg, values=main()

    if calculate_flg:
        # Get the input values
        demand_annual = values["Demand Per Annum"]
        production = values["Production Per Day"]
        scheduled_time = values["Scheduled Time(3 shifts, 8 hours)"]
        oee_loss = values["OEE Loss Target(Assumption) %"]

        # Calculate OEE
        oee = calculate_oee(demand_annual, production, scheduled_time, oee_loss)

        # convert OEE into percentage for display
        oee_percentage = oee * 100

        # Display the result
        st.subheader("📊 OEE Result")
        st.write(f"✅ Overall Equipment Effectiveness (OEE): {oee_percentage:.2f}%")
        st.write("ℹ️ This is the OEE value based on the input data.")  