import json
import os
import random
from tabulate import tabulate



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MERGED_FILE = os.path.join(BASE_DIR, "merged_countries.json")

# Constants for thresholds
HAPPINESS_ATTACK_THRESHOLD = 20
HAPPINESS_COUP_THRESHOLD = 10

base_year = 2000  # or your chosen starting year
avg_age = 35.0    # starting average age, adjust as needed
round_number = 0  # initialize round counter


# War variables
num_wars = random.randint(1, 3)       # 0–3 wars possible
num_disasters = random.randint(0, 2)  # 0–2 disasters

round_number = 1  # Initialize global round number

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_countries(class_period):
    if not os.path.exists(MERGED_FILE):
        print(f"[ERROR] Merged countries JSON file not found: {MERGED_FILE}")
        return []

    with open(MERGED_FILE, "r") as f:
        all_countries = json.load(f)

    # Make sure user input is int and class_period in JSON is int,
    # so just filter by equality
    countries = [c for c in all_countries if c.get("class_period") == class_period]

    for c in countries:
        if "country_name" not in c:
            print(f"[ERROR] Missing 'country_name' in country data: {c}")

    return countries


def display_round(round_number, births, deaths):
    global avg_age
    current_year = base_year + 10 * round_number

    # Update average age
    if births > deaths:
        avg_age -= 1  # Decrease average age if births outnumber deaths
    else:
        avg_age += 1  # Increase average age otherwise

    # Separation line and banner
    print("\n")  # blank line for clarity
    print(f"===== ROUND {round_number} - Year: {current_year} =====")

    # Display round info
    print(f"Births: {births}")
    print(f"Deaths: {deaths}")
    print(f"Average Age: {avg_age:.1f}")

    # Wait for user input before moving on
    input("\nPress Enter to continue...")


def display_country_table(countries):
    table_data = []
    for c in countries:
        table_data.append([
            c.get("country_name", "Unknown"),
            c.get("population", "N/A"),
            round(c.get("happiness_index", 0), 2),
            round(c.get("military_strength", 0), 2),
            c.get("continent", "N/A"),
            c.get("government", "Unknown"),
            round(c.get("technology_level", 0), 2),
            c.get("terrain", "N/A"),
            round(c.get("average_age", 0), 2)
        ])

    headers = ["Country", "Population", "Happiness", "Military Strength", "Continent", "Government", "Tech Level", "Terrain", "Avg Age"]
    print(tabulate(table_data, headers=headers, tablefmt="pretty"))

def random_government():
    return random.choice(["Democracy", "Monarchy", "Dictatorship", "Communist", "Republic", "Theocracy"])

def coup_event(country):
    old_gov = country.get("government", "Unknown")
    new_gov = random_government()
    changes = []

    # Change government
    country["government"] = new_gov
    changes.append(f"Government changed from {old_gov} to {new_gov}")

    # Adjust military strength randomly +/- 20%
    old_military = country.get("military_strength", 1000)
    military_change = old_military * random.uniform(-0.2, 0.2)
    country["military_strength"] = max(0, old_military + military_change)
    changes.append(f"Military strength changed by {military_change:.0f} to {country['military_strength']:.0f}")

    # Adjust literacy rate +/- 10%
    old_literacy = country.get("literacy_rate", 70)
    literacy_change = random.uniform(-10, 10)
    country["literacy_rate"] = max(0, min(100, old_literacy + literacy_change))
    changes.append(f"Literacy rate changed by {literacy_change:.1f}% to {country['literacy_rate']:.1f}%")

    # Adjust birth rate +/- 1 per 1000
    old_birth_rate = country.get("birth_rate", 12)
    birth_rate_change = random.uniform(-1, 1)
    country["birth_rate"] = max(0, old_birth_rate + birth_rate_change)
    changes.append(f"Birth rate changed by {birth_rate_change:.2f} to {country['birth_rate']:.2f}")

    # Population loss due to coup and war
    pop_loss = int(country.get("population", 1000) * random.uniform(0.15, 0.30))  # 15%-30% loss
    old_population = country.get("population", 1000)
    country["population"] = max(0, old_population - pop_loss)
    changes.append(f"Population decreased by {pop_loss} due to coup/war")

    # Reset happiness to 50
    country["happiness_index"] = 50
    changes.append("Happiness reset to 50")

    return changes

