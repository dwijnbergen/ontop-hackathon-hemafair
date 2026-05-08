import os
import duckdb

database_file ="input/artemis.db"

with duckdb.connect(database_file) as con:
    con.execute("""
        DROP TABLE IF EXISTS astronauts
    """)

    con.execute("""
        DROP TABLE IF EXISTS missions
    """)

    con.execute("""
        DROP TABLE IF EXISTS roles
    """)

    con.execute("""
        CREATE TABLE IF NOT EXISTS astronauts AS
        SELECT * FROM read_csv_auto('csv_data/artemis_astronauts.csv')
    """)

    con.execute("""
        CREATE TABLE IF NOT EXISTS missions AS
        SELECT * FROM read_csv_auto('csv_data/artemis_missions.csv')
    """)

    con.execute("""
        CREATE TABLE IF NOT EXISTS roles AS
        SELECT * FROM read_csv_auto('csv_data/artemis_roles.csv')
    """)

    con.execute("""
        SHOW ALL TABLES
    """)

    print("Current tables:")
    for table in con.fetchall():
        print("\033[1m" + table[2] + "\033[0m")
        print("\t".join(table[3]))
        print("\t".join(table[4]))
        print("")

os.chmod(database_file, 0o777)