# Google Search Scraper

This repository contains a Python script to scrape Google search results using Selenium. The script retrieves titles, links, and descriptions for a specified number of search results and prints them to the terminal with colored output, using the `colorama` library.

---

## Features
- **Scrapes Google Search Results**: Extracts titles, links, and descriptions from Google search results.
- **Customizable Number of Results**: Specify how many results to retrieve.
- **Error Handling**: Handles missing titles, links, or descriptions gracefully with fallback messages.
- **Colorized Output**: Displays results in a visually appealing format using colors.

---

## Requirements
- Python 3.7 or higher
- Google Chrome browser
- [Chromedriver](https://sites.google.com/a/chromium.org/chromedriver/) (compatible with your Chrome version)

### Python Libraries
Install the required libraries using:
```bash
pip install selenium colorama
```

---

## Usage

### Setting Up Chromedriver
1. Download the appropriate Chromedriver for your Chrome version from [here](https://sites.google.com/a/chromium.org/chromedriver/).
2. Replace the `path` variable in the script with the path to your Chromedriver executable.

### Running the Script
1. Clone this repository:

   ```bash
   git clone https://github.com/M-SaiCharan/Google-Search-Scraper.git
   cd Google-Search-Scraper
   ```
   
3. Run the script:

   ```bash
   python main.py
   ```
   

---

## Output Example

When you run the script, you will see output like this:

```
Result 1:
Title       : Welcome to Python.org
Link        : https://www.python.org
Description : The official website of the Python Programming Language, featuring downloads, tutorials, and more.

----------------------------------------

Result 2:
Title       : Python Programming Language - Wikipedia
Link        : https://en.wikipedia.org/wiki/Python_(programming_language)
Description : Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum...

----------------------------------------
```

---

## Limitations
- **Dynamic Content**: Google’s structure may change over time, potentially breaking the script. If this happens, inspect the page elements and update the CSS selectors in the script.
- **No Official API**: This script does not use the official [Google Custom Search JSON API](https://developers.google.com/custom-search/v1/introduction). Use at your own discretion.

---

## Contributing
Feel free to fork the repository and submit pull requests for improvements.

---

## Disclaimer
This script is intended for educational purposes only. Scraping Google without permission may violate their [Terms of Service](https://policies.google.com/terms). Use responsibly.
