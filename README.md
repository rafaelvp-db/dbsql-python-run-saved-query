# dbsql-run-query
Basic example of how to use [Databricks SQL Python Connector](https://docs.databricks.com/dev-tools/python-sql-connector.html) for running a pre-saved query.

## Instructions

1. Create a ```venv```, activate it and install dependencies by running ```pip install -r requirements.txt```
2. Set the following environment variables: ```DBSQL_PAT```, ```DBSQL_BASE_URL``` and ```DBSQL_API_PATH```
3. From a terminal: ```python dbsql_runner.py saved --query_name="YOUR_QUERY_NAME"```

<img src="https://github.com/rafaelvp-db/dbsql-python-run-saved-query/blob/main/img/carbon.png?raw=true" />

## Reference

* [Databricks SQL](https://databricks.com/product/databricks-sql)
* [Databricks SQL Queries and Dashboards REST API](https://docs.databricks.com/sql/api/queries-dashboards.html)
* [PyPi - Databricks SQL Connector](https://pypi.org/project/databricks-sql-connector/)

