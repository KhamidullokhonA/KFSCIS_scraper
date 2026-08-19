import requests
import pandas as pd
import os


output_path = os.path.expanduser("~/Desktop/faculty_members.csv")

BASE_URL = "https://www.cis.fiu.edu/wp-json/wp/v2/staff-member"

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://www.cis.fiu.edu/faculty-staff/",
}

def scrape_faculty():
    professors = []
    page_number = 1

    while True:

        url = f"{BASE_URL}?page={page_number}"

        page = requests.get(url, headers = HEADERS)
        
        if page.status_code != 200:
            break
            
        data = page.json()
        if not data:
            break

        for professor in data:
            if not {543, 544, 545,549, 550, 551}.isdisjoint(professor["staff-member-category"]):
                professors.append({"Name": professor["title"]["rendered"].strip(), "Title": professor["metadata"]["title"][0], "Email": professor["metadata"]["email"][0]})
                
        page_number+=1

    return professors

def main():
    professors = scrape_faculty()
    df = pd.DataFrame(professors)

    df.to_csv(output_path, index = False, encoding = 'utf-8')

    print(f"Scraped {len(df)} faculty members.")
    print("Saved to faculty_members.csv")

if __name__ == "__main__":
    main()