def update_military_strength(country):
    # Military strength affected by tech, gov spending, and age demographics

    base_military = country.get("military_strength", 1000)
    tech_level = country.get("technology_level", 50)  # 0-100 scale
    gov_spending = country.get("government_spending_pct", 20)  # percentage
    average_age = country.get("average_age", 30)
    birth_rate = country.get("birth_rate", 12)  # per 1000

    # Military strength grows with tech and gov spending
    military_growth = (tech_level * 0.05) + (gov_spending * 0.1)

    # Military strength decreases with high average age (older population)
    age_penalty = max(0, (average_age - 35) * 5)  # penalty if avg age > 35

    # Population growth (births - deaths) influences military replenishment
    # If birth rate < death rate (death rate ~ pop loss?), military weakens
    # Simplify: birth rate threshold 12 as replacement level
    if birth_rate < 12:
        birth_penalty = (12 - birth_rate) * 10
    else:
        birth_penalty = 0

    new_military = base_military + military_growth - age_penalty - birth_penalty

    # Clamp to minimum 0
    country["military_strength"] = max(0, new_military)

def natural_disaster_event(countries, event_log):
    # Pick a random country weighted by population
    if not countries:
        return
    disaster_country = random.choices(
        countries,
        weights=[c.get("population", 1000) for c in countries],
        k=1
    )[0]

    country_name = disaster_country.get("country_name", "Unknown")
    terrain = disaster_country.get("terrain", "plains")
    continent = disaster_country.get("continent", "Unknown")

    # Define terrain-disaster mapping with likelihoods and impact
    terrain_disasters = {
        "mountains": ["earthquake", "avalanche"],
        "coast": ["hurricane", "tsunami"],
        "plains": ["tornado", "drought"],
        "desert": ["drought", "sandstorm"],
        "forest": ["wildfire", "storm"],
        "urban": ["earthquake", "fire"],
        "jungle": ["flood", "storm"],
    }

    possible_disasters = terrain_disasters.get(terrain.lower(), ["storm"])

    disaster = random.choice(possible_disasters)

    print(f"🌪️ Natural disaster ({disaster}) strikes {country_name} ({terrain})!")

    event_log.append(f"Natural disaster ({disaster}) struck {country_name}.")

    # Impact: population and happiness reduced, severity depends on disaster type
    severity_map = {
        "earthquake": 0.15,
        "avalanche": 0.10,
        "hurricane": 0.20,
        "tsunami": 0.25,
        "tornado": 0.10,
        "drought": 0.18,
        "sandstorm": 0.08,
        "wildfire": 0.12,
        "storm": 0.10,
        "flood": 0.15,
        "fire": 0.10,
    }

    severity = severity_map.get(disaster, 0.10)

    tech_level = disaster_country.get("technology_level", 50)
    gov = disaster_country.get("government", "Democracy")

    gov_efficiency = {
        "Democracy": 0.9,
        "Republic": 0.85,
        "Monarchy": 0.7,
        "Dictatorship": 0.6,
        "Communist": 0.65,
        "Theocracy": 0.7
    }

    efficiency = gov_efficiency.get(gov, 0.8)

    # Adjust severity by tech and gov efficiency
    adjusted_severity = severity * (1 - (tech_level / 200)) * efficiency

    pop_loss = int(disaster_country.get("population", 1000) * adjusted_severity)
    happiness_loss = int(20 * adjusted_severity * 2)


    disaster_country["population"] = max(0, disaster_country.get("population", 0) - pop_loss)
    disaster_country["happiness_index"] = max(0, disaster_country.get("happiness_index", 50) - happiness_loss)

    print(f"  Population decreased by {pop_loss}. Happiness decreased by {happiness_loss}.")

    # Neighbor help (simple): neighbors on same continent may help with 50% chance each
    neighbors = [c for c in countries if c.get("continent") == continent and c != disaster_country]

    for neighbor in neighbors:
        if random.random() < 0.5:
            help_pop_loss = int(pop_loss * 0.05)  # neighbors lose some population helping
            help_happiness_loss = 5
            neighbor["population"] = max(0, neighbor.get("population", 0) - help_pop_loss)
            neighbor["happiness_index"] = max(0, neighbor.get("happiness_index", 50) - help_happiness_loss)

            print(f"  Neighbor {neighbor['country_name']} helped {country_name} at cost of population {help_pop_loss} and happiness {help_happiness_loss}.")
            event_log.append(f"{neighbor['country_name']} helped {country_name} after natural disaster.")




