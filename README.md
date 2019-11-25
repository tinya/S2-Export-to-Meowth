# S2 Export to Meowth

A script to convert exported gyms/pokestops from the IITC [Pogo-Tools plugin](https://gitlab.com/AlfonsoML/pogo-s2) to CSV format consumable by the [Meowth 3.0](https://github.com/FoglyOgly/Meowth) Discord bot.

## Requirements
- [Pogo-Tools](https://gitlab.com/AlfonsoML/pogo-s2) export must be in JSON format.

## Limitations
- No handling of POIs not shown on the Ingress Intel map (such as sponsored stops)
- No handling of a nickname list (TBD)
- No handling of alternate lat/lon for a POI (ie, to point to a better meeting/parking point) (TBD)

## Setup
1. You must manually mark all pokestops and gyms (and EX eligibility) manually on the Ingress Intel map using [Pogo-Tools](https://gitlab.com/AlfonsoML/pogo-s2).

2. On the Ingress Intel map, zoom out until the area you wish to export all gyms/pokestops for is visible.

3. On the right hand pane, click "Pogo-Actions"

4. You can either click "Save" or "Export Gyms & Pokestops". If you click "Save", select "Pokestops + Gyms" and "JSON" options.

5. Rename the downloaded JSON file as you desire. Place it in the same location as this script.

6. Edit the following line in the script, to replace `EXPORTNAME.json` with your Pogo-Tools generated JSON filename.

```python
import_filename = 'EXPORTNAME.json'
```

7. Run the script.

```
python3 pogomeowthcsv.py
```

8. The script will generate the following two files, one each for gyms and pokestops.

```
parsed_gyms.csv
parsed_stops.csv
```

9. Run the Meowth command to import gyms/stops on your server (you may want to backup or flush the existing list first), then upload the generated CSVs.

10. You should delete the generated CSVs before running the script again to re-generate.