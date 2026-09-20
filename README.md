# Python Automation Scripts
 Collection of small Automation tools iI built to learn practiacl python -File Handling,Web Scraping,Report Generation and Scheduling.
#  Scriptsgn### rename_files.py
Renames every file in a given folder by prepending today's date.
```bash
python rename_files.py
```

### scraper.py
Scrapes book titles, prices, and ratings from books.toscrape.com and saves 
them to a CSV. URL and output filename are configurable via CLI arguments.
```bash
python scraper.py --url <target_url> --output <filename.csv>
```
**Note:** the URL/output are flexible, but the HTML selectors are currently 
written specifically for books.toscrape.com's page structure. To scrape a 
different site, the `find_all()` selectors need to be updated to match that 
site's HTML.

### report_generator.py
Reads a CSV and generates a formatted Excel report with bold headers, 
auto-sized columns, and a total row.
```bash
python report_generator.py
```

## Scheduling
scraper.py can be scheduled to run daily via cron or Task Scheduler, so it 
runs automatically without manual triggering.
Example cron line: `0 9 * * * python3 scraper.py --url ... --output ...`
 
### bot.py
A Discord bot with a `!remind` command that echoes back a reminder message.
Includes graceful error handling for missing arguments and unknown commands.
```bash
python bot.py
```
Requires a `.env` file with `DISCORD_BOT_TOKEN=your_token_here`.

## Tech used
Python, requests, BeautifulSoup, openpyxl, argparse/Task Scheduler.lSoup, openpyxl, argparse,discord.py