def decide_war_action(country, opponent):
    """
    Decide whether the country attacks aggressively ('a') or defends ('d')
    based on attributes.
    """
    happiness = country.get("happiness_index", 50)
    military = country.get("military_strength", 1000)
    opponent_military = opponent.get("military_strength", 1000)
    government = country.get("government", "Democracy")

    # Base probabilities
    attack_prob = 0.5

    # Adjust based on happiness
    if happiness > 60:
        attack_prob += 0.3
    elif happiness < 30:
        attack_prob -= 0.3

    # Adjust based on military strength compared to opponent
    if military > opponent_military:
        attack_prob += 0.2
    else:
        attack_prob -= 0.2

    # Adjust based on government type
    if government in ["Dictatorship", "Monarchy"]:
        attack_prob += 0.2
    elif government == "Democracy":
        attack_prob -= 0.2

    # Clamp probability between 0 and 1
    attack_prob = max(0, min(1, attack_prob))

    # Make decision based on probability
    decision = "a" if random.random() < attack_prob else "d"
    return decision


def run_war(c1, c2, event_log):
    c1_name = c1.get("country_name", "Unknown")
    c2_name = c2.get("country_name", "Unknown")

    # Check happiness: If below threshold, cannot attack
    if c1.get("happiness_index", 0) < HAPPINESS_ATTACK_THRESHOLD:
        print(f"{c1_name} is too unhappy to attack.")
        event_log.append(f"{c1_name} too unhappy to attack, war avoided.")
        return False
    if c2.get("happiness_index", 0) < HAPPINESS_ATTACK_THRESHOLD:
        print(f"{c2_name} is too unhappy to attack.")
        event_log.append(f"{c2_name} too unhappy to attack, war avoided.")
        return False

    # Prompt each country for a decision
    decision_c1 = decide_war_action(c1, c2)
    decision_c2 = decide_war_action(c2, c1)

    print(f"{c1_name} chooses to {'Attack aggressively' if decision_c1 == 'a' else 'Defend'}.")
    print(f"{c2_name} chooses to {'Attack aggressively' if decision_c2 == 'a' else 'Defend'}.")

    # Calculate impact factors dynamically
    base_impact = {"a": 20, "d": 10}
    c1_impact = base_impact.get(decision_c1, 10)
    c2_impact = base_impact.get(decision_c2, 10)

    # Adjust by military strength ratio (if attacker much stronger, defender loses more)
    military_ratio_c1 = c1.get("military_strength", 1) / max(1, c2.get("military_strength", 1))
    military_ratio_c2 = c2.get("military_strength", 1) / max(1, c1.get("military_strength", 1))

    # Base population loss calculation
    c1_pop_loss = int(c2_impact * 1000 / military_ratio_c1)
    c2_pop_loss = int(c1_impact * 1000 / military_ratio_c2)

    # Adjust losses by technology (higher tech reduces losses)
    tech_c1 = c1.get("technology_level", 50)
    tech_c2 = c2.get("technology_level", 50)

    # Each tech point over 50 reduces loss by 0.5% (capped at 25%)
    tech_loss_mod_c1 = 1 - min(0.005 * max(0, tech_c1 - 50), 0.25)
    tech_loss_mod_c2 = 1 - min(0.005 * max(0, tech_c2 - 50), 0.25)

    c1_pop_loss = int(c1_pop_loss * tech_loss_mod_c1)
    c2_pop_loss = int(c2_pop_loss * tech_loss_mod_c2)

    # Apply population losses
    c1["population"] = max(0, c1.get("population", 1000) - c1_pop_loss)
    c2["population"] = max(0, c2.get("population", 1000) - c2_pop_loss)

    # **Calculate and apply military losses**
    # Let's say military losses are proportional to population losses but more severe
    # Military loss could be 30% greater than population loss scaled by military strength ratio and tech

    c1_military_loss = int(c1_pop_loss * 1.3 / military_ratio_c1)
    c2_military_loss = int(c2_pop_loss * 1.3 / military_ratio_c2)

    # Apply tech reduction to military loss (same modifier)
    c1_military_loss = int(c1_military_loss * tech_loss_mod_c1)
    c2_military_loss = int(c2_military_loss * tech_loss_mod_c2)

    # Update military strength, ensuring not below 0
    c1["military_strength"] = max(0, c1.get("military_strength", 1000) - c1_military_loss)
    c2["military_strength"] = max(0, c2.get("military_strength", 1000) - c2_military_loss)

    # Adjust happiness due to war losses (simple model)
    happiness_loss_c1 = int(c1_pop_loss / 100)  # e.g., 1 point happiness lost per 100 population lost
    happiness_loss_c2 = int(c2_pop_loss / 100)

    c1["happiness_index"] = max(0, c1.get("happiness_index", 50) - happiness_loss_c1)
    c2["happiness_index"] = max(0, c2.get("happiness_index", 50) - happiness_loss_c2)

    # Log and print results
    print(f"{c1_name} lost {c1_pop_loss} population and {c1_military_loss} military strength.")
    print(f"{c2_name} lost {c2_pop_loss} population and {c2_military_loss} military strength.")
    print(f"{c1_name} happiness decreased by {happiness_loss_c1}.")
    print(f"{c2_name} happiness decreased by {happiness_loss_c2}.")

    event_log.append(f"{c1_name} lost {c1_pop_loss} population and {c1_military_loss} military strength in war.")
    event_log.append(f"{c2_name} lost {c2_pop_loss} population and {c2_military_loss} military strength in war.")
    event_log.append(f"{c1_name} happiness decreased by {happiness_loss_c1} due to war.")
    event_log.append(f"{c2_name} happiness decreased by {happiness_loss_c2} due to war.")

    return True


