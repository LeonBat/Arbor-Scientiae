############
# This script ingests the mock run data into the database for testing purposes.
############


#Libraries
import json
import requests




# getting response from github
url = "https://github.com/LeonBat/Arbor-Scientiae/blob/main/tests/mock_papers.json"

try: 
    response = requests.get(url)
except requests.exceptions.RequestException as e:
    print(f"Error fetching data from {url}: {e}")
    exit(1)


# Writing result of response to a testfile
# Request is successful
file = open("tests/test_data.json", "w")
json.dump(response.json(), file)
file.close()