#!usr/bin/env python3

import json
import csv

import_filename = 'gyms+stops_2019_11_21_23_21_19.json'
exp_gym_filename = 'parsed_gyms.csv'
exp_stop_filename = 'parsed_stops.csv'
meowth_gym_filename = 'meowth_gyms.csv'
meowth_stop_filename = 'meowth_stops.csv'
parsed_header = ['guid','lat','lon','name','ex']
meowth_gym_header = ['name','nickname','lat','lon','exraid']
meowth_stop_header = ['name','nickname','lat','lon']


with open(import_filename, 'r') as fd:
    iitc_data = json.load(fd)

### Parse the gyms from IITC
gym_data = iitc_data['gyms']

# Open a file for writing
export_file = open(exp_gym_filename, 'w')

# Create CSV writer object
csvwriter = csv.writer(export_file)
csvwriter.writerow(parsed_header)

for gym in gym_data:
 #   print('{} - {}'.format(gym, gym_data[gym]))
 #   for g in gym_data[gym]:
 #       print('{} - {}'.format(g, gym_data[gym][g]))
    csvwriter.writerow(gym_data[gym].values())

export_file.close()

### Parse the stops from IITC
stop_data = iitc_data['pokestops']

# Open a file for writing
export_file = open(exp_stop_filename, 'w')

# Create CSV writer object
csvwriter = csv.writer(export_file)
csvwriter.writerow(parsed_header)

for stop in stop_data:
    csvwriter.writerow(stop_data[stop].values())

export_file.close()

# Convert parsed CSV to Meowth CSV
export_file = open(meowth_gym_filename, 'w')
csvwriter = csv.writer(export_file)
csvwriter.writerow(meowth_gym_header)

with open(exp_gym_filename, 'r') as fd:
    csvgym = csv.DictReader(fd)

    for row in csvgym:
        if row['ex'] == 'True':
            csvwriter.writerow([row['name'], ' ', row['lat'], row['lon'], 'TRUE'])
        else:
            csvwriter.writerow([row['name'], ' ', row['lat'], row['lon'], 'FALSE'])

export_file.close()

export_file = open(meowth_stop_filename, 'w')
csvwriter = csv.writer(export_file)
csvwriter.writerow(meowth_stop_header)

with open(exp_stop_filename, 'r') as fd:
    csvstop = csv.DictReader(fd)

    for row in csvstop:
        csvwriter.writerow([row['name'], ' ', row['lat'], row['lon']])

export_file.close()