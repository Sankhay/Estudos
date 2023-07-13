import asyncio
from playwright.async_api import async_playwright

auth = 'brd-customer-hl_41d05ae4-zone-scraping_browser-country-br:31cmz2h2c8ty'
browser_url = f'wss://{auth}@brd.superproxy.io:9222'

async def main():
    async with async_playwright() as pw:
        print('connecting')
        browser = await pw.chromium.connect_over_cdp(browser_url)
        print('connected')
        page = await browser.new_page()
        print('goto')
        await page.goto('https://www.carrosnaweb.com.br/fichadetalhe.asp?codigo=17949', timeout=120000)
        print('done, evaluating')

        # Wait for any dynamic content to load
        await page.wait_for_load_state()

        # Get the page content
        page_content = await page.evaluate('() => document.documentElement.outerHTML')

        # Check if the specific error message is present in the page content
        error_message = '<br><br><br>'
        if error_message not in page_content:
            print(page_content)  # Print the HTML content of the page

        await browser.close()

asyncio.run(main())



