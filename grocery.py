import streamlit as st

def main():
    st.set_page_config(page_title="Grocery Store Sales Prediction", page_icon=":shopping_cart:")

    st.title('Grocery Store Sales Prediction')
    st.subheader('Enter the following information about the store to predict sales')

    # Dropdown for Store Type
    store_type = st.selectbox('Store Type', options=['Type 1', 'Type 2', 'Type 3'])

    # Radio buttons for Location
    location = st.radio('Location', options=['City', 'Urban', 'Rural'])

    # Slider for Store Size
    size = st.slider('Store Size (in square feet)', min_value=0, max_value=10000, step=100, value=5000)

    # Number input for Advertising Spend
    advertising = st.number_input('Advertising Spend (in dollars)', min_value=0, max_value=100000, step=1000, value=5000)

    # Checkbox for Loyalty Program
    loyalty_program = st.checkbox('Loyalty Program')

    # Date input for Promotion Start Date
    start_date = st.date_input('Promotion Start Date')

    # Time input for Promotion Start Time
    start_time = st.time_input('Promotion Start Time')

    if st.button('Predict Sales'):
        st.success(f'Predicted Sales: $100,000')

if __name__ == '__main__':
    main()
