# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 15:17:02 2025

@author: aliel
"""
#Importing libraries
import pandas as pd 
import numpy as np
from sqlalchemy import create_engine, Table, Date, Column, ForeignKey, Float, String, Integer, text, Text, MetaData
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

#Importing the data
df = pd.read_csv(r'D:\philosophy_data.csv')
df.info()

#DB connection
engine = create_engine('sqlite:///philosophy.db')

metadata = MetaData()

sentences = Table('sentences', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String),
    Column('author', String),
    Column('school', String),
    Column('original_publication_date', Integer),
    Column('corpus_edition_date', Integer),
    Column('sentence_length', Text),
    Column('sentence_str', Text)
    )

metadata.create_all(engine)


df[['title','author','school','original_publication_date','corpus_edition_date',
    'sentence_length','sentence_str']].to_sql('sentences',engine, index=False, if_exists='replace')


def run_query(sql):
    with engine.connect() as conn:
        result = conn.execute(text(sql))
        return result.fetchall()
    
#Top 5 philosiphers with most senteneces in corpus
    query = """
    SELECT author, COUNT(*) as sentence_count
    FROM sentences
    GROUP BY author
    ORDER BY sentence_count DESC
    LIMIT 5;
    """
    rows = run_query(query)
    for row in rows:
        print(row)
        
#Most used philosophical schools
    query2 = """
    SELECT school, COUNT(*) as count
    FROM sentences
    GROUP BY school
    ORDER BY count DESC
    
    """
    rows2= run_query(query2)
    print(rows2)
    
#Average sentence length per author
    query3= """
    SELECT author, AVG(sentence_length) as avg_length
    FROM sentences
    GROUP BY author
    ORDER BY avg_length DESC;
    
    """
    row3 = run_query(query3)
    print(row3)

#Sentences published before 1800
    query4 ="""
    SELECT title, author, sentence_length
    FROM sentences
    WHERE original_publication_date < 1800
    LIMIT 10;
    
    """
    row4 = run_query(query4)
    print(row4)

#Longest sentence per author    
    query5 = """
    SELECT s.author, s.sentence_str, s.sentence_length
    FROM sentences s
    WHERE s.sentence_length = (
        SELECT MAX(s2.sentence_length)
        FROM sentences s2
        WHERE s2.author = s.author
        )
    ORDER BY s.sentence_length DESC;
    
    """
    row5 = run_query(query5)
    print(row5)
    
#Ranking philosophers by sentence length
    query6 = """
    SELECT author, sentence_str, sentence_length,
    RANK() OVER (PARTITION BY author ORDER BY sentence_length DESC) as rank_within_author
    FROM sentences
    WHERE school= 'rationalism'
    ORDER BY author, rank_within_author
    LIMIT 10;
    """
    row6 = run_query(query6)
    print(row6)

#Percentage of sentences by school
    query7 = """
    SELECT school, 
       COUNT(*) AS sentence_count,
       ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM sentences), 2) AS percentage_of_total
FROM sentences
GROUP BY school
ORDER BY percentage_of_total DESC;

    """
    row7 = run_query(query7)
    print(row7)




