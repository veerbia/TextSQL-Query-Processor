# TextSQL-Query-Processor

TextSQL Query Processor is an asynchronous Python class designed to process both SQL and Web queries. Built for the LLM-powered emerging text-to-SQL use case in [TextSQL](https://github.com/caesarHQ/textSQL). It utilizes the power of Python's asyncio library for concurrent execution of SQL and Web queries, and employs TF-IDF Vectorization and Cosine Similarity for result quality assessment.

## Features
- **Concurrent Query Processing**: The QueryProcessor class concurrently executes SQL and Web queries for a given input text using Python's asyncio library. This allows for efficient utilization of resources and faster query results.

- **Quality Assessment**: The QueryProcessor class assesses the quality of the query results using TF-IDF Vectorization and Cosine Similarity. The quality of a result is determined by its similarity to the original query.

- **Result Prioritization**: Results are prioritized based on their quality and timestamp. The result with the highest quality (i.e., highest similarity to the original query) is returned first. If two results have the same quality, the one that was produced first is returned.

- **Timeout Management**: The class allows for timeout management to avoid excessively long-running queries. The timeout can be specified during the class instantiation.

## Usage
```python
query_processor = QueryProcessor()
query = "Find the player with the highest PER in the 2019 season"
result = asyncio.run(query_processor.process_query(query))
print(result)
```
## Customization
This template includes placeholders for SQL and web query processing methods (`process_sql_query` and `process_web_query`). Replace these placeholders with your actual SQL and web query processing code to suit your specific requirements.

## Dependencies
The QueryProcessor class depends on the following Python libraries:

- Python 3.7 and above
- asyncio
- concurrent.futures
- heapq
- logging
- sklearn.feature_extraction.text.TfidfVectorizer
- sklearn.metrics.pairwise.cosine_similarity

## Installation
Ensure that you have the necessary dependencies installed. You can install these dependencies using pip:

```pip3 install sklearn asyncio```

Once the dependencies are installed, you can use the QueryProcessor class in your Python code

## License
This project is licensed under the terms of the MIT license.