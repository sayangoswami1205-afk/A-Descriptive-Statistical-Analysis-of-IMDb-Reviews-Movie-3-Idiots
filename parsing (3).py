from playwright.async_api import async_playwright
from playwright_stealth import Stealth
from bs4 import BeautifulSoup
import pandas as pd
import asyncio

async def save_login_session():
    async with Stealth().use_async(async_playwright()) as p:
        
        browser = await p.chromium.launch(
            headless=False,
            executable_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        )
        
        USER_AGENT = (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/137.0.0.0 Safari/537.36"
        )

        context = await browser.new_context(
            user_agent=USER_AGENT
        )
        
        page = await context.new_page()
        
        print("Opening IMDb login page in Stealth Mode...")
        await page.goto("https://www.imdb.com/registration/signin")
        
        print("⏳ You have 60 seconds to log in manually using Google...")
        await page.wait_for_timeout(60000)
        
        print("Saving your session cookies...")
        await context.storage_state(path="imdb_session.json")
        
        await browser.close()
        print("✅ Session saved successfully to 'imdb_session.json'!")

# Run the generator
asyncio.run(save_login_session())

url = "https://www.imdb.com/title/tt1187043/reviews/"

async def scroll_and_fetch_html():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=False,
            executable_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        )
        
        USER_AGENT = (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/137.0.0.0 Safari/537.36"
        )

        context = await browser.new_context(
            user_agent=USER_AGENT, 
            storage_state="imdb_session.json"
        )
        
        page = await context.new_page()
        
        print("Loading page as an authenticated user...")
        await page.goto(url)
        
        # THE FIX: Explicitly wait for the body to exist and let React settle
        print("Waiting for the page to physically render...")
        await page.wait_for_selector("body", timeout=15000)
        await page.wait_for_timeout(3000)
        
        print("Starting dynamic scroll to load ALL reviews...")
        
        previous_count = 0
        retries = 0
        
        while True:
            # THE FIX: A safer javascript scroll that won't crash if the body temporarily vanishes
            await page.evaluate("if (document.body) window.scrollTo(0, document.body.scrollHeight)")
            await page.wait_for_timeout(2000) 
            
            try:
                load_more_button = page.locator('button.ipc-see-more__button, button:has-text("more"), button:has-text("See all")').first
                if await load_more_button.is_visible(timeout=1000):
                    await load_more_button.click()
                    await page.wait_for_timeout(2000)
            except Exception:
                pass 
                
            current_cards = page.locator('.ipc-list-card, .review-container, article')
            current_count = await current_cards.count()
            
            if current_count == previous_count:
                retries += 1
                if retries >= 3:
                    print("Reached the absolute bottom of the page!")
                    break
            else:
                print(f"Loaded {current_count} reviews on screen so far...")
                retries = 0 
                previous_count = current_count
        
        print("Grabbing raw HTML for lightning-fast parsing...")
        html_content = await page.content()
        await page.close()

        await browser.close()
        return html_content

# 1. Use Playwright to load the page
raw_html = asyncio.run(scroll_and_fetch_html())

# 2. Use BeautifulSoup to extract the data instantly in memory
print("Parsing data with BeautifulSoup...")
soup = BeautifulSoup(raw_html, 'html.parser')

data = []
all_cards = soup.find_all(['div', 'article'], class_=lambda c: c and ('ipc-list-card' in c or 'review-container' in c))

for card in all_cards:
    # Silver Bullet Filter: Must have a review permalink
    review_link = card.find('a', href=lambda h: h and '/review/rw' in h)
    if not review_link:
        continue # Skip this card if it's an ad or sidebar
        
    # UPDATED: Username (Targeting the specific antialiased/text-ellipsis span)
    user_span = card.find('span', class_=lambda c: c and 'text-ellipsis' in c and 'whitespace-nowrap' in c)
    username = user_span.text.strip() if user_span else "Unknown"
    
    # UPDATED: Review Title (Targeting the h3 tag directly)
    title_h3 = card.find('h3', class_='ipc-title__text')
    title = title_h3.text.strip() if title_h3 else "Title not found"
    
    # Rating (Unchanged)
    rating_span = card.find('span', class_=lambda c: c and 'ipc-rating-star--rating' in c)
    if not rating_span:
        rating_span = card.find('span', class_='ipc-rating-star--rating')
    rating = rating_span.text.strip() if rating_span else "No Rating"
    
    # UPDATED: Review Text (Targeting the exact inner div)
    text_div = card.find('div', class_='ipc-html-content-inner-div')
    review_text = text_div.text.strip() if text_div else "Text not found"
    
    data.append({
        'Username': username,
        'Rating': rating,
        'Review Title': title,
        'Review Text': review_text
    })

# 3. Create DataFrame
df = pd.DataFrame(data)
print(f"🎉 Success! Created DataFrame with {len(df)} reviews.")

df.to_csv('3_idiots_reviews.csv', index=False)