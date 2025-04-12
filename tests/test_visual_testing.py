from playwright.sync_api import Page

# visual testing
def test_visual_snapshot(page: Page, base_url: str):
    page.goto(base_url)
    page.screenshot(path="snapshots/homepage.png", full_page=True)