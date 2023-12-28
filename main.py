import streamlit as st
import plotly.express as px

st.title('Weather Forecast for the Next Days')
place = st.text_input(label='Place:')
days_slider = st.slider(label='Forecast Days', min_value=1, max_value=5,
                        help='Select the number of forecasted days')
select_option = st.selectbox(label='Select data to view',
                             options=('Temperature', 'Sky'))

st.subheader(f'{select_option} for the next {days_slider} days in {place}')


def get_data(days_slider):
    dates = ['2023-20-12', '2023-21-12', '2023-22-12']
    temperatures = [2, 3, 5]
    temperatures = [days_slider * i for i in temperatures]
    return dates, temperatures

d, t = get_data(days_slider)

figure = px.line(x=d, y=t, labels={'x': 'Date', 'y': 'Temperature (C)'})
st.plotly_chart(figure)
