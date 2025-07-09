import requests
import json 
import pandas as pd  
url = "https://api.usaspending.gov/api/v2/references/toptier_agencies/"
params = {
    "per_page": 200,
    "page": 1
}
 
 
response = requests.get(url, params=params, verify=False)
 
if response.status_code == 200:
    data = response.json()
 
    # Save JSON file
    with open("USASpending.json", "w") as f:
        json.dump(data, f, indent=2)
    print("Data saved to USASpendings.json")
 
    # Normalize and save as CSV
    df = pd.json_normalize(data['results'])
 
    df = df[[
        'agency_id', 'toptier_code', 'abbreviation', 'agency_name', 'congressional_justification_url', 'active_fy',
        'active_fq', 'outlay_amount', 'obligated_amount', 'budget_authority_amount',
        'current_total_budget_authority_amount', 'percentage_of_total_budget_authority','agency_slug'
    ]]
 
    df.to_csv("USASpendings.csv", index=False)
    print(" Data saved to USASpendings.csv")
 
elif response.status_code == 400:
    print("Bad Request")
else:
    print(f"Request failed with status code: {response.status_code}")
 
print("Status Code:", response.status_code)