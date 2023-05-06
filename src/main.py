import asyncio
from query_processor_template import QueryProcessor

def main():
    query_processor = QueryProcessor(timeout=5)
    query = "ADD YOUR QUERY HERE (BEFORE OR AFTER NARROWING/REFINEMENT)"
    result = asyncio.run(query_processor.process_query(query))
    print(result)

if __name__ == "__main__":
    main()

