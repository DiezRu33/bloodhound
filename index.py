from neo4j import GraphDatabase

# Conectarse a la base de datos de Neo4j
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "tu_contraseña"))

# Ejecutar una consulta Cypher
with driver.session() as session:
    result = session.run("MATCH (n) RETURN n LIMIT 10")
    for record in result:
        print(record)

# Cerrar la conexión
driver.close()
