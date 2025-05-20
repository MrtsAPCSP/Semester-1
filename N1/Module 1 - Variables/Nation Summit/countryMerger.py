# This file merges all of the student country files
# All information is added to the merged_countries.json file
# This data then will be used for the simulation without affecting
# the original files

import os
import importlib.util
import json

# Base directory is where this script lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Folder containing student .py files
COUNTRY_FOLDER = os.path.join(BASE_DIR, "country_files")

# Output merged JSON file
MERGED_OUTPUT_FILE = os.path.join(BASE_DIR, "merged_countries.json")

# Optional: Add a log file to track which countries were processed
MERGE_LOG_FILE = os.path.join(BASE_DIR, "merge_log.txt")


def load_country_data(file_path):
    spec = importlib.util.spec_from_file_location("country", file_path)
    country_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(country_module)
    return country_module


def calculate_derived_values(country):
    # Calculate GDP
    country.GDP = 250_000_000_000 * (1 + (country.tax_rate * -0.01) / 5) * (1 + (country.population / 200_000_000))

    # Calculate Happiness Index
    country.happiness_index = (
        100
        - ((country.tax_rate / 100) / 5)
        + (1 if country.government_spending_pct > 50 else 0)
        - (1 if country.income_inequality > 75 else 0)
        + (1 if country.literacy_rate > 90 else 0)
        - (country.unemployment_rate / 2)
    )

    # Calculate Population Loyalty
    country.population_loyalty = (
        60 + country.happiness_index - country.unemployment_rate + (country.government_spending_pct / 2)
    )

    # Calculate Environmental Score
    base_score = 50
    if getattr(country, "terrain_type", None) == "desert":
        base_score -= 5
    elif country.terrain_type == "forest":
        base_score += 5
    elif country.terrain_type == "tundra":
        base_score -= 3

    if country.continent == "Africa":
        base_score += 2
    elif country.continent == "Europe":
        base_score += 3
    elif country.continent == "Asia":
        base_score -= 1

    country.environment_score = base_score

    return country


def convert_to_dict(country):
    # Get all public (non-dunder) variables and constants from the module
    raw_dict = vars(country)
    country_dict = {
        key: value
        for key, value in raw_dict.items()
        if not key.startswith("__") and not callable(value)
    }
    return country_dict


def merge_country_files():
    countries = []
    log_lines = []

    if not os.path.exists(COUNTRY_FOLDER):
        print(f"[ERROR] Folder not found: {COUNTRY_FOLDER}")
        return

    print(f"[INFO] Scanning folder: {COUNTRY_FOLDER}")
    for filename in os.listdir(COUNTRY_FOLDER):
        if filename.endswith(".py"):
            file_path = os.path.join(COUNTRY_FOLDER, filename)
            try:
                country = load_country_data(file_path)
                country = calculate_derived_values(country)
                country_dict = convert_to_dict(country)
                countries.append(country_dict)
                log_lines.append(f"✅ Processed: {filename} → {country_dict.get('country_name', 'UNKNOWN')}")
            except Exception as e:
                error_message = f"❌ Error processing {filename}: {e}"
                print(error_message)
                log_lines.append(error_message)

    # Save to merged JSON
    with open(MERGED_OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(countries, f, indent=4)

    # Save a text log file for review
    with open(MERGE_LOG_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(log_lines))

    print(f"[INFO] Merged {len(countries)} countries to: {MERGED_OUTPUT_FILE}")
    print(f"[INFO] Log written to: {MERGE_LOG_FILE}")


if __name__ == "__main__":
    merge_country_files()
