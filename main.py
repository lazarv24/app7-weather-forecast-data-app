import streamlit as st

st.title('Weather Forecast for the Next Days')
place = st.text_input(label='Place:')
days_slider = st.slider(label='Forecast Days', min_value=1, max_value=5,
                        help='Select the number of forecasted days')
select_option = st.selectbox(label='Select data to view',
                             options=('Temperature', 'Sky'))

st.subheader(f'{select_option} for the next {days_slider} days in {place}')