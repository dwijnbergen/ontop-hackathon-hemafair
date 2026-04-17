import duckdb

with duckdb.connect("example.db") as con:
    con.execute("""
        CREATE TABLE IF NOT EXISTS example AS
        SELECT * FROM read_csv_auto('example.csv')
    """)