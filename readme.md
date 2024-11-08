# Cong Bo Ban An Crawler and Analysis Project

This project is designed to crawl and extract data from the [Công Bố Bản Án website](https://congbobanan.toaan.gov.vn), which is the official website for publishing Vietnamese court decisions. The project also provides data analysis tools using Python and Jupyter Notebook to process and analyze the scraped court decision information.

## Project Structure

The project consists of two main components:

1. **Data Crawling (Scrapy Spiders)**

   - The crawling portion of the project is implemented using [Scrapy](https://scrapy.org/), a Python framework for fast and powerful web scraping.
   - **Spiders** are used to crawl and collect data from the Công Bố Bản Án website, specifically collecting metadata and downloading court decisions in PDF format.

   The crawling code is divided into two parts:

   - `banan.py`: This spider scrapes court decision details, such as type, date, case number, case relationship type, etc., and saves the results to `output.csv`.
   - `pdf.py`: This spider reads a list of case URLs from `banan.txt` and downloads the corresponding PDF documents.

2. **Data Analysis (Jupyter Notebook)**
   - The data analysis part uses `analysis.ipynb`, which contains code for loading and analyzing the scraped data using [Pandas](https://pandas.pydata.org/).
   - This notebook processes and cleans the data, performs various transformations, and provides example visualizations to understand the collected court data better.

## Installation and Setup

To run this project, you'll need Python 3 and some additional packages. You can set up your environment as follows:

1. Clone the repository:

   ```sh
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Create a virtual environment and install dependencies:

   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Set up input files for crawling:
   - Create a file named `banan.txt` that contains the URLs of the cases you want to scrape.

## Crawling Court Data

### Running the `banan` Spider

The `banan` spider scrapes metadata about court decisions and saves it to a CSV file (`output.csv`).

To run the spider, use:

```sh
scrapy crawl banan
```

This spider will start with a list of generated URLs and scrape the court decisions' metadata, which it saves into the CSV file `output.csv`.

### Running the `pdf` Spider

The `pdf` spider reads URLs from `banan.txt` and downloads the associated PDF files of court decisions.

To run the spider, use:

```sh
scrapy crawl pdf
```

Ensure you have `banan.txt` prepared with the URLs for downloading PDFs.

## Data Analysis

After scraping, you can analyze the collected data using the Jupyter Notebook (`analysis.ipynb`). This notebook:

- Loads the `output.csv` file.
- Cleans and preprocesses the data, extracting information such as court case ID, date, type, and details.
- Performs exploratory analysis to gain insights into the types of cases, relationships, courts involved, etc.

To start the notebook, run:

```sh
jupyter notebook analysis.ipynb
```

## Key Features

- **Efficient Crawling:** Utilizes Scrapy's concurrency capabilities to scrape large volumes of data quickly from the Công Bố Bản Án website.
- **Automated PDF Downloads:** Automatically downloads PDF versions of court decisions.
- **Detailed Data Analysis:** Provides initial exploratory analysis on the scraped data, with information such as case types, parties involved, and courts.

## Custom Settings in Scrapy Spiders

- **Concurrency Settings:** The spiders are set up to handle a large number of concurrent requests (`CONCURRENT_REQUESTS = 128`), which helps in efficiently scraping a high volume of data.
- **Timeout and Retry Settings:** Timeouts are set to avoid long waits for non-responsive pages, and retries are disabled to speed up the crawling process.
- **Error Handling:** If a URL request fails, the URL is logged to `failed_urls.txt` for later review and retry.

## Notes and Considerations

- **Website Structure Changes**: If the structure of the `congbobanan.toaan.gov.vn` website changes, the scraping selectors (`css`) may need updates.
- **Legal Use**: Ensure compliance with local laws and website terms of use when scraping court data.
- **Dataset Size**: Depending on the number of cases, the output data may be large. Consider optimizing storage with compression (e.g., saving CSV as `gzip`).

## License

This project is licensed under the MIT License. See `LICENSE` for more information.

## Contributing

Feel free to submit issues, suggestions, or contributions via pull requests. Contributions are always welcome!

## Contact

If you have any questions, feel free to reach out to me via GitHub issues.

---

Happy crawling and analyzing!
