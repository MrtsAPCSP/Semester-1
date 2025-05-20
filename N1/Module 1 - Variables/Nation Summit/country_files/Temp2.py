# Build-a-Country Simulation Worksheet Template
# Replace the Example Values with your Countries

# Student Names and Class Info
student_name_1 = "Alice Johnson"      # Name 1 from worksheet
student_name_2 = "Bob Martinez"       # Name 2 from worksheet
date = "2025-05-16"                   # Date
class_period = 3                      # Period (int)

# STEP 1: Country Profile Setup
country_name = "Freedonia2"            # Country Name
country_slogan = "Freedom and Progress"  # Slogan or Motto
flag_colors_symbols = "Red, White, Blue; Eagle emblem"  # Flag Colors/Symbols
country_acronym = "FR2"               # 3 Letter Acronym (must be unique)

government_type = "Democracy"         # Government Type chosen from worksheet options
continent = "North America"           # Continent Preference chosen from list
climate_type = "Temperate"            # Climate Type chosen from options
terrain_type = "forest"               # ✅ NEW — Options: forest, desert, tundra, mountain, plains

country_size_description = "Medium"  # Country Size description (Small/Medium/Large)
exact_country_size = 450000           # Exact Size (int) in sq. km

# Natural Resources (2 or 3 chosen from worksheet list)
natural_resource_1 = "Timber"
natural_resource_2 = "Freshwater"
natural_resource_3 = "Coal"

# STEP 2: Base Values
population = 50000000                 # Population (int), e.g. 50 million
birth_rate = 2.5                     # Birth Rate in % (float)
death_rate = 1.2                     # Death Rate in % (float)
average_age = 30                     # Avg Age (int)
literacy_rate = 90                   # Literacy Rate in % (int)

# STEP 3: Economy & Taxes
tax_rate = 25                       # Tax Rate in % (int)
government_spending_pct = 40        # Gov Spending % of GDP (int)
unemployment_rate = 8               # Unemployment Rate in % (int)
income_inequality = 35              # Income Inequality (0-100 int)

# STEP 4: Technology & Research
research_cybersecurity = 20          # Research focus % for Cybersecurity (int)
research_renewable_energy = 25       # Renewable Energy (int)
research_ai_development = 15         # AI Development (int)
research_military_tech = 20           # Military Tech (int)
research_health_biotech = 20          # Health & Biotech (int)

technology_level = 65                 # Technology Level (int 0-100) calculated based on rules

# STEP 5: Military & Diplomacy
military_aggressiveness = "Balanced"  # Military Aggressiveness chosen from options
will_defend_allies = True             # Will defend allies if attacked (bool)
will_join_ally_wars = False           # Will join ally's wars (bool)
prioritizes_peace_talks = True        # Prioritizes peace talks (bool)
will_spy_on_allies = False            # Will spy on allies (bool)
will_break_treaties_for_survival = False  # Will break treaties for survival (bool)

military_spending_pct = 15            # Military Spending % of GDP (int)
cyber_attack_strength = 70            # Cyber Attack Strength (int 0-100)
nuclear_weapons = True                # Nuclear Weapons (bool)

# Enemy and Ally Countries (up to 3 each, stored as separate string variables)
enemy_country_1 = "Ruritania"
enemy_country_2 = "Zubrowka"
enemy_country_3 = ""

ally_country_1 = "Elbonia"
ally_country_2 = "Genovia"
ally_country_3 = ""

# STEP 6: Trade & Global Impact
trade_policy = "Free Trade"           # Trade Policy chosen from options
trade_partner_1 = "Elbonia"           # Trade Partner 1
trade_partner_2 = "Genovia"           # Trade Partner 2
trade_partner_3 = ""                  # Trade Partner 3 (empty if none)

final_trade_openness = 65             # Final Trade Openness Score (int)

soft_power_score = 70                 # Soft Power Score (int 0-100)

# STEP 7: Environmental Impact
energy_source = "Wind/Solar"          # Energy Source chosen from options
environmental_impact_score = 15       # Environmental Impact Score (int) calculated

# STEP 8: Final Attributes
cultural_value_1 = "Freedom"          # Cultural Identity Value 1
cultural_value_2 = "Innovation"       # Cultural Identity Value 2
cultural_value_3 = "Nature"           # Cultural Identity Value 3


# === Calculations below (do not edit input variables above) ===

# Map government type efficiency and happiness impacts
gov_efficiency_map = {
    "military_dictatorship": 0.9,
    "democracy": 1.1,
    "authoritarian": 0.95,
    "monarchy": 1.0,
    "communist": 0.85
}

gov_happiness_map = {
    "military_dictatorship": -10,
    "democracy": 10,
    "authoritarian": -5,
    "monarchy": 0,
    "communist": -8
}

gov_military_multiplier_map = {
    "military_dictatorship": 1.3,
    "democracy": 1.0,
    "authoritarian": 1.1,
    "monarchy": 1.05,
    "communist": 1.15
}

gov = government_type.lower()
gov_efficiency = gov_efficiency_map.get(gov, 1.0)
gov_happiness = gov_happiness_map.get(gov, 0)
gov_military_multiplier = gov_military_multiplier_map.get(gov, 1.0)

# Resources impact: Simple average from presence of 3 resources (scale 0-10)
resource_value_map = {
    "timber": 7,
    "freshwater": 8,
    "coal": 6,
    "oil": 9,
    "natural_gas": 8,
    "gold": 7,
    "diamonds": 7,
    "iron": 6,
    "uranium": 8,
    "none": 0
}

resource_scores = [
    resource_value_map.get(natural_resource_1.lower(), 0),
    resource_value_map.get(natural_resource_2.lower(), 0),
    resource_value_map.get(natural_resource_3.lower(), 0),
]

average_resource_score = sum(resource_scores) / max(len([r for r in resource_scores if r > 0]), 1)

# Country size factor (based on exact size)
# Normalize exact_country_size to millions sq km for scale effect
country_size_millions = exact_country_size / 1_000_000

# Technology scale 0-100 normalized for formulas (0 to 10)
tech_scale = technology_level / 10

# Military Personnel (assumed from population)
# Approximate military personnel = 0.5% of population as base
military_personnel = population * 0.005

# Nuclear weapons count for military strength calculation (assume True = 3 nukes, False = 0)
nuclear_count = 3 if nuclear_weapons else 0

# Calculate Military Strength
military_strength = int(
    military_personnel
    * gov_military_multiplier
    * (1 + tech_scale * 0.1)
    * (1 + 0.5 * nuclear_count)   # 50% strength boost per nuclear weapon
    * (country_size_millions ** 0.5)
)

# Calculate GDP influenced by resources, tech, gov efficiency, country size, tax rate, government spending, unemployment, inequality
base_gdp = 250_000_000_000

resource_factor = 1 + (average_resource_score * 0.1)
tech_factor = 1 + (tech_scale * 0.15)
size_factor = country_size_millions ** 0.8
tax_penalty = 1 - (tax_rate * 0.003)  # higher tax slightly reduces GDP
gov_spending_bonus = 1 + ((government_spending_pct - 30) * 0.005)  # Spending >30% boosts economy slightly
unemployment_penalty = 1 - (unemployment_rate * 0.01)
inequality_penalty = 1 - ((income_inequality / 100) * 0.02)

GDP = int(base_gdp * gov_efficiency * resource_factor * tech_factor * size_factor *
          tax_penalty * gov_spending_bonus * unemployment_penalty * inequality_penalty)

# Calculate Happiness Index
happiness_index = (
    50
    + gov_happiness
    + (average_resource_score * 2)
    + (tech_scale * 1.5)
    + (literacy_rate / 10)
    - (unemployment_rate * 1.5)
    - ((income_inequality / 100) * 20)
    - (abs(average_age - 35) * 0.7)  # peak happiness at age 35
)

# Clamp happiness index to 0-100 range
happiness_index = max(0, min(100, happiness_index))

# Calculate Environmental Impact Score - normalized and influenced by energy source and government spending on environment
energy_impact_map = {
    "coal": 80,
    "oil": 75,
    "natural_gas": 50,
    "nuclear": 30,
    "wind/solar": 10,
    "hydroelectric": 15,
    "none": 50
}

energy_impact = energy_impact_map.get(energy_source.lower(), 50)
env_spending_factor = 1 - ((government_spending_pct - 30) * 0.01)  # Spending more on government reduces impact

environmental_impact_score = int(energy_impact * env_spending_factor)
environmental_impact_score = max(0, min(100, environmental_impact_score))


# Output summary for worksheet use:
print(f"--- {country_name} ({country_acronym}) Summary ---")
print(f"Population: {population:,}")
print(f"Government Type: {government_type} (Efficiency Multiplier: {gov_efficiency:.2f})")
print(f"Country Size: {exact_country_size} sq km ({country_size_description})")
print(f"Natural Resources Avg Score: {average_resource_score:.2f}")
print(f"Technology Level: {technology_level}")
print(f"Military Strength: {military_strength:,}")
print(f"GDP (in billions USD): ${GDP / 1_000_000_000:.2f}B")
print(f"Happiness Index (0-100): {happiness_index:.1f}")
print(f"Environmental Impact (0-100): {environmental_impact_score}")
print(f"Flag Description: {flag_colors_symbols}")
print(f"Cultural Values: {cultural_value_1}, {cultural_value_2}, {cultural_value_3}")
