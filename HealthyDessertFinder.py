from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

url = "https://www.eastewart.com/recipes-and-nutrition/heart-healthy-desserts/"

ing1 = input("Enter your 1st Ingredient: ").lower()
ing2 = input("Enter your 2nd Ingredient: ").lower()

STAPLES = ["salt", "pepper", "white sugar", "oil", "vanilla extract", "butter", "flour", "baking powder", "baking soda", "water"]
user_pantry = [ing1] + [ing2] + STAPLES

with sync_playwright() as p: #start playwright, define it as p
    browser = p.chromium.launch(headless=False) #open the browser (chrome)
    page = browser.new_page() #open tab
    page.goto(url, wait_until="domcontentloaded") #go to the website page

    recipe_links = page.get_by_role("link", name="GET THE RECIPE").evaluate_all(
        "(links) => links.map(link => link.href)"
    ) #so this is getting all the recipe links from the page

    matches = []

    for recipe in recipe_links:
        try:
            page.goto(recipe, wait_until="domcontentloaded", timeout=6000)
            page.wait_for_timeout(2000) #timeouts help avoid like those automated browsing blockers or whatever

            body_text = page.locator("body").inner_text().lower()

            if "access issue" in body_text: #important for debugging and stopping this from crashing every time it reaches a link which crashes
                print("Blocked by the website:", recipe)
                continue

            recipe_name = page.locator("h1").inner_text(timeout=10000)
            ingredients_content = page.locator(".wprm-recipe-ingredients").inner_text(timeout=10000).lower()

            if (ing1 in ingredients_content) and (ing2 in ingredients_content):
                matches.append((recipe_name, recipe))
                print(f"Found {len(matches)} recipes so far...")
        except Exception as e:
            print(f"Failed to get {recipe}.") #also important for debugging, understanding which recipe links won't open
            print(e)


    browser.close() #closes the browser window

    print("Following are the best matching recipes: ")
    if matches == []:
        print("Sorry, no recipes found!")
    else:
        for name, alink in matches:
            print(f"Dessert: {name}")
            print(f"Link to recipe: {alink}")

#this project uses solely playwright, because BeautifulSoup is a HTML scraper, so it can't open up links and stuff