# Comment Scraper

This project is a web scraping application built with Scrapy and Selenium to collect product comments from an e-commerce website. It also includes a simple frontend to display the extracted comments.

## Features

- **Scrapes product reviews:** Uses Selenium to navigate and extract product reviews dynamically from e-commerce pages.
- **Handles infinite scrolling:** Scrolls through dynamically loaded content to ensure all product listings and reviews are captured.
- **Extracts comments:** Retrieves reviewer names, dates, and actual review texts for detailed analysis.
- **Filters seller-specific comments:** Selects reviews based on the seller, ensuring only relevant feedback is collected.
- **Stores data in JSON format:** Outputs structured data that can be used for further processing or visualization.
- **Simple frontend for visualization:** Displays the collected reviews in a user-friendly interface.

## Technologies

- **Scrapy:** A fast and powerful web scraping framework used to extract structured data from websites.
- **Selenium:** A browser automation tool that enables dynamic interaction with web pages, handling JavaScript-rendered content.
- **WebDriver Manager:** Simplifies the management and installation of WebDriver binaries for Selenium.
- **Python:** The core programming language used for backend logic, scraping, and data processing.
- **HTML & CSS:** Used to create the frontend structure and styling for displaying comments.
- **JavaScript:** Adds interactivity to the frontend, enabling dynamic content updates without requiring page reloads.


## Installation

- **Backend Setup**

To clone the project, run the following commands:

Clone the repository:

```
git clone https://github.com/mehmetbacik/comment-scraping.git
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the Scrapy spider:

```
scrapy crawl comment_spider
```

- **Frontend Setup**

Open index.html in a browser.

Ensure scripts.js fetches and displays the extracted comments correctly.


## Usage

The Scrapy spider navigates the product listing page, extracts links, and fetches reviews.

The extracted data is stored in JSON format.

The frontend displays the reviews dynamically.


## GitHub Page

GitHub Repository: [https://github.com/mehmetbacik/comment-scraping.git](https://github.com/mehmetbacik/comment-scraping.git).

## License

This project is open-source and available under the MIT License.

## Contributions

If you wish to contribute to the project, please open a pull request. Any contributions and feedback are welcome!

---
