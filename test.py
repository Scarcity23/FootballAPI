import csv
from google.cloud.sql.connector import Connector

def getconn():
    connector = Connector()
    conn = connector.connect(
        "civil-treat-496117-n0:us-central1:footballdataproject",
        "pymysql",
        user="root",               # Your database user
        password="4`8HILAi+mhtbN?B", # Your database password
        db="projectdata"           # Your database name
    )
    return conn

if __name__ == "__main__":
    print("Connecting to database...")
    connection = getconn()
    
    try:
        with connection.cursor() as cursor:
            # 1. Verify the data exists
            print("Checking table contents...")
            cursor.execute("SELECT COUNT(*) FROM fixture_players;")
            row_count = cursor.fetchone()[0]
            print(f"✅ Success! Found {row_count} rows in the 'fixture_players' table.")

            if row_count > 0:
                # 2. Fetch all data
                print("Fetching data for export...")
                cursor.execute("SELECT * FROM fixture_players;")
                rows = cursor.fetchall()
                
                # Extract the column headers dynamically
                column_names = [description[0] for description in cursor.description]

                # 3. Write data to a CSV file
                csv_filename = "tableau_export.csv"
                with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(column_names)  # Write headers first
                    writer.writerows(rows)         # Write the data rows
                
                print(f"🚀 Export complete! '{csv_filename}' has been generated and is ready for Tableau.")
            else:
                print("⚠️ The table is empty. Double-check your insertion script.")

    except Exception as e:
        print(f"❌ An error occurred: {e}")
        
    finally:
        connection.close()
        print("Connection closed.")



        import json
import pymysql
from google.cloud.sql.connector import Connector

def getconn():
    connector = Connector()
    conn = connector.connect(
        "civil-treat-496117-n0:us-central1:footballdataproject",
        "pymysql",
        user="root",               # Replace with the user found in the Console
        password="4`8HILAi+mhtbN?B", # The password you set during instance creation
        db="projectdata"    # The specific database/schema name inside the instance
    )
    return conn

def create_table(cursor):
    """Creates the fixture_players table if it doesn't already exist."""
    create_table_query = """
    CREATE TABLE IF NOT EXISTS fixture_players (
        id INT AUTO_INCREMENT PRIMARY KEY,
        fixture_id INT,
        team_id INT,
        player_id INT,
        games_minutes INT,
        games_number INT,
        games_position VARCHAR(10),
        games_rating VARCHAR(10),
        games_captain BOOLEAN,
        games_substitute BOOLEAN,
        offsides INT,
        shots_total INT,
        shots_on INT,
        goals_total INT,
        goals_conceded INT,
        goals_assists INT,
        goals_saves INT,
        passes_total INT,
        passes_key INT,
        passes_accuracy VARCHAR(10),
        tackles_total INT,
        tackles_blocks INT,
        tackles_interceptions INT,
        duels_total INT,
        duels_won INT,
        dribbles_attempts INT,
        dribbles_success INT,
        dribbles_past INT,
        fouls_drawn INT,
        fouls_committed INT,
        cards_yellow INT,
        cards_red INT,
        penalty_won INT,
        penalty_commited INT,
        penalty_scored INT,
        penalty_missed INT,
        penalty_saved INT
    );
    """
    cursor.execute(create_table_query)

def insert_data(cursor, data):
    """Parses JSON data and inserts it into the database."""
    insert_query = """
    INSERT INTO fixture_players (
        fixture_id, team_id, player_id, games_minutes, games_number, games_position, games_rating, 
        games_captain, games_substitute, offsides, shots_total, shots_on, goals_total, goals_conceded, 
        goals_assists, goals_saves, passes_total, passes_key, passes_accuracy, tackles_total, tackles_blocks, 
        tackles_interceptions, duels_total, duels_won, dribbles_attempts, dribbles_success, dribbles_past, 
        fouls_drawn, fouls_committed, cards_yellow, cards_red, penalty_won, penalty_commited, penalty_scored, 
        penalty_missed, penalty_saved
    ) VALUES (
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
    )
    """

    # Extract fixture_id from the top-level parameters
    fixture_id = int(data['parameters']['fixture'])

    # Loop through teams and players
    for team_data in data['response']:
        team_id = team_data['team']['id']
        
        for player_data in team_data['players']:
            player_id = player_data['player']['id']
            stats = player_data['statistics'][0]  # Get the first item in the statistics array
            
            # Extract specific stat dictionaries
            g = stats.get('games', {})
            s = stats.get('shots', {})
            go = stats.get('goals', {})
            pa = stats.get('passes', {})
            t = stats.get('tackles', {})
            d = stats.get('duels', {})
            dr = stats.get('dribbles', {})
            f = stats.get('fouls', {})
            c = stats.get('cards', {})
            p = stats.get('penalty', {})

            # Map the values to a tuple for insertion
            values = (
                fixture_id,
                team_id,
                player_id,
                g.get('minutes'),
                g.get('number'),
                g.get('position'),
                g.get('rating'),
                g.get('captain'),
                g.get('substitute'),
                stats.get('offsides'),
                s.get('total'),
                s.get('on'),
                go.get('total'),
                go.get('conceded'),
                go.get('assists'),
                go.get('saves'),
                pa.get('total'),
                pa.get('key'),
                pa.get('accuracy'),
                t.get('total'),
                t.get('blocks'),
                t.get('interceptions'),
                d.get('total'),
                d.get('won'),
                dr.get('attempts'),
                dr.get('success'),
                dr.get('past'),
                f.get('drawn'),
                f.get('committed'),
                c.get('yellow'),
                c.get('red'),
                p.get('won'),
                p.get('commited'),
                p.get('scored'),
                p.get('missed'),
                p.get('saved')
            )

            cursor.execute(insert_query, values)

if __name__ == "__main__":
    # Load JSON file
    with open('data2.json', 'r') as file:
        json_data = json.load(file)

    # Connect to DB and execute
    print("Connecting to database...")
    connection = getconn()
    
    try:
        with connection.cursor() as cursor:
            print("Creating table if not exists...")
            create_table(cursor)
            
            print("Inserting data...")
            insert_data(cursor, json_data)
            
        # Commit the transaction
        connection.commit()
        print("Data successfully inserted.")

    except Exception as e:
        print(f"An error occurred: {e}")
        connection.rollback()
        
    finally:
        connection.close()
        print("Connection closed.")