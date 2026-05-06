import rdflib
g = rdflib.Graph()

# Prepare first query
query1 = """
PREFIX sio: <http://semanticscience.org/resource/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ncit: <http://purl.obolibrary.org/obo/NCIT_>
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>

SELECT ?firstName ?lastName ?placeOfBirth ?population WHERE {
    SERVICE <http://localhost:8080/sparql> {
        ?astronaut a foaf:Person .
        ?astronaut foaf:firstName ?firstName .
        ?astronaut foaf:lastName ?lastName .
        ?astronaut ncit:C176764 ?placeOfBirth .

    }

    SERVICE <https://query.wikidata.org/sparql> {
        ?placeOfBirth wdt:P1082 ?population .
    }
}
"""

query2 = """
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>

SELECT ?city ?population WHERE {
    SERVICE <https://query.wikidata.org/sparql> {
        ?city wdt:P31/wdt:P279* wd:Q515 .
        ?city wdt:P1082 ?population .
        ?city wdt:P17 wd:Q55 .
    }
}
"""

query3 = """
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>

SELECT ?population WHERE {
    SERVICE <https://query.wikidata.org/sparql> {
        <http://www.wikidata.org/entity/Q5092> wdt:P1082 ?population .
    }
}
"""

# Run first query
qres = g.query(query1)
places_of_birth = []
for row in qres:
    print(row)
    places_of_birth.append(str(row.placeOfBirth))

# Prepare second query
places_of_birth_str = " ".join(["<" + item + ">" for item in places_of_birth])

query4 = """
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?label ?pop WHERE {
    VALUES ?x { """ + places_of_birth_str + """ }

    SERVICE <https://query.wikidata.org/sparql> {
        ?placeOfBirth wdt:P1082 ?pop .
        ?placeOfBirth rdfs:label ?label .
    }
}
"""
# Run second query

qres = g.query(query4)
for row in qres:
    print(row)