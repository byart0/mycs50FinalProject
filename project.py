import sys
from datetime import datetime
import requests
import re
from collections import Counter
import csv
import time


def read_photos():
    with open("photos.txt", "r") as file:
        return [line.strip() for line in file.readlines()]


class Regex:
    @staticmethod
    def search_keywords(keyword):
        search = re.search(r"(_(.+)\.)", keyword)
        return search.group(2) if search else None

    @staticmethod
    def check_photos_by_date(name):
        check = re.search(r"(\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])_)", name)
        return check.group(0) if check else None


def log(n):
    def new_log(*args, **kwargs):
        last_spell = n.__name__.replace("_", " ")
        print(
            f"[{datetime.now().strftime('%Y-%m-%d, %H:%M:%S')}] 🧙 Young wizard chosed '{last_spell}' spell.🧙\n"
        )
        result = n(*args, **kwargs)
        print(
            f"[{datetime.now().strftime('%Y-%m-%d, %H:%M:%S')}] 🧙 '{last_spell}' spell is done.🧙\n"
        )
        return result

    return new_log


def open_meteo(photoDate):
    try:
        openweather = requests.get(
            f"https://api.open-meteo.com/v1/forecast?latitude=39.695&longitude=3.0176"
            f"&start_date={photoDate}&end_date={photoDate}&hourly=temperature_2m"
        )
        organize = openweather.json()
        temperature = organize["hourly"]["temperature_2m"][0]
        return temperature
    except requests.RequestException:
        print(" ❗💀 There is some problems in API spell. ❗💀")


@log
def search_keywords():
    valid_keywords = {
        "sunset",
        "sea",
        "beach",
        "friends",
        "selfie",
        "party",
        "dinner",
        "museum",
        "city",
    }
    while True:
        searchKeyword = input(
            "🧙 Let's search photos with keywords young wizard!\n🧙 Here is avaliable keywords --> sunset|sea|beach|friends|selfie|party|dinner|museum|city ✨\n"
        )

        if searchKeyword.lower() in valid_keywords:
            break
        else:
            print(" ❗💀 Invalid Keyword ❗💀 Please try again.\n")

    keywords = read_photos()
    matchedKeyword = [
        keyword
        for keyword in keywords
        if Regex.search_keywords(keyword) == searchKeyword.lower()
    ]

    print(f"\n✨🔍 We found {len(matchedKeyword)} photos. 🔍✨\n")
    for _ in matchedKeyword:
        print(_)


@log
def check_photos_by_date():

    while True:
        try:
            photoDate = input(
                "🧙 Let's check the photos, enter a valid date young wizard!(YYYY-MM-DD): "
            )
            datetime.strptime(photoDate, "%Y-%m-%d")
            break
        except ValueError:
            print(" ❗💀 Invalid format date Young Wizard!!Please use YYYY-MM-DD. ❗💀")
    photoNames = read_photos()
    matchedPhotos = [
        name
        for name in photoNames
        if Regex.check_photos_by_date(name) == photoDate + "_"
    ]
    temperature = open_meteo(photoDate)

    print(
        f"\n✨📍 We found {len(matchedPhotos)} photos on {photoDate}.The weather in Mallorca was: {temperature}°C ✨\n"
    )
    for _ in matchedPhotos:
        print(_)


@log
def show_active_days():
    photoActive = read_photos()
    dates = [
        Regex.check_photos_by_date(name)
        for name in photoActive
        if Regex.check_photos_by_date(name)
    ]
    date_counts = Counter(dates)
    print("\n✨📅 From the most to the least active days without cursed photos: ✨\n")

    for date, count in sorted(date_counts.items(), reverse=True):
        print(f"Date: {date.replace("_","")}, Photos: {count}")


@log
def view_invalid_photos():

    print("🧙 Let's view the cursed photos! ")
    invalidPhotos = read_photos()
    matchedInvalid = [
        name for name in invalidPhotos if not Regex.check_photos_by_date(name)
    ]

    print(f"\n💀💀 We found {len(matchedInvalid)} 💀 cursed photos. 💀💀\n")
    for _ in matchedInvalid:
        print(_)


@log
def export_grouped_data():
    exportedPhotos = read_photos()

    dict_by_date = {}

    for name in exportedPhotos:
        date = Regex.check_photos_by_date(name)
        keyword = Regex.search_keywords(name)
        if date and keyword:
            dateClean = date.rstrip("_")
            if dateClean not in dict_by_date:
                dict_by_date[dateClean] = []
            dict_by_date[dateClean].append((name, keyword))

    for key, value in dict_by_date.items():
        filename = f"{key}.csv"
        with open(filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Photo Name", "Keyword"])
            for name, keyword in value:
                writer.writerow([name, keyword])

    print(
        f"\n✨ Exported photos into {len(dict_by_date)} CSV files based on dates young wizard.\n"
    )


spells = {
    1: search_keywords,
    2: check_photos_by_date,
    3: show_active_days,
    4: view_invalid_photos,
    5: export_grouped_data,
}


def main():
     while True:
            try:
                time.sleep(2)
                print(open("menu.txt").read())
                spell = int(input("🧙 Your Spell: "))
                print("────────────────────────────────────────────")
                if spell == 6:
                    sys.exit("🚪 Mischief Managed. Until next time...")
                elif spell in spells:
                    spells[spell]()

                else:
                    raise ValueError

            except ValueError:
                print("❗💀 Only a number between 1 and 6, young wizard!❗💀")


if __name__ == "__main__":
    main()
