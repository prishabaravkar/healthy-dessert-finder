Healthy Dessert Finder

A Python-based web scraping application that helps users find healthy dessert recipes using ingredients they already have.

The program asks the user to enter two ingredients, searches a healthy dessert website, and returns matching recipes that contain both ingredients. It then extracts and displays the complete recipe, including the ingredient list and preparation instructions.

DISCLAIMER: This project was created for educational and portfolio purposes. It is not affiliated with the website being scraped. Website structure and availability may change over time, and users should comply with the website’s terms of use.

Features:
    - Accepts two ingredients through command-line input
    - Automates website navigation using Playwright
    - Searches recipe listings for relevant results
    - Opens and extracts data from individual recipe pages
    - Filters recipes based on the user’s selected ingredients
    - Displays full ingredient lists and preparation instructions
    - Handles cases where no suitable recipe is found

Technologies Used:
- Python
- Playwright
- Browser automation
- Web scraping
- DOM element selection
- Command-line input and output

How It Works
1. The user enters two ingredients.
2. Playwright launches a browser and opens the target recipe website.
3. The program collects links to available dessert recipes.
4. Each recipe is checked to determine whether it contains both ingredients.
5. When a match is found, the program extracts the recipe title, ingredients, and instructions.
6. The complete recipe is displayed in the terminal.


--

Through this project, I gained experience with:
- Browser automation using Playwright
- Inspecting webpage structure and selecting DOM elements
- Extracting and processing data from multiple webpages
- Filtering scraped data based on user input
- Handling page-loading and element-selection issues
- Structuring a Python automation project

Limitations
- The scraper depends on the current structure of the target website.
- Changes to page layouts or element selectors may require updates to the code.
- Ingredient names may appear in different forms, which can affect matching accuracy.
- The tool currently runs through the command line.

Future Improvements
- Add approximate ingredient matching
- Allow users to enter more than two ingredients
- Rank recipes based on how closely they match the available ingredients
- Add dietary filters such as vegan, gluten-free, or high-protein
- Build a graphical or web-based interface
- Add automated tests for the scraping and filtering logic
- Export selected recipes to a text or PDF file
