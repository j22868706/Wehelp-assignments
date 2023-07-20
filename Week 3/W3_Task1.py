# to fetch data from the URL
import urllib.request as request
import json
import re
import csv


src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data = json.load(response) # to deserialize a JSON file

# extracts the list of attractions from JSON file
attraction_list = data["result"]["results"]
with open("attraction.csv", "w", encoding = "utf-8", newline = "" ) as file:  # writes the list to a file
    csv_writer = csv.writer(file)

    for attraction in attraction_list:
        attraction_title = attraction["stitle"]
        attraction_address = attraction["address"]
        attraction_longitude = attraction["longitude"]
        attraction_file = attraction["file"]
    
        match_attraction_address = re.search(r'\S+區', attraction_address) #matches a sequence of non-whitespace characters followed by the character "區" in a string.
        if match_attraction_address:
            extracted_district = match_attraction_address.group()

        split_attraction_file = attraction_file.split("https://")
        extracted_url = "https://" + split_attraction_file[1]
        
        csv_writer.writerow([attraction_title, extracted_district, attraction_longitude, extracted_url])


mrt_list = data["result"]["results"]

mrt_attractions = {}
for mrt in mrt_list:
    mrt_title = mrt["MRT"]
    if not mrt_title:
        continue
    attraction_title = mrt["stitle"]
    if mrt_title in mrt_attractions:
        mrt_attractions[mrt_title].append(attraction_title)
    else:
        mrt_attractions[mrt_title] = [attraction_title]
    print(attraction_title)
output_file = "mrt.csv"
with open(output_file, "w", encoding = "utf-8", newline = "" ) as csvfile:  # writes the list to a file
    csv_writer = csv.writer(csvfile)
    for mrt, attractions in mrt_attractions.items():
        attractions_str = ','.join(attractions)
        csv_writer.writerow([mrt, attractions_str])
print("Data successfully written to attraction.csv")