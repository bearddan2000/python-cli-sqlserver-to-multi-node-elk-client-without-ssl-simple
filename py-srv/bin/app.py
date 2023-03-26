
from elasticsearch import Elasticsearch
from elasticsearch.client import IndicesClient
import os

from settings import configurations

INDEX_NAME=os.environ["INDEX_NAME"]

def main():
    for node in ['es1','es2','es3']:
        es = Elasticsearch(
                node + ":9200",
                http_auth=["elastic", "changeme"],
            )

        client = IndicesClient(es)
        try:
            client.create(index=INDEX_NAME, body=configurations)
        except:
            pass


main()