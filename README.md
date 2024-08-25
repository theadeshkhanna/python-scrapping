# Python FastAPI Web Scraping Tool

This project is a Python-based web scraping tool built using the FastAPI framework. The tool scrapes product information from a specified website and stores the data locally in a JSON file. It includes features like optional proxy support, page limiting, and token-based authentication.

## Features

- Scrapes product names, prices, and images from a catalog.
- Optional proxy support and page limiting.
- Stores scraped data in a local JSON file.
- Caching mechanism to avoid redundant updates.
- Simple token-based authentication for API access.

## Prerequisites

- **Python 3.8+**
- **pip** (Python package installer)
- **virtualenv** (optional, but recommended)

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```

### 2. Set Up a Virtual Environment (Optional but Recommended)

Setting up a virtual environment helps manage dependencies and avoids conflicts with other projects.

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

After activating the virtual environment, install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

### 4. Run the Application

Start the FastAPI server using Uvicorn:

```bash
uvicorn main:app --reload
```

### 5. Access the Scraping API

To use the scraping functionality, you can make a POST request to the /scrape endpoint.

```bash
curl -X POST "http://127.0.0.1:8000/scrape" \
-H "Authorization: Bearer secret_token" \
-H "Content-Type: application/json" \
-d '{
    "pages": 5,
    "proxy": "http://myproxy:8080"
}'
```
