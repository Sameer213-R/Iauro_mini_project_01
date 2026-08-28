# Generic Web Scraper

A simple and reusable **Python-based web scraper** that extracts useful information from publicly accessible webpages and stores the data in a structured **JSON file**.

## Problem Statement

Collecting information from webpages manually can be time-consuming and difficult to manage. The goal of this project is to automate the process of fetching webpage content, extracting useful information, and storing it in a structured format.

## Solution

The application accepts a webpage URL, fetches its HTML content, parses the HTML using BeautifulSoup, extracts useful information, and stores the result in a JSON file.

**Workflow:**

```text
URL → Fetch HTML → Parse HTML → Extract Data → Store as JSON
```

## Features

* Accepts webpage URL as input.
* Supports configurable browser User-Agent.
* Extracts:

  * Page title
  * Headings
  * Paragraphs
  * Links
  * Images
* Stores extracted data in JSON format.
* Handles basic HTTP and connection errors.
* Uses a modular project structure for easy maintenance and future development.

## Technology Stack

* **Python:** 3.12.9
* **Requests:** For fetching webpage content
* **BeautifulSoup:** For parsing HTML
* **JSON:** For storing structured data
* **lxml:** For HTML parsing support

## Project Structure

```text
Web_Scraper/
│
├── main.py
├── requirements.txt
│
├── scraper/
│   ├── __init__.py
│   ├── fetcher.py
│   ├── parser.py
│   ├── extractor.py
│   └── exporter.py
│
└── output/
    └── data.json
```

### Module Description

| File               | Purpose                             |
| ------------------ | ----------------------------------- |
| `main.py`          | Main entry point of the application |
| `fetcher.py`       | Fetches webpage HTML content        |
| `parser.py`        | Parses HTML using BeautifulSoup     |
| `extractor.py`     | Extracts useful webpage information |
| `exporter.py`      | Saves data into JSON                |
| `requirements.txt` | Contains project dependencies       |
| `output/data.json` | Stores the scraped data             |

## Installation

Make sure Python **3.12.9** is installed.

Clone or download the project and open the project directory:

```bash
cd Web_Scraper
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python main.py
```

Provide the webpage URL when requested.

For example:

```text
https://en.wikipedia.org/wiki/Python_(programming_language)
```

The application will fetch the webpage, extract the required information, and save the result in:

```text
output/data.json
```

## Example Output

```json
{
    "url": "https://example.com",
    "title": "Example Website",
    "headings": [],
    "paragraphs": [],
    "links": [],
    "images": []
}
```

## Error Handling

The application handles common issues such as:

* Invalid URLs
* Connection failures
* Request timeouts
* HTTP errors
* Empty or unavailable webpage content

## Limitations

The current version mainly works with webpages where the required content is available in the HTML response.

Websites that load their content dynamically using JavaScript may require additional tools such as **Selenium or Playwright**.

The scraper should only be used for publicly accessible content and in accordance with the target website's terms and access policies.

## Future Improvements

Possible improvements include:

* JavaScript-based webpage support
* HTML table extraction
* Multiple URL processing
* Database storage
* Logging
* Scheduled scraping
* Additional browser/User-Agent configurations
* Data validation and duplicate detection

## Conclusion

This project provides a simple and reusable foundation for extracting structured information from webpages. Its modular design makes it easy to maintain and extend with additional scraping and data-processing capabilities.
