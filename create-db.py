import duckdb

with duckdb.connect("artemis.db") as con:
    con.execute("""
        CREATE TABLE IF NOT EXISTS astronauts AS
        SELECT * FROM read_csv_auto('artemis_astronauts.csv')
    """)

    con.execute("""
        CREATE TABLE IF NOT EXISTS missions AS
        SELECT * FROM read_csv_auto('artemis_missions.csv')
    """)

    con.execute("""
        CREATE TABLE IF NOT EXISTS roles AS
        SELECT * FROM read_csv_auto('artemis_roles.csv')
    """)