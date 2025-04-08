# =======================================================
# Name: Barthélemy Quentin
# GitHub: BlueHowl
# Year: 2025
# Description: Scrap informations on NYTimes with Playwright (performs faster than selenium)
# Sources : https://scrapfly.io/blog/web-scraping-with-playwright-and-python/
# =======================================================

from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

# auto close the resource when done
with sync_playwright() as pw:
    # create browser instance
    browser = pw.chromium.launch(headless=False) # set to True if you want to run in the background
    context = browser.new_context(viewport={"width": 800, "height": 600})
    
    page = context.new_page()
    page.goto("https://www.nytimes.com/")

    # wait for fides cookie banner to appear
    page.wait_for_selector("#fides-banner")

    context.add_cookies([
        {
            'name' : 'fides_consent',
            'value' : '%7B%22consent%22%3A%7B%7D%2C%22identity%22%3A%7B%22fides_user_device_id%22%3A%22fc660568-3ec2-42ea-8320-35e830640263%22%7D%2C%22fides_meta%22%3A%7B%22version%22%3A%220.9.0%22%2C%22createdAt%22%3A%222025-03-25T09%3A02%3A30.940Z%22%2C%22updatedAt%22%3A%222025-03-25T09%3A03%3A01.645Z%22%2C%22consentMethod%22%3A%22reject%22%7D%2C%22tcf_consent%22%3A%7B%22system_consent_preferences%22%3A%7B%7D%2C%22system_legitimate_interests_preferences%22%3A%7B%7D%7D',
            'domain': '.nytimes.com',
            'path': '/'
        }
    ])

    page.reload()

    # Find the element with the class 'css-hqisq1' and click on the child button with JavaScript
    page.evaluate("""
        var parentElement = document.querySelector('.css-hqisq1'); 
        if (parentElement) {
            var button = parentElement.querySelector('button');  // Trouver le bouton dans cet élément
            if (button) {
                button.click();  // Cliquer sur le bouton
            } else {
                console.log('Bouton introuvable');
            }
        } else {
            console.log('Élément parent introuvable');
        }
    """)

    #extract article titles via beautifulsoup or use parsel
    soup = BeautifulSoup(page.content(), "html")
    all_titles = []
    for item in soup.select("section.story-wrapper a div.css-xdandi p"):
        if item.text != "":
            all_titles.append(item.text)

    print(all_titles)