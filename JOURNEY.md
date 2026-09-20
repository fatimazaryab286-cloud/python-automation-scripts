# Learning Journey

A day-by-day log of building this repo, part of a self-directed plan to 
learn practical Python automation.

## Day 1 — File Renaming
Built `rename_files.py` — takes a folder path and renames every file in 
it by prepending today's date. First time using Python's `os` module for 
file operations.

## Day 2 — Web Scraping
Built `scraper.py` using `requests` and `BeautifulSoup` to scrape book 
titles, prices, and ratings from books.toscrape.com, saved to CSV.

## Day 3 — Excel Reports
Built `report_generator.py` using `openpyxl` — reads the scraper's CSV 
output and generates a formatted `.xlsx` report with bold headers and 
auto-sized columns.

## Day 4 — CLI Tool + Scheduling
Refactored `scraper.py` to accept `--url` and `--output` as command-line 
arguments using `argparse`, instead of hardcoded values. Set up scheduled 
daily execution via [cron / Task Scheduler]. Learned that flexible CLI 
inputs don't mean the scraper works on *any* site — the HTML selectors 
are still specific to books.toscrape.com's structure.

## ## Day 5 — Discord Bot
Built a Discord bot using discord.py with a `!remind` command, structured
inside its own `discord-bot/` subfolder with a separate `.env` and 
`.gitignore`. Learned about Discord's intents system, event-driven 
programming (on_ready, on_command_error), and how to handle errors 
gracefully instead of letting the bot crash on bad input.