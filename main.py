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

    st.write("This is a simple example of a Streamlit app with a sidebar and main content area.")

if __name__ == "__main__":
    main()