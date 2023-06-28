from datetime import datetime
import random
import logging
from elasticsearch import Elasticsearch

# Create an Elasticsearch client
es = Elasticsearch(['http://localhost:9200'])

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def generate_logs(index_name, num_logs):
    # Generate and index logs
    for i in range(num_logs):
        log = {
            'timestamp': datetime.now(),
            'level': random.choice(['INFO', 'WARNING', 'ERROR']),
            'message': generate_random_message()
        }
        res = es.index(index=index_name, body=log)
        logger.info(f'Indexed log: {res["_id"]}')

def generate_random_message():
    # Generate a random log message
    messages = [
        'User logged in successfully',
        'Failed to process request',
        'Database connection error',
        'Page not found: /path/to/page',
        'Internal server error',
        'Request timed out'
    ]
    return random.choice(messages)

if __name__ == '__main__':
    index_name = 'logs'
    num_logs = 10

    # Create the index if it doesn't exist
    if not es.indices.exists(index=index_name):
        es.indices.create(index=index_name)

    # Generate and index logs
    generate_logs(index_name, num_logs)

