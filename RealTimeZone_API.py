import requests
print('===================================================')
print('=========== WELCOME TO TIMEZONE API ===========')
print('************ BSIT 2-2 (GROUP_2) ************')
print()
try:
    
    Location = input(' Enter County: ')
    print('===================================================')
    key = 'a0727fe5080d4596a848d13b6983f382'
    url = 'https://timezone.abstractapi.com/v1/current_time/?api_key={}&location={}'.format(key, Location)
    r = requests.get(url)
    data = r.json()

    location = data['requested_location']
    longitude = data['longitude']
    latitude = data['latitude']
    datetime = data['datetime']
    timezone_name = data['timezone_name']
    timezone_location = data['timezone_location']
    print('******* info *******')
    print()
    print('  requested_location: ', location)
    print('  timezone_name: ', timezone_name)
    print('  timezone_location: ', timezone_location)
    print('  datetime: ', datetime)
    print('  longitude: ', longitude)
    print('  latitude: ',latitude)
    print('  ([INFO!!] Success..)')
    print()
except:
    print('[INFO] ERROR.....')
    print('plsss try again.....')

#print(data.keys())