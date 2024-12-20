import json
import os

# Base image URL (your Pinata IPFS URL for images)
base_image_url = "gateway_url = \"http://bafybeiey5pkgz2whufsio4d6w3ktntjrxwkzxp5zwzilj6r5vkg5kd3a5e.ipfs.localhost:8080/\""



# Output folder for metadata files
output_folder = "metadata_with_traits"

# Traits for each NFT
traits = [
    "Rogue Sniper", "Indegenious Warrior", "Orc Lord", "Mr Alligator", "Transcendent", "Quad Hero", "Basel Libre",
    "Midnight", "Demon Lord", "Genie", "Slime", "Steampunk", "Mummy", "Blacksmith", "Illusion Jumpsuit", "God of War",
    "Mercenary", "Chef", "Superhero", "Tigaar", "Orion", "Ronin", "Feral Sorcerer", "Kitten", "Cow", "Bee", "Flame On",
    "Designer", "Angel", "Cactus", "Roman Emperor", "Assasin", "Guide of Darkness", "Thing", "Rupert", "Machinist",
    "Ghost", "Formal", "Mouse", "Penguin", "Snow Monk", "Kawaii", "Bunni", "Panda", "Martial Fighter", "Adventurer",
    "Peacekeeper", "Arcane", "Mewew", "Red Moon Ninja", "Steampunk Spinner", "Roman Gladiator", "Shark", "Ninjitsu",
    "Dev", "Archer", "Paladin", "Archaeologist", "Last Samurai", "Barbarian", "Pharaoh", "Ancient King", "Sun Wu Kong",
    "Vampire", "Wizard", "Sultan", "Thor", "Awakened", "Pizza Lover", "Tribe King", "Mineseeker", "Sage", "Dragoon",
    "Kaisen", "Chita", "Baseliodas", "Gon", "Mashle", "Jojo", "Koro Sensei", "Choppy", "Umaru", "Eri", "Psycho", "Pepe",
    "Saitamo", "Chika", "Nezuki", "Konichiwa Kitty", "Imp", "Mime", "Luppy", "Bastar", "Pup", "Oink", "Elephant",
    "Pandoor", "Water Bendoor", "FED", "Dragon King"
]

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Generate metadata for each token
for token_id, trait in enumerate(traits, start=1):
    metadata = {
        "name": f"Basel #{token_id}",
        "description": "Basel is a collection of 100 unique NFTs, each with its own identity.",
        "image": f"{base_image_url}{token_id}.png",
        "attributes": [
            {"trait_type": "Identity", "value": trait}
        ]
    }
    # Save metadata to file
    with open(f"{output_folder}/{token_id}.json", "w") as f:
        json.dump(metadata, f, indent=4)

print(f"Metadata files generated in '{output_folder}' folder.")
