############
# Ingestion Script
############


# This script is used to ingest paper information from the Semantic
# Scholar API into a MYSQL database. It fetches paper metadata like the title,
# authors or citations and also content like the abstract


# Libraries
import requests
import json
import time


# Function to fetch papers from Semantic Scholar API

def fetch_papers(query, limit, fields = "title, citations, references, year, authors"):

    # defining request
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    params = {
        "query": query,
        "limit": limit,
        "fields": fields
    }

    # Initialize Exponential Backoff parameters
    max_retries = 5
    wait_time = 1 #in seconds

    for attempt in range(max_retries):
        response = requests.get(url, params = params)

        if response.status_code == 200:
            return response.json()
        
        elif response.status_code == 429:
            print(f"Rate limit hit. Wait time {wait_time}")
            time.sleep(wait_time)
            wait_time *= 2
            
        else:
            print(f"Error: {response.status_code}")
            break
    
    return None


data = fetch_papers("machine_learning", limit = 5)

print(data)