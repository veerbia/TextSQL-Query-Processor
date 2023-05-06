import asyncio
import time
import concurrent.futures
import heapq
import logging
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class QueryProcessor:
    def __init__(self, timeout=5):
        self.timeout = timeout
        self.vectorizer = TfidfVectorizer()
        self.results_queue = []
        self.lock = asyncio.Lock()

    async def process_sql_query(self, query):
        try:
            # Placeholder for SQL query processing (symmatrical with web query)
            await asyncio.sleep(1)
            result = "SQL result for query: " + query
            return result
        except Exception as e:
            logging.error(f"Error processing SQL query: {e}")
            return "SQL query failed"

    async def process_web_query(self, query):
        try:
            # Placeholder for web query processing (symmatrical with SQL query)
            await asyncio.sleep(2)
            result = "Web result for query: " + query
            return result
        except Exception as e:
            logging.error(f"Error processing web query: {e}")
            return "Web query failed"

    def assess_quality(self, result, query):
        tfidf_matrix = self.vectorizer.fit_transform([result, query])
        result_vector = tfidf_matrix[0]
        query_vector = tfidf_matrix[1]
        similarity = cosine_similarity(result_vector, query_vector)[0][0]
        quality = similarity * 100
        return quality

    async def process_query(self, query):
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            loop = asyncio.get_event_loop()
            sql_query_future = loop.run_in_executor(executor, asyncio.ensure_future, self.process_sql_query(query))
            web_query_future = loop.run_in_executor(executor, asyncio.ensure_future, self.process_web_query(query))

            done, _ = await asyncio.wait(
                [sql_query_future, web_query_future],
                timeout=self.timeout,
                return_when=asyncio.FIRST_COMPLETED
            )

            for future in done:
                result = future.result()
                quality = self.assess_quality(result, query)
                timestamp = time.time()

                priority = (-1*quality, timestamp)
                async with self.lock:
                    heapq.heappush(self.results_queue, (priority, result))

            if self.results_queue:
                _, best_result = heapq.heappop(self.results_queue)
                return best_result
            else:
                return "No results"

# Sample testing usage
# query_processor = QueryProcessor()
# query = "Find the top rated movies"
# result = asyncio.run(query_processor.process_query(query))
# print(result)
