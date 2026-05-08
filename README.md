# ontop-hackathon-hemafair
Materials for Ontop tutorial

## Deployment (Linux)
```git clone https://github.com/dwijnbergen/ontop-hackathon-hemafair.git```

Clones this repository.

```sh create_python_env.sh```

Creates a Python virtual environment with RDFLib and DuckDB libraries.

```source activate_python_env.sh```

Actives the python virtual environment.

```python3 create-db.py```

Creates a DuckDB database from the csv files.

```download_duckdb_jdbc.sh``` (from the jdbc folder)

Downloads the DuckDB jdbc.

```sudo docker compose up -d```

Starts the container and detaches.
