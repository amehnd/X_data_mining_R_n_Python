
## WHY THE ERROR # what I know...


getting an empty JSON file because the code isn't correctly parsing actual tweet links or content from Google's search results. Google dynamically renders much of its content and obfuscates its HTML structure, making scraping difficult and unreliable without a proper headless browser setup

Google search results don't directly show tweet texts; they show links, and often tweet previews are not even in the main HTML returned from a requests.get call.

Google actively prevents scraping using rate-limiting, captchas, and obfuscation techniques.

