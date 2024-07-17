import requests
import json
import csv

def run_f1_API():
    response = requests.get("http://ergast.com/api/f1/current/last/results.json") 
    data=response.json()

    # print(data)

    race_results = data['MRData']['RaceTable']['Races'][0]['Results']

    # Define the CSV file name
    csv_file = 'race_results.csv'

    # Write the extracted data to a CSV file
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header
        writer.writerow(["Position", "Driver", "Constructor", "Grid", "Points"])
        
        # Write the rows
        for result in race_results:
            position = result['position']
            driver = result['Driver']['givenName'] + " " + result['Driver']['familyName']
            constructor = result['Constructor']['name']
            grid = result['grid']
            points = result['points']
            
            writer.writerow([position, driver, constructor, grid, points])

    print(f"Data has been written to {csv_file}")