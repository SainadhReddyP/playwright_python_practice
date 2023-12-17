import re
from playwright.sync_api import sync_playwright


def test_example():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False, args=["--start-maximized"])
        page = browser.new_page(no_viewport=True)
        # page = context.new_page()
        page.goto("https://sdetqaportal.blogspot.com/")
        title = page.title()
        print(title)
        page.screenshot(path="screenshots/example.png")
        browser.close()

# def test_has_title(page: Page):
#     browser = page.
#     page.goto("https://sdetqaportal.blogspot.com/")
#     expect(page).to_have_title(re.compile("Sainadh"))
