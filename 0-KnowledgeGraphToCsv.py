from neo4j import GraphDatabase
import pandas as pd
import os
# Replace with your Neo4j credentials and connection details
uri = "neo4j://localhost:7687"  # Change to your Neo4j URI
username = "neo4j"
password = "12345678"
database = "neo4j"  # Name of your database

# Connect to Neo4j
driver = GraphDatabase.driver(uri, auth=(username, password))

# Create the csv directory if it doesn't exist
if not os.path.exists("csv"):
    os.makedirs("csv")

# Queries to extract each dataset with specific attributes
queries = {
    "users": """
        MATCH (u:User) 
        RETURN elementId(u) AS id, 
               u.friends_count AS friends_count, 
               u.user_id AS user_id, 
               u.screen_name AS screen_name, 
               u.favourites_count AS favourites_count, 
               u.verified AS verified, 
               u.created_at AS created_at, 
               u.description AS description, 
               u.follower_count AS follower_count, 
               u.influencer_score AS influencer_score
    """,
    "tweets": """
        MATCH (t:Tweet) 
        RETURN elementId(t) AS id, 
               t.annotation_label AS annotation, 
               t.user_id AS user_id, 
               t.tweet_id AS tweet_id, 
               t.favorite_count AS favorite_count, 
               t.text AS text, 
               t.retweet_count AS retweet_count
    """,
    "events": """
        MATCH (e:Event) 
        RETURN elementId(e) AS id, 
               e.name AS name
    """,
    "tweet_tweet_relationships": """
        MATCH (t1:Tweet)-[r]->(t2:Tweet) 
        RETURN elementId(r) AS relationship_id, 
               type(r) AS relationship_type, 
               elementId(t1) AS start_tweet_id, 
               elementId(t2) AS end_tweet_id,
               r.timestamp AS timestamp
    """,
    "user_tweet_relationships": """
        MATCH (u:User)-[r]->(t:Tweet) 
        RETURN elementId(r) AS relationship_id, 
               type(r) AS relationship_type, 
               elementId(u) AS user_id, 
               elementId(t) AS tweet_id,
               r.timestamp AS timestamp
    """,
    ## I added tweet user relationship which is "mention"
    "tweet_user_relationships": """
        MATCH (t:Tweet)-[r]->(u:User) 
        RETURN elementId(r) AS relationship_id, 
               type(r) AS relationship_type, 
               elementId(t) AS tweet_id, 
               elementId(u) AS user_id,
               r.timestamp AS timestamp
    """,
    "tweet_event_relationships": """
        MATCH (t:Tweet)-[r]->(e:Event) 
        RETURN elementId(r) AS relationship_id, 
               type(r) AS relationship_type, 
               elementId(t) AS tweet_id, 
               elementId(e) AS event_id,
               r.timestamp AS timestamp
    """
}

# Function to run query and save results to CSV
def save_query_to_csv(driver, query, filename, database):
    with driver.session(database=database) as session:
        result = session.run(query)
        # Convert to pandas DataFrame
        data = [record.data() for record in result]
        df = pd.DataFrame(data)
        # Save DataFrame to CSV
        f = "csv/"+filename
        df.to_csv(f, index=False)
        print(f"Saved {filename}")

# Run each query and save to corresponding CSV file
for name, query in queries.items():
    save_query_to_csv(driver, query, f"{name}.csv", database)

# Close the Neo4j connection
driver.close()
