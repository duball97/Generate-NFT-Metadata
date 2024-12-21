import json
import os
import random

# Base image URL (your IPFS URL for images)
# Replace YOUR_IPFS_URL with your IPFS folder's URL where images are hosted
base_image_url = "http://YOUR_IPFS_URL/"

# Output folder for metadata files
output_folder = "metadata_with_traits"

# Note: For detailed customization instructions, read the README file in this repository.

# Define possible traits
backgrounds = ["Blue", "Red", "Green", "Purple", "Yellow"]
bodies = ["Robot", "Alien", "Human", "Animal"]
accessories = ["Hat", "Glasses", "Scarf", "Watch"]
expressions = ["Happy", "Angry", "Neutral", "Excited"]

# Total number of NFTs
num_nfts = 100  # Change this to your collection size

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Generate metadata for each token
for token_id in range(1, num_nfts + 1):
    metadata = {
        "name": f"NFT #{token_id}",
        "description": "A unique NFT from a customizable collection.",
        "image": f"{base_image_url}{token_id}.png",  # Assumes images are named sequentially
        "attributes": [
            {"trait_type": "Background", "value": random.choice(backgrounds)},
            {"trait_type": "Body", "value": random.choice(bodies)},
            {"trait_type": "Accessory", "value": random.choice(accessories)},
            {"trait_type": "Expression", "value": random.choice(expressions)}
        ]
    }
    
    # Save metadata to file
    with open(f"{output_folder}/{token_id}.json", "w") as f:
        json.dump(metadata, f, indent=4)

print("Metadata files generated in 'metadata_with_traits' folder.")
print("For detailed customization instructions, please refer to the README file.")
