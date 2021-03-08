from wiki_operations import find_country_links, get_holiday_details, get_country_name, NoWikiTableError
import csv

base_url = 'https://en.wikipedia.org/wiki/List_of_holidays_by_country'

links = find_country_links(base_url)
no_wikitables = []

with open('holidays.csv', 'w', newline='') as csvfile:
    holiwriter = csv.writer(csvfile)
    holiwriter.writerow(
        ['Country', 'Date', 'Descritpion #1', 'Description #2', 'Mess...'])
    for link in links:
        try:
            rec = get_holiday_details(link)
            for l in rec:
                holiwriter.writerow([get_country_name(link)] + l)
        except NoWikiTableError:
            no_wikitables.append(link)
            print(
                f'Can\'t find wikitable for country: {get_country_name(link)}')
            pass

with open('no_wikitables.csv', 'w') as wikifile:
    for c in no_wikitables:
        wikifile.write(c + '\n')
