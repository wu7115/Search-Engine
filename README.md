# Search Engine Project

This repository contains a modular and comprehensive implementation of a search engine, showcasing various aspects of information retrieval, data processing, and database-driven search functionalities. The project is divided into five interconnected components, each addressing a critical step in building a modern search engine.

## Project Overview

The search engine project is structured to progressively integrate foundational concepts, advanced algorithms, and practical implementations. Below is a high-level overview of the components:

1. **Information Retrieval**
   - Implements the basics of text processing and retrieval, including tokenization, lemmatization, stemming, stopword removal, inverted indexing, and vector space retrieval.
   - These techniques form the backbone of indexing and searching textual data.

2. **Web Spidering**
   - Develops a web crawler that collects web pages, extracts content and links, and stores the data in a structured SQLite database.
   - This step creates the dataset required for further analysis and ranking.

3. **PageRank Algorithm**
   - Calculates the importance of web pages based on their link structure using the PageRank algorithm.
   - Integrates with the crawled data to assign importance scores to pages, which enhances search result relevance.

4. **Search Engine Application**
   - Builds a web interface with functionalities for:
     - Text-based web search using TF-IDF and PageRank.
     - Image search based on metadata.
     - Reverse image search using deep learning-based feature extraction.
   - Combines the crawled data, tokenized text, and precomputed image features for an interactive user experience.

5. **Web Search Engine Using Database**
   - Implements an advanced web search engine backed by an SQLite database.
   - Integrates web crawling, PageRank computation, and a query-based search interface.
   - Provides a seamless pipeline from data collection to ranked search results.

---

## Components and Workflow

### 1. **Information Retrieval**
- **Objective**: Lay the groundwork for text-based search.
- **Techniques**:
  - Tokenization and lemmatization to preprocess text.
  - Stopword removal to eliminate irrelevant words.
  - Inverted indexing for efficient term lookup.
  - TF-IDF and cosine similarity for ranking search results.

### 2. **Web Spidering**
- **Objective**: Collect web data and links for building a web graph.
- **Features**:
  - Crawls web pages starting from seed URLs.
  - Extracts and stores HTML content, cleaned text, titles, and outgoing links.
  - Stores data in an SQLite database for easy retrieval.

### 3. **PageRank Algorithm**
- **Objective**: Rank web pages based on link popularity.
- **Features**:
  - Constructs a directed graph from crawled data.
  - Uses NetworkX to compute PageRank scores.
  - Updates the SQLite database with PageRank values for later use.

### 4. **Search Engine Application**
- **Objective**: Develop a user-facing interface for searching web and image data.
- **Features**:
  - **Web Search**: Combines TF-IDF and PageRank to rank and display textual content.
  - **Image Search**: Matches metadata to user queries.
  - **Reverse Image Search**: Extracts image features using a deep learning model (VGG16) and finds visually similar images.
  - **Backend**: Flask-based web application.

### 5. **Web Search Engine Using Database**
- **Objective**: Integrate all components into a cohesive database-driven search engine.
- **Features**:
  - Advanced web crawling with structured data storage.
  - Query processing with ranked results based on PageRank and textual relevance.
  - Efficient database operations to handle large datasets.

---

## How It All Comes Together

The individual components form a pipeline that mimics the operation of real-world search engines:

1. **Data Collection**:
   - The web spider gathers raw data (HTML content, links) and stores it in the SQLite database.

2. **Data Processing**:
   - Text data is tokenized, cleaned, and indexed for fast retrieval.
   - Images are processed to extract features for reverse image search.

3. **Relevance Ranking**:
   - PageRank computes link-based importance scores.
   - TF-IDF ensures query relevance in textual searches.
   - Combined scores provide ranked search results.

4. **User Interaction**:
   - The Flask-based application provides intuitive interfaces for textual, metadata-based, and reverse image searches.

---

## Usage Instructions

### Dependencies
- Install the required Python libraries by running:
  ```bash
  pip install -r requirements.txt
  ```
- Download additional NLTK resources:
  ```python
  import nltk
  nltk.download('punkt')
  nltk.download('wordnet')
  nltk.download('stopwords')
  ```

### Steps to Run the Project

1. **Set Up Database**:
   - Run `web_spider.py` to populate the SQLite database with crawled web pages.
   - Run `pagerank.py` to calculate and store PageRank scores.

2. **Precompute Features**:
   - Run `offline.py` to extract and store image features.
   - Run `craw_store_as_tokens_pickle.py` to tokenize and store webpage text data.

3. **Start the Web Application**:
   - Execute the Flask app:
     ```bash
     python searchengine.py
     ```
   - Navigate to `http://127.0.0.1:5000/` to access the search engine.

---

## Applications
- Academic demonstration of search engine design.
- Information retrieval systems for web and multimedia data.
- Reverse image search and image similarity detection.

This repository provides a modular, scalable, and extensible framework for understanding and implementing search engine technologies.
