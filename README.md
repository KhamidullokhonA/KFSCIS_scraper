# FIU CS Faculty Scraper

A small Flask app that scrapes the current faculty roster from the FIU School of Computing & Information Sciences website and displays it as a searchable directory.

## What it does

- Pulls faculty data live from FIU's public WordPress REST API (`cis.fiu.edu/wp-json/wp/v2/staff-member`)
- Filters entries down to specific staff categories (professors, associate/assistant professors, lecturers)
- Serves a web page where you can trigger the scrape, browse results as cards, search/filter by name or title, and export the results to CSV

## Project structure

```
fiu_scraper_python/
├── app.py              # Flask routes (/ and /scrape)
├── scraper_fiu.py       # Scraping logic + standalone CLI script
├── requirements.txt
├── templates/
│   └── index.html       # Frontend UI
└── .gitignore
```

## Setup

1. Clone the repo and navigate into it:
   ```
   git clone <your-repo-url>
   cd fiu_scraper_python
   ```

2. (Recommended) Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate      # macOS/Linux
   venv\Scripts\activate         # Windows
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the app:
   ```
   python app.py
   ```

5. Open `http://127.0.0.1:5000` in your browser and click **Run scrape**.

## Running the scraper standalone

You can also run the scraper directly from the command line, without the web app, to save results straight to a CSV:

```
python scraper_fiu.py
```

This saves `faculty_members.csv` to your Desktop by default (see `output_path` in `scraper_fiu.py` to change the destination).

## Notes

- The scraper stops automatically once it hits an empty page of results, so it doesn't depend on a hardcoded page count.
- Faculty category filtering is based on internal FIU staff-category IDs (`543, 544, 545, 549, 550, 551`). If FIU changes their site structure, these may need to be updated.
