import os


class Environments:
    @property
    def teams_incoming_webhook(self) -> str:
        tiw: str = os.environ.get("TEAMS_INCOMING_WEBHOOK")
        assert tiw
        return tiw

    @property
    def mssql_connection_string(self) -> str:
        conn_string: str = os.environ.get("MSSQL_CONNECTION_STRING")
        assert conn_string
        return conn_string
