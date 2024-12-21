# How to Upload an NFT Collection for Free on IPFS

### Steps:

1. **Fork the Repository**
   - Fork this repository to your GitHub account.

2. **Download Python**
   - Install Python from the official website: [Download Python](https://www.python.org/downloads/).

3. **Install IPFS Desktop App**
   - Download and install the IPFS Desktop App:  
     [IPFS Desktop App](http://bafybeig2htkx6trji2aast7x6bdymzdgm4gc4ouvp25n7fufr55nitci3y.ipfs.localhost:8080/).

4. **Import Your NFT Images**
   - Open the IPFS Desktop app.
   - Go to **Files** and click **Import**.
   - Import the folder containing your NFT images.  
     **Note**: This script works for collections numbered sequentially (e.g., `1.png`, `2.png`, etc.).

5. **Share the IPFS Link**
   - Click the three-dot button next to the folder and select **Share Link**.
   - Copy the link.

6. **Update the Python Script**
   - Open the `generate_metadata.py` script.
   - Replace the `base_image_url` with the IPFS link you copied.  
     - **If your link is flagged in the browser**, replace `dweb.link` in the URL with `.ipfs.localhost:8080/`.
   - Customize the `traits` list with your own NFT traits.
   - Save the updated script.

7. **Run the Python Script**
   - Open your command prompt or terminal.
   - Navigate to the folder containing the script:
     ```bash
     cd your-folder
     ```
   - Run the script:
     ```bash
     python generate_metadata.py
     ```

8. **Upload Metadata Files to IPFS**
   - After running the script, a folder named `metadata_with_traits` will be created.
   - Open the IPFS Desktop app and import this folder.
   - Once uploaded, click **Share Link** and save the IPFS URL.

---

## Support
If this guide helped you, please consider giving this repository a ⭐!  
For any questions, feel free to reach out to me:  
- **Telegram**: [@duball69](https://t.me/duball69)  
- **Twitter (X)**: [@duball69](https://x.com/duball69)

---
