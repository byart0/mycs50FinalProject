# Photo Organizer Wizard
#### Video Demo:  <https://youtu.be/G6pPXEIA1gI>
#### Description:

Photo Organizer Wizard is a Python **command-line tool** that organizes photo files based on the dates and keywords in their filenames. The project allows users to search photo names in the **photos.txt** file, list photos taken on specific dates, view active days, detect invalid or incorrectly formatted photos, and export the results to CSV files. **Don't forget young wizard, this organizer was made with 💫 magic and Python.**

---

## Project Purpose

This application is developed especially for users who want to easily group and manage a large number of photos by date and keywords. Photo filenames must include a date (in the **YYYY-MM-DD format**) and descriptive keywords (e.g., sunset, beach, selfie, etc.). Users can search by specific keywords or list photos by date. Also, users can detect invalid formatted photos easily. Additionally, by using an **API**, the app also displays the temperature of the photo location on the day it was taken. The primary purpose of this program is to refresh memories and make them easier to recall.

---

## File Descriptions

- **project.py**: The main execution file of the project. It takes commands from the user via a menu and calls the relevant functions.
- **photos.txt**: A text file containing photo filenames line by line. It is the data source of the program.
- **requirements.txt**: This file contains the names of the libraries used and installed in the project.
- **CSV Files**: `export_grouped_data`function exports photos and keywords grouped by date to CSV files.
- **menu.txt**: Contains the command menu text shown to the user.
- **text_project.py**: The main logic and user interaction management file of the project. It handles reading photo files and extracting dates and keywords from filenames.

---

## Technologies and Libraries Used

- Python 3
- `re` module (to extract date and keyword information from photo names using regular expressions)
- `requests` module (to fetch weather data from the Open-Meteo API)
- `csv` module (to export data in CSV format)
- `collections.Counter` (to count the photos according to dates)
- `sys` (for system operations like exiting the program)
- `datetime` (for date and time operations)
- `unittest.mock (mock_open, patch)` (to mock file reading during tests)
- `time` (to make menu.txt delay to appear for 2 sec )
---

## Design Decisions and Challenges

To keep the project simple yet modular, functions were divided for clear responsibilities, and a menu system was designed to present each operation like a **spell** to the user. To avoid disrupting the program's flow, the menu system is stored in a separate file named **menu.txt**, which is read and displayed continuously until the user exits. To reduce clutter in the terminal, the menu is displayed with a **2-second delay.**

Regex usage was critical to correctly extract dates and keywords from photo filenames. The regular expressions were designed based on the photo filenames listed in **photos.txt**.**For a photo file to be considered invalid, it simply needs to not start with a date followed by an underscore. All photo files, including invalid ones, end with .png, .jpg, or .jpeg. No other file types are present in the photos.txt file.**

Fetching data from the **Open-Meteo API** was added to enrich user experience; however, error handling was implemented to manage possible internet connection issues.**The Open-Meteo API can be used starting from April 29, 2025**. If the user queries a photo with an earlier date, the program will raise an error. **However, this program was specifically designed to organize photos from a 3-day vacation in Mallorca on the dates 2025-05-24, 2025-05-25, and 2025-05-26**. The coordinates for Mallorca were used in the implementation. It provides the temperature during the first hour of each day. Open-Meteo was chosen because it is a free service.

Exporting to CSV is useful for data analysis and reporting, and automatic file creation for different dates simplifies this process.

Enhancing with log decorators that display information after each user command. Once a command is selected, the program shows the date, time, and the name of the chosen spell. When the spell is completed, it also displays a message indicating the completion time and date.

## Usage

When the program runs, it displays a command menu and performs operations according to the selected “spell”:

1. Search photos by keywords
2. List photos by date and show weather information
3. List shooting days from most to least frequent based on dates
4. List photos with invalid formats
5. Export photos to date-based CSV files
6. EXIT

The program starts when the user enters a number between 1 and 6 in the terminal. If the user **enters 6**, the program exits. If a number outside the range of 1–6 is entered, the program raises an error. Each command is sensitive to incorrect input—if the input is invalid, the program displays an error message and prompts the user to try again.

**Photo filenames in the photos.txt file follow the format: 2025-07-30_sunset.jpg.** All filenames must start with a date followed by an underscore; otherwise, the photo is considered invalid.

**In Command 1**, the available keywords are displayed to the user. Whether the user types in uppercase or lowercase, the program searches for matching keywords and displays how many matching photos were found, along with their names.

**In Command 2**, if the user enters a valid date in the correct format and within the acceptable date range, the program shows how many photos were taken on that day and lists them. It also provides weather information for that date.

**Command 3** lists all active shooting days sorted by date frequency from most to least, along with the number of photos taken on each day.

**Command 4** displays how many and which photos are considered "cursed" (invalid format).

**Command 5** automatically organizes the photo names—regardless of their order in photos.txt—by date and exports them into separate .csv files for each day. In each .csv file, the user can view photo names and their keywords in a table-like format.

---

## Conclusion

**Photo Organizer Wizard** is a practical, **potterhead friendly ⚡** and enjoyable tool for those who want to organize their photo collections. The project integrates important programming concepts such as file handling, regex, API usage, user interaction, and data export.

**This program is designed for a specific date and location**. In the future, greater flexibility regarding date and location can be implemented. Currently, the temperature data reflects only the early hours of the day; additional metrics such as the daily average temperature may be added later. It is also possible to switch to a different weather API in future updates.

---

*Prepared by:* [Başak Yaralı]
*Github:* [byart0]
*edX:* [basakyarali_66]
*Date Saved:* 2025-07-31
*Location:* [İstanbul, Türkiye]
*e-mail:* [basakyarali@gmail.com]

---
**Made with 💫 magic and Python**
---
