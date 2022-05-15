from typing import Union, List

import fire
from query import get_query, run_query

class DBSQLQueryExecutor(object):
    """A simple DBSQLExecutor class."""

    def adhoc(self, query: str, params: List[str] = []):
        """
        Runs Adhoc DBSQL Query.

        Args:
            query: DBSQL query.
            params: DBSQL query parameters.

        Returns:
            List of Rows reflecting the query result.
        """

        result = run_query(query, params)
        if result is not None:
            print(f"Sample result: {result[0]}")
        else:
            print("No results")

    def saved(
        self,
        query_name: str,
        params: List[str] = []
    ):
        """
        Runs Saved DBSQL Query.

        Args:
            query_name: DBSQL query name.
            params: DBSQL query parameters. Optional

        Returns:
            List of Rows reflecting the query result.
        """

        result = None
        print(f"Getting query {query_name}...\n\n")
        query = get_query(query_name)
        print(query)

        if len(query) > 0:
            result = run_query(query, params)

        if result is not None:
            print(f"\n\n{result}")
        else:
            print("No results")
    

if __name__ == '__main__':
    fire.Fire(DBSQLQueryExecutor)