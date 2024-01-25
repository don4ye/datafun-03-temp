# datafun-03-temp# datafun-03-project

## Create Project Virtual Environment

On Windows, create a project virtual environment in the .venv folder.

```shell
py -m venv .venv
.venv\Scripts\Activate
py -m pip install -r requirements.txt
git add .
git commit -m "add .gitignore, cmds to readme"
git push origin main
"""
Transportation Services Module

This module provides a reusable byline for transportation services.

Functions:
- moving_of_goods_to_different_destinations: Function to facilitate the movement of goods to various destinations.

Classes:
- CargoVan: A class representing a cargo van used for transportation.

Author: Don
Date: 1/11/2024
"""

import math
import statistics

# Company information
company_name = "Aaga Logistics LLC."
count_active_projects = 5
has_international_presence = False
average_client_satisfaction = 4.7
services_offered = ["Logistics and Supply Chain Management", "Courier and Express Delivery Services", "Freight Transportation"]
satisfaction_scores = [4.8, 4.6, 4.9, 5.0, 4.7]

# Statistics calculations
smallest = min(satisfaction_scores)
largest = max(satisfaction_scores)
total = sum(satisfaction_scores)
count = len(satisfaction_scores)
mean = statistics.mean(satisfaction_scores)
mode = statistics.mode(satisfaction_scores)
median = statistics.median(satisfaction_scores)
standard_deviation = statistics.stdev(satisfaction_scores)

# Descriptive statistics string
stats_string = f"""
Descriptive Statistics for Our Satisfaction Scores:
  Smallest: {smallest}
  Largest: {largest}
  Total: {total}
  Count: {count}
  Mean: {mean}
  Mode: {mode}
  Median: {median}
  Standard Deviation: {standard_deviation}
"""

def main():
    ''' Display company information and statistics '''
    print("Company Information:")
    print(f"Company Name: {company_name}")
    print(f"Active Projects: {count_active_projects}")
    print(f"International Presence: {has_international_presence}")
    print(f"Average Client Satisfaction: {average_client_satisfaction}")

    print("\nServices Offered:")
    for service in services_offered:
        print(f"- {service}")

    print("\nDescriptive Statistics:")
    print(stats_string)

if __name__ == "__main__":
    main()
