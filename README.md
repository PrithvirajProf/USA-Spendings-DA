# USA-Spendings-EDA


This is a repo about USA Spendings in particular quarter,
This USA Spendings Extractor will extract data, analyze it and visualize it after every financial quarter, after updated on the API.
The API used in this repo is:
https://api.usaspending.gov/api/v2/references/toptier_agencies/

## Dataset Fields in USA Spendings Data Set:
 
| Field Name     | Description                                           |
|----------------|-------------------------------------------------------|
| `agency_id`           | Unique identifier for the agency                     |
| `toptier_code`         | Code for top-level federal agency classification                                   |
| `abbreviation` |Acronym of the agency name  |
| `agency_name`       | Full name of the federal agency                                        |
| `congressional_justification_url`         | Link to agency’s budget request document submitted to Congress                     |
| `active_fy`        | Current fiscal year(financial year) for which data is reported                  |
| `active_fq`  |Current fiscal quarter                                   |
| `outlay_amount`      | Actual amount spent by the agency               |
| `obligated_amount`    |Funds committed by the agency but not yet spent                                  |
| `budget_authority_amount`     | Authorized budget for the agency                                  |
| `current_total_budget_authority_amount`        |Total budget authority including all adjustments                      |
| `agency_slug`  |URL-friendly version of the agency name used in web links                                  |
