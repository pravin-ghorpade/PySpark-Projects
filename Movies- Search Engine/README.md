Extracted and uploaded the file plot summaries.txt from http://www.cs.cmu.edu/~ark/personas/ data/MovieSummaries.tar.gz to Databricks. 
Removed stopwords.
Created a tf-idf for every term and every document (represented by Wikipedia movie ID) using the MapReduce method.
Output the top 10 documents with the highest tf-idf values for that term.
Read the search terms from the search file and output the top 10 documents with the highest tf-idf values for that term:
Evaluated cosine similarity between the query If the user enters a query consisting of multiple terms eg: "Funny movie with action scenes"
