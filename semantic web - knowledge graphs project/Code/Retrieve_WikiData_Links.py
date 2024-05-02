import requests
import csv

# Load csv to read the Rider names
csv_path = r'C:\Users\panos\Downloads\riders-finishing-positions.csv' # please update  with your file path
csv_flag = True
with open(csv_path, 'r', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)
    data = [row for row in csvreader]

for row in data:

    rider_name = row['Rider']
    print(rider_name)

    # Split the full name into first and last names
    names = rider_name.split()
    search_name = names[0]  # First name
    search_surname = ' '.join(names[1:])  # Remaining names as the surname

    # Define the SPARQL query with parameters for name and surname
    sparql_query = f"""
        SELECT ?item ?name
        WHERE {{
          ?item wdt:P735 ?n.
          ?n wdt:P1705 ?name.
          FILTER(STR(?name)="{search_name}")

          ?item wdt:P734 ?s.
          ?s wdt:P1705 ?surname.
          FILTER(STR(?surname)="{search_surname}")

          SERVICE wikibase:label {{ bd:serviceParam wikibase:language "el,en" }}
        }}
        """

    # Define Wikidata Query Service endpoint
    endpoint_url = "https://query.wikidata.org/sparql"

    # Set up the HTTP headers with the User-Agent information
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "application/json"
    }

    # Set up the HTTP parameters
    params = {
        "query": sparql_query,
        "format": "json"
    }

    # Send the HTTP request to the Wikidata Query Service API
    response = requests.get(endpoint_url, headers=headers, params=params)

    # Check if the request was successfully sent
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract the ?item and ?name values from the results
        results = data.get("results", {}).get("bindings", [])
        if results:
            item_value = results[0].get("item", {}).get("value", "")
            name_value = results[0].get("name", {}).get("value", "")

            # Save the results to a CSV file
            csv_filename = "wikidata_results.csv"
            with open(csv_filename, mode='a', newline='', encoding='utf-8') as csv_file:
                fieldnames = ['wiki data link', 'Name']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                if csv_flag == True:
                    writer.writeheader()
                    csv_flag = False

                writer.writerow({'wiki data link': item_value, 'Name': rider_name})

            print(f"Results saved to {csv_filename}")

        else:
            print("No results found.")
    else:
        print("Error:", response.status_code)
        print(response.text)
