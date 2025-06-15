import csv
import os

TEMPLATE_FILE = 'template.html'
CSV_FILE = 'shows.csv'
OUTPUT_FILE = 'index.html'

def load_shows(csv_file):
    html = ''
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            parts = [row['date'].strip()]
            if row['venue'].strip():
                parts.append(row['venue'].strip())
            if row['city'].strip():
                parts.append(row['city'].strip())
            text = " - ".join(parts)
            if row['link'].strip():
                html += f'    <br>\n    <li><a href="{row["link"].strip()}">{text}</a></li>\n'
            else:
                html += f'    <br>\n    <li>{text}</li>\n'

    html += '<br>'  # add one break at end
    return html

def build_page():
    with open(TEMPLATE_FILE, 'r', encoding='utf-8') as f:
        template = f.read()

    shows_html = load_shows(CSV_FILE)
    final_html = template.replace('<!-- SHOWS_PLACEHOLDER -->', shows_html)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(final_html)

    print(f'✅ index.html generated at: {OUTPUT_FILE}')

if __name__ == '__main__':
    build_page()
