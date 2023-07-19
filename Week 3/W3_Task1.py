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

    csv_writer.writerow(["景點名稱", "區域", "經度,緯度", "第一張圖檔位置"])


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

print("Data successfully written to attraction.csv")