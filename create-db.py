import duckdb

with duckdb.connect("artemis.db") as con:
    con.execute("""
        CREATE TABLE IF NOT EXISTS artemis AS
        SELECT * FROM read_csv_auto('artemis.csv')
    """)