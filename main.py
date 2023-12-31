import streamlit as st
import plotly.express as px
from backend import get_data

st.title('Weather Forecast for the Next Days')
place = st.text_input(label='Place:')
days_slider = st.slider(label='Forecast Days', min_value=1, max_value=5,
                        help='Select the number of forecasted days')
select_option = st.selectbox(label='Select data to view',
                             options=('Temperature', 'Sky'))

st.subheader(f'{select_option} for the next {days_slider} days in {place}')

if place:
    try:
        filtered_data = get_data(place, days_slider)

        if select_option == 'Temperature':
            temperatures = [dict['main']['temp'] for dict in filtered_data]
            dates = [dict['dt_txt'] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={'x': 'Date',
                                                       'y': 'Temperature (C)'})
            st.plotly_chart(figure)

        if select_option == 'Sky':
            images = {'Clear': 'images/clear.png', 'Clouds': 'images/cloud.png',
                      'Rain': 'images/rain.png', 'Snow': 'images/snow.png'}
            sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            print(sky_conditions)
            st.image(image_paths, width=115)

    except KeyError:
        st.write("You entered a place that doesn't exist. Please write a "
                 "correct name of the place")
