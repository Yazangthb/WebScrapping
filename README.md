# Yazangthb Web Scrapping

This repository contains a web scraping project that extracts movie data from Wikipedia's "List of highest-grossing films" page using Scrapy. It processes the data by cleaning and saving it in multiple formats, and it provides a simple web interface to display the results.

---

## Directory Structure

```plaintext
yazangthb-webscrapping/
├── index.html           # Main web interface page
├── movies.json          # JSON file containing scraped movie data
├── script.js            # JavaScript for dynamic behavior on the web page
├── style.css            # CSS styling for the web page
└── hw/                  # Scrapy project directory
    ├── output.csv       # CSV output of scraped data
    ├── output.json      # JSON output of scraped data
    ├── scrapy.cfg       # Scrapy configuration file
    └── hw/              # Main Scrapy project module
        ├── __init__.py
        ├── items.py         # Defines the MovieItem with fields: Rank, Title, Year, Directed_by, Box_office, movie_url
        ├── middlewares.py   # Custom spider and downloader middlewares
        ├── pipelines.py     # Pipelines for data cleaning and saving (including saving to MySQL)
        ├── settings.py      # Scrapy settings (includes pipelines configuration)
        ├── __pycache__/
        └── spiders/
            ├── __init__.py
            ├── wikitable.py   # Spider that scrapes movie data from Wikipedia
            └── __pycache__/
```

---

## Features

- **Web Scraping with Scrapy:**  
  Scrapes movie details such as rank, title, year, director, and box office from Wikipedia.
  
- **Data Processing Pipelines:**  
  Processes and cleans the scraped data, then saves it to CSV, JSON, and a MySQL database.
  
- **Simple Frontend Interface:**  
  A basic HTML/CSS/JavaScript interface displays the scraped movie data using the generated `movies.json`.

---

## Requirements

- **Python 3.x**
- **Scrapy:** Install via `pip install scrapy`
- **MySQL Connector for Python:** Install via `pip install mysql-connector-python`
- **MySQL Server:** Ensure you have a running MySQL server with a database named `movies` (or update the connection settings in `pipelines.py` accordingly)

---

## Setup and Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/yazangthb-webscrapping.git
   cd yazangthb-webscrapping
   ```

2. **Install Dependencies:**

   If you have a `requirements.txt`, run:
   
   ```bash
   pip install -r requirements.txt
   ```
   
   Otherwise, install manually:
   
   ```bash
   pip install scrapy mysql-connector-python
   ```

3. **Configure MySQL Database:**

   Make sure your MySQL server is running and that there is a database named `movies`. Adjust the connection settings in `hw/hw/pipelines.py` if necessary.

4. **Run the Spider:**

   Navigate to the `hw` directory and start the spider:
   
   ```bash
   cd hw
   scrapy crawl wikitable
   ```
   
   The spider will scrape the movie data from Wikipedia and save the output as defined (CSV, JSON, and into MySQL).

5. **View the Web Interface:**

   Open `index.html` in your web browser. The page loads `movies.json` to display the list of movies.

---

## Project Details

- **Scrapy Settings:**  
  Configured in `hw/hw/settings.py` (e.g., obeying robots.txt, pipeline settings).

- **Spider Implementation:**  
  The spider in `hw/hw/spiders/wikitable.py` fetches data from Wikipedia, processes table rows, and follows links for detailed movie information.

- **Pipelines:**  
  - **MoviePipeline:** Cleans and processes scraped data.
  - **SaveToMysqlPipeline:** Saves the data into a MySQL database.

- **Middlewares:**  
  Custom spider and downloader middleware are defined in `hw/hw/middlewares.py` for extended functionality.

---

## Contributing

Contributions are welcome! Please open issues or submit pull requests for bug fixes or new features.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For questions or inquiries, please contact [your.email@example.com].