def select_war_candidates(countries):
    potential_pairs = []

    for i in range(len(countries)):
        for j in range(i + 1, len(countries)):
            c1, c2 = countries[i], countries[j]
            same_continent = c1.get("continent") == c2.get("continent")
            avg_happiness = (c1.get("happiness_index", 50) + c2.get("happiness_index", 50)) / 2
            military_gap = abs(c1.get("military_strength", 0) - c2.get("military_strength", 0))
            aggression_bonus = 0

            if same_continent:
                aggression_bonus += 1.5
            if avg_happiness < 50:
                aggression_bonus += 1
            if military_gap > 100:
                aggression_bonus += 0.5

            # Weighted likelihood for war pair
            score = random.random() + aggression_bonus
            potential_pairs.append((score, c1, c2))

    # Sort by score descending
    potential_pairs.sort(reverse=True, key=lambda x: x[0])

    # Return top N candidates
    return potential_pairs[:3]


def run_round(countries, event_log):
    print("\nRunning a round...")

    war_triggered = random.random() < 0.5  # 50% chance
    disaster_triggered = random.random() < 0.5  # 50% chance

    if not war_triggered and not disaster_triggered:
        print("\n🕊️ Peaceful round. No war or disaster this time.")
        event_log.append("Peaceful round.")
        return

    if war_triggered:
        handle_war_phase(countries, event_log)

    if disaster_triggered:
        print("\n🌍 Natural disaster event triggered")
        natural_disaster_event(countries, event_log)

    input("\nPress Enter to continue...")
    clear_screen()


