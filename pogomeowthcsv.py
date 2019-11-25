#!usr/bin/env python3

import json
import csv

import_filename = 'EXPORTNAME.json'
gymnick_filename = 'gymnicknames.csv'
exp_gym_filename = 'parsed_gyms.csv'
exp_stop_filename = 'parsed_stops.csv'
meowth_gym_filename = 'meowth_gyms.csv'
meowth_stop_filename = 'meowth_stops.csv'
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
csvwriter.writerow(meowth_gym_header)

for gym in gym_data:
 #   print('{} - {}'.format(gym, gym_data[gym]))
 #   for g in gym_data[gym]:
 #       print('{} - {}'.format(g, gym_data[gym][g]))
    #csvwriter.writerow(gym_data[gym].values())
    if 'isEx' in gym_data[gym].keys():
        csvwriter.writerow([gym_data[gym]['name'], ' ', gym_data[gym]['lat'], gym_data[gym]['lng'], 'TRUE'])
    else:
        csvwriter.writerow([gym_data[gym]['name'], ' ', gym_data[gym]['lat'], gym_data[gym]['lng'], 'FALSE'])

export_file.close()

### Parse the stops from IITC
stop_data = iitc_data['pokestops']

# Open a file for writing
export_file = open(exp_stop_filename, 'w')

# Create CSV writer object
csvwriter = csv.writer(export_file)
csvwriter.writerow(meowth_stop_header)

for stop in stop_data:
    csvwriter.writerow([stop_data[stop]['name'], ' ', stop_data[stop]['lat'], stop_data[stop]['lng']])

export_file.close()


"""
# Add nicknames to Meowth CSV

gymnick_dict = csv.DictReader(open(gymnick_filename, 'r'))
gym_dict = csv.DictReader(open(exp_gym_filename, 'r'))
#export_file = open(meowth_gym_filename, 'w')
#csvwriter = csv.writer(export_file)

#csvwriter.writerow(meowth_gym_header)

#with open(exp_gym_filename, 'r') as fd:
#    csvgym = csv.DictReader(fd)


for nick in gymnick_dict:
    print(nick['name'])
    tmpgym_dict = list(gym_dict)
    for gym in tmpgym_dict:
        print(nick['lat'])

#       if gymnick_dict[nick]['lat'] == gym_dict[gym]['lat'] and gymnick_dict[nick]['lon'] == gym_dict[gym]['lon']:
#           print(nick['lat'])

#export_file.close()



export_file = open(meowth_stop_filename, 'w')
csvwriter = csv.writer(export_file)
csvwriter.writerow(meowth_stop_header)

with open(exp_stop_filename, 'r') as fd:
    csvstop = csv.DictReader(fd)

    for row in csvstop:
        csvwriter.writerow([row['name'], ' ', row['lat'], row['lon']])

export_file.close()

"""
