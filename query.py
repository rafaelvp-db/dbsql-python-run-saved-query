"""Small example of running a pre-defined DBSQL query using the DBSQL REST API."""

import logging
import os
import requests
import traceback
from typing import Union, List

from databricks import sql

TOKEN = os.environ["DBSQL_PAT"]
BASE_URL = os.environ["DBSQL_BASE_URL"]
PATH = os.environ["DBSQL_API_PATH"]

CONNECTION_PARAMS = {
    "server_hostname": BASE_URL,
    "http_path": PATH,
    "access_token": TOKEN
}

HEADERS = {
    'Authorization': 'Bearer %s' % TOKEN
}

PARAMS = {
    "page": 1,
    "order": "name",
    "page_size": 1
}

def get_query(query_name: Union[str, None]) -> str:
    """
    Gets DBSQL query content based on either query_id or query_name.

    Args:
        query_id: DBSQL Query ID. Mandatory if query_name is not present.
        query_name: DBSQL Query Name. Mandatory if query_name is not present.

    Returns:
        DBSQL Query definition.
    """

    result = ""

    try:
        if query_name:
            PARAMS["q"] = query_name
        else:
            raise ValueError("Invalid query name")

        url = f"https://{BASE_URL}/api/2.0/preview/sql/queries"
        response = requests.get(
            url,
            headers = HEADERS,
            params = PARAMS
        )
        result = response.json()["results"][0]["query"]
        return result

    except Exception as e:
        logging.error(f"Error getting DBSQL Query: {e}")
        logging.error(f"Query params: {str(PARAMS)}")
        logging.error(f"Response: {response.text}")
        print(f"URL details {BASE_URL + PATH}")


def run_query(query: str, params: List[str] = []) -> List:
    """
    Runs DBSQL Query.

    Args:
        query: DBSQL query.
        params: DBSQL query parameters.

    Returns:
        List of Rows reflecting the query result.
    """

    try:
        if len(query) == 0:
            raise ValueError("Empty query")
        with sql.connect(**CONNECTION_PARAMS) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                return result

    except:
        print(f"Connection params: {CONNECTION_PARAMS}")
        traceback.print_exc()
