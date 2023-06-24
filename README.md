# Frequency Dictionary Scraper

📚🔍🚀 This Python script scrapes a frequency dictionary of German words from the Wiktionary website and saves the data to a text file.

## Installation

To run the script, you need to have Python 3 installed on your system. Additionally, you need to install the following dependencies:

- requests
- beautifulsoup4

You can install the dependencies by executing the following command in your terminal:

pip install requests bs4

## Usage

1. Clone the repository or download the script file `frequency_dictionary_scraper.py`.

2. Open the terminal and navigate to the directory where the script is located.

3. Run the following command to execute the script:

python frequency_dictionary_scraper.py

The script will start scraping the frequency dictionary from the specified URLs and save the data to a file named `frequency_dictionary.txt`.

⏳ Wait for the script to complete the scraping process. It will pause for a short time between each request to avoid overloading the server.

Once the script finishes, you can find the generated `frequency_dictionary.txt` file in the same directory as the script.

**Note:** Please be aware that web scraping may be subject to the terms of service of the website you are scraping from. Make sure to respect the website's policies and do not overload the server with too many requests.

🚀 Happy scraping! 📚🔍

Additional Information: We used the frequency dictionaries from https://en.wiktionary.org/wiki/User:Matthias_Buchmeier#German_frequency_list for testing purposes.