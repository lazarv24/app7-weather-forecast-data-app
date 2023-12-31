import requests

API_KEY = '785e9ec543b09c96af3a17caacc0b809'


def get_data(place, forecast_days=None):
    url = (f'http://api.openweathermap.org/data/2.5/forecast?q='
           f'{place}&appid={API_KEY}&units=metric')
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    number_of_values = 8 * forecast_days
    filtered_data = filtered_data[:number_of_values]
    return filtered_data


if __name__ == '__main__':
    print(get_data(place='Tokyo', forecast_days=3))
