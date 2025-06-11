import json
import os

# Base image URL (your IPFS URL for images)
# Ensure this is a clean URL without unnecessary prefixes
base_image_url = "http://bafybeiey5pkgz2whufsio4d6w3ktntjrxwkzxp5zwzilj6r5vkg5kd3a5e.ipfs.localhost:8080/"

# Output folder for metadata files
output_folder = "metadata_with_traits"

# Traits for each NFT
traits = [
    "Rogue Sniper", "Indigenous Warrior", "Orc Lord", "Mr Alligator", "Transcendent", "Quad Hero", 
    "Basel Libre", "Midnight", "Demon Lord", "Genie", "Slime", "Steampunk", "Mummy", "Blacksmith", 
    "Illusion Jumpsuit", "God of War", "Mercenary", "Chef", "Superhero", "Tigaar", "Orion", "Ronin", 
    "Feral Sorcerer", "Kitten", "Cow", "Bee", "Flame On", "Designer", "Angel", "Cactus", "Roman Emperor", 
    "Assassin", "Guide of Darkness", "Thing", "Rupert", "Machinist", "Ghost", "Formal", "Mouse", "Penguin", 
    "Snow Monk", "Kawaii", "Bunni", "Panda", "Martial Fighter", "Adventurer", "Peacekeeper", "Arcane", 
    "Mewew", "Red Moon Ninja", "Steampunk Spinner", "Roman Gladiator", "Shark", "Ninjitsu", "Dev", "Archer", 
    "Paladin", "Archaeologist", "Last Samurai", "Barbarian", "Pharaoh", "Ancient King", "Sun Wu Kong", 
    "Vampire", "Wizard", "Sultan", "Thor", "Awakened", "Pizza Lover", "Tribe King", "Mineseeker", "Sage", 
    "Dragoon", "Kaisen", "Chita", "Baseliodas", "Gon", "Mashle", "Jojo", "Koro Sensei", "Choppy", "Umaru", 
    "Eri", "Psycho", "Pepe", "Saitamo", "Chika", "Nezuki", "Konichiwa Kitty", "Imp", "Mime", "Luppy", 
    "Bastar", "Pup", "Oink", "Elephant", "Pandoor", "Water Bendoor", "FED", "Dragon King"
]

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Generate metadata for each token
for token_id, trait in enumerate(traits, start=1):
    metadata = {
        "name": f"NFT #{token_id}",  # Replace "NFT" with your collection name if needed
        "description": "A unique NFT from a collection of digital assets.",  # Update with your collection's description
        "image": f"{base_image_url}{token_id}.png",  # Generate correct image URL
        "attributes": [
            {"trait_type": "Identity", "value": trait}  # Add additional traits as needed
        ]
    }
    # Save metadata to file
    with open(f"{output_folder}/{token_id}.json", "w") as f:
        json.dump(metadata, f, indent=4)

print(f"Metadata files generated in '{output_folder}' folder.")
