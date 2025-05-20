import os
import importlib.util
import re

CREATURE_FOLDER = "creatures_submissions"
OUTPUT_FILE = "creature_data.py"

def simplify_id(class_period, name, counter):
    short_name = re.sub(r'[^a-zA-Z0-9]', '', name.lower())[:3]
    return f"{class_period}_{short_name}{counter}"

def load_creature_from_file(filepath):
    spec = importlib.util.spec_from_file_location("creature_module", filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    creature = module.creature  # expects each file to define a `creature` dict
    return creature

def serialize_creature_dict(creature):
    # Serialize a creature dictionary into valid Python syntax
    lines = ["{"]
    for k, v in creature.items():
        if isinstance(v, str):
            lines.append(f'        "{k}": "{v}",')
        elif isinstance(v, dict):
            lines.append(f'        "{k}": {{')
            for sk, sv in v.items():
                lines.append(f'            "{sk}": {sv},')
            lines.append("        },")
        else:
            lines.append(f'        "{k}": {v},')
    lines.append("    }")
    return "\n".join(lines)

def main():
    all_creatures = {}
    name_counter = {}

    for filename in os.listdir(CREATURE_FOLDER):
        if filename.endswith(".py"):
            filepath = os.path.join(CREATURE_FOLDER, filename)
            try:
                creature = load_creature_from_file(filepath)
                name = creature["name"]
                class_period = creature.get("class_period", "0")

                # Track duplicates
                base_key = f"{class_period}_{name}"
                name_counter[base_key] = name_counter.get(base_key, 0) + 1
                id_val = simplify_id(class_period, name, name_counter[base_key])

                # Assign simplified ID and ensure boost flag
                creature["id"] = id_val
                creature["terrain_boost_used"] = False

                all_creatures[id_val] = creature
                print(f"✔️ Loaded {name} as ID: {id_val}")
            except Exception as e:
                print(f"❌ Error loading {filename}: {e}")

    # Write the combined file
    with open(OUTPUT_FILE, "w") as f:
        f.write("# Auto-generated creature data\n")
        f.write("creatures = {\n")
        for cid, creature in all_creatures.items():
            f.write(f'    "{cid}": {serialize_creature_dict(creature)},\n')
        f.write("}\n")

    print(f"\n✅ Saved all {len(all_creatures)} creatures to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
