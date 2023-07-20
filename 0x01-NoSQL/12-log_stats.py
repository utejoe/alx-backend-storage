#!/usr/bin/env python3
"""
Script that provides some stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


def log_stats():
    client = MongoClient()
    collection = client.logs.nginx

    # Get the total number of logs
    total_logs = collection.count_documents({})

    # Get the number of logs for each method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_logs = {}
    for method in methods:
        count = collection.count_documents({"method": method})
        method_logs[method] = count

    # Get the number of logs with method=GET and path=/status
    status_check = collection.count_documents({"method": "GET", "path": "/status"})

    # Display the statistics
    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_logs.items():
        print(f"\tmethod {method}: {count}")
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