def handle_war_phase(countries, event_log):
    war_pairs = select_war_candidates(countries)
    if not war_pairs:
        print("Not enough countries for a war.")
        event_log.append("War skipped due to insufficient countries.")
        return

    for _, c1, c2 in war_pairs:
        success = run_war(c1, c2, event_log)
        if success:
            break  # Only one war per round; remove break to allow multiple wars




def show_status():
    print("\nStatus: All systems nominal. No ongoing conflicts or disasters.")



def main():
    class_period = int(input("Enter class period to load countries: "))
    countries = load_countries(class_period)

    if not countries:
        print("No countries loaded. Exiting.")
        return

    global round_number
    event_log = []

    while True:
        clear_screen()
        print(f"--- Starting Round {round_number} ---")

        births, deaths = 0, 0

        # Update military strength for each country
        for country in countries:
            update_military_strength(country)

        # Trigger random disasters
        for _ in range(num_disasters):
            natural_disaster_event(countries, event_log)

        # Trigger random wars
        for _ in range(num_wars):
            if len(countries) < 2:
                break
            c1, c2 = random.sample(countries, 2)
            war_occurred = run_war(c1, c2, event_log)
            if war_occurred:
                event_log.append(f"War between {c1['country_name']} and {c2['country_name']}")

        # Trigger coups if happiness is low
        for country in countries:
            if country.get("happiness_index", 50) < HAPPINESS_COUP_THRESHOLD:
                changes = coup_event(country)
                event_log.append(f"Coup in {country['country_name']}: " + ", ".join(changes))

        # Calculate births and deaths and update populations
        births, deaths = calculate_population_changes(countries)

        display_round(round_number, births, deaths)
        display_country_table(countries)

        print("\nEvents this round:")
        for event in event_log:
            print(" -", event)
        event_log.clear()

        round_number += 1

        cont = input("\nContinue to next round? (y/n): ").strip().lower()
        if cont != 'y':
            break


def display_country_stats(countries):
    """
    Displays a neatly formatted table with country stats like:
    Country | Population | Births | Deaths | Avg Age | Happiness | Military Strength
    """

    header = f"{'Country':<20} {'Population':>12} {'Births':>8} {'Deaths':>8} {'Avg Age':>8} {'Happiness':>10} {'Military':>10}"
    print("\n" + header)
    print("-" * len(header))

    for country in countries:
        name = country.get("country_name", "Unknown")
        population = country.get("population", 0)
        births = country.get("births", 0)
        deaths = country.get("deaths", 0)
        avg_age = country.get("avg_age", 0.0)
        happiness = country.get("happiness_index", 0)
        military = country.get("military_strength", 0)

        print(f"{name:<20} {population:>12,} {births:>8,} {deaths:>8,} {avg_age:>8.1f} {happiness:>10} {military:>10}")

    print()


def calculate_population_changes(countries):
    births = 0
    deaths = 0
    for country in countries:
        pop = country.get("population", 1000)
        birth_rate = country.get("birth_rate", 12)  # per 1000 people
        death_rate = 10  # fixed death rate per 1000 for simplicity

        country_births = int(pop * birth_rate / 1000)
        country_deaths = int(pop * death_rate / 1000)

        births += country_births
        deaths += country_deaths

        country["population"] = max(0, pop + country_births - country_deaths)

    return births, deaths


if __name__ == "__main__":
    main()
