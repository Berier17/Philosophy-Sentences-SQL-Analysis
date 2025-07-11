# Philosophy-Sentences-SQL-Analysis
Philosophy Sentences SQL Analysis explores 360k+ philosophical sentences using Python, SQLAlchemy, and SQLite. The project loads the dataset into a relational DB and performs advanced SQL queries to uncover trends in authorship, philosophical schools, sentence lengths, and historical publication.
# Philosophy Sentences SQL Analysis

A data analysis project combining **Python**, **SQLAlchemy**, and **SQLite** to explore a large corpus of philosophical texts. The project stores and queries over 360,000 philosophical sentences with detailed author, school, and publication data.

## 📌 Project Overview
This project loads a CSV dataset of philosophical sentences into a relational database (SQLite) and performs advanced SQL queries to extract meaningful insights such as:
- Top philosophers by sentence count
- Most represented philosophical schools
- Average sentence length per author
- Sentences published before 1800
- Longest sentences per author
- Ranking philosophers by sentence length within their works
- Percentage of sentences by philosophical school

All queries are executed using **SQLAlchemy Core** for flexible SQL execution combined with Python.

## 🗂️ Project Structure
philosophy-sql-analysis/
├── philosophy_data.csv # Raw dataset of philosophical sentences
├── philosophy.db # SQLite database generated by SQLAlchemy
├── main.py # Main Python script for data loading and analysis
├── requirements.txt # Required Python packages
└── README.md # Project documentation (this file)

markdown
Copy
Edit

## 📊 Example Insights
- **Top 5 Philosophers by Sentence Count**
- **Percentage of Sentences by Philosophical School**
- **Average Sentence Length by Author**
- **Oldest Sentences in the Corpus (pre-1800)**

## ⚙️ Requirements

pandas
numpy
sqlalchemy

 Why This Project?
Demonstrates SQL + Python integration

Highlights relational database design for unstructured data (philosophical text)

Showcases intermediate-to-advanced SQL querying (GROUP BY, aggregation, window functions)
