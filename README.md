# dbsql-run-query
Basic example of how to use Databricks SQL Python Connector for running a pre-saved query.

## Instructions

1. Create a ```venv```, activate it and install dependencies by running ```pip install -r requirements.txt```
2. Set the following environment variables: ```DBSQL_PAT```, ```DBSQL_BASE_URL``` and ```DBSQL_API_PATH```
3. From a terminal: ```python dbsql_runner.py saved --query_name="YOUR_QUERY_NAME"```

<img src="https://github.com/rafaelvp-db/dbsql-python-run-saved-query/blob/main/img/carbon.png?raw=true" />

