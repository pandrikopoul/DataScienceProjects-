import requests

# Set the URL of BlazeGraph REST API endpoint
blazegraph_url = 'http://localhost:8080/blazegraph' # please The BlazeGraph REST API endpoint acordingly (if diferent)

# Set the Content-Type of HTTP request as application/x-turtle
headers = {'Content-Type': 'application/x-turtle'}

# Store MotoGp p

# Read the RDF data from the ttl file
with open("C:/Users/panos/PycharmProjects/pythonProject/venv/MotoGp_P_FinalOutPut.ttl", 'r', encoding='utf-8') as file:   # please update  with your file path
    rdf_data = file.read()
rdf_data = rdf_data.encode('utf-8')
# Set the BlazeGraph REST API endpoint
update_endpoint = blazegraph_url + '/namespace/kde1'

# Make a POST request to insert the data in the Triple store
response = requests.post(update_endpoint, headers=headers, data=rdf_data)

# Check the responce status
if response.status_code == 200:
    print("The MotoGp_P_FinalOutPut RDF Graph for the was stored succesfully")
else:
    print(f" An error occured when trying to store the MotoGp_P_FinalOutPut Graph. Responce status code: {response.status_code}")
    print(response.text)

# Store MotoGp s

# Read the RDF data from the ttl file
with open("C:/Users/panos/PycharmProjects/pythonProject/venv/MotoGP_S_FinalOutPut.ttl", 'r', encoding='utf-8') as file:# please update  with your file path
    rdf_data = file.read()
rdf_data = rdf_data.encode('utf-8')
# Set the BlazeGraph REST API endpoint
update_endpoint = blazegraph_url + '/namespace/kde1'

# Make a POST request to insert the data in the Triple store
response = requests.post(update_endpoint, headers=headers, data=rdf_data)

# Check the responce status
if response.status_code == 200:
    print("The MotoGP_S_FinalOutPut RDF Graph for the was stored succesfully")
else:
    print(f" An error occured when trying to store the MotoGP_S_FinalOutPut Graph. Responce status code: {response.status_code}")
    print(response.text)

# Store Formula1


# Read the RDF data from the ttl file
with open("C:/Users/panos/PycharmProjects/pythonProject/venv/FormulaOne_FinalOutPut.ttl", 'r', encoding='utf-8') as file:# please update  with your file path
    rdf_data = file.read()
rdf_data = rdf_data.encode('utf-8')
# Set the BlazeGraph REST API endpoint
update_endpoint = blazegraph_url + '/namespace/kde1'

# Make a POST request to insert the data in the Triple store
response = requests.post(update_endpoint, headers=headers, data=rdf_data)

# Check the responce status
if response.status_code == 200:
    print("The FormulaOne_FinalOutPut RDF Graph for the was stored succesfully")
else:
    print(f" An error occured when trying to store the FormulaOne_FinalOutPut Graph. Responce status code: {response.status_code}")
    print(response.text)





