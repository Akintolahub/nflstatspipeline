import requests, csv
from google.cloud import storage


url = "https://nfl-football-api.p.rapidapi.com/nfl-team-statistics"

querystring = {"year":"2024","id":"25"}

headers = {
	"x-rapidapi-key": "db828f1485msh78216986a709b58p1c92edjsn81bad99a5993",
	"x-rapidapi-host": "nfl-football-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()
csv_filename = '49ers_def_rankings_2024.csv'
field_names = ['Defensive Stat', 'Rank']

# get relevant defensive stats
# get the rank of the defensive stats

class DefensiveStats:

    def get_forced_fumbles():
        if response.status_code == 200:
            gen_stats = data.get('statistics', {}).get('splits', {}).get('categories', [])[0].get('stats', {})
            stat = gen_stats[2]
            # stat_name = stat.get('displayName', 'Unknown')  # Use .get() to handle missing keys
            stat_rank = stat.get('rankDisplayValue', 'N/A')
            main_stats = f"{stat_rank}"
            print(main_stats)
        else:
            print("Api call failed")
        return main_stats

    def get_fumble_touchdowns():
        if response.status_code == 200:
            gen_stats = data.get('statistics', {}).get('splits', {}).get('categories', [])[0].get('stats', {})
            stat = gen_stats[4]
            # stat_name = stat.get('displayName', 'Unknown')  # Use .get() to handle missing keys
            stat_rank = stat.get('rankDisplayValue', 'N/A')
            main_stats = f"{stat_rank}"
            print(main_stats)
        else:
            print("Api call failed")
        return main_stats


    def get_tackle_assists():
        if response.status_code == 200:
            gen_stats = data.get('statistics', {}).get('splits', {}).get('categories', [])[4].get('stats', {})
            stat = gen_stats[0]
            # stat_name = stat.get('displayName', 'Unknown')  # Use .get() to handle missing keys
            stat_rank = stat.get('rankDisplayValue', 'N/A')
            main_stats = f"{stat_rank}"
            print(main_stats)
        else:
            print("Api call failed")
        return main_stats

    def get_sacks():
        if response.status_code == 200:
            gen_stats = data.get('statistics', {}).get('splits', {}).get('categories', [])[4].get('stats', {})
            stat = gen_stats[14]
            # stat_name = stat.get('displayName', 'Unknown')  # Use .get() to handle missing keys
            stat_rank = stat.get('rankDisplayValue', 'N/A')
            main_stats = f"{stat_rank}"
            print(main_stats)
        else:
            print("Api call failed")
        return main_stats

    def get_solo_tackles():
        if response.status_code == 200:
            gen_stats = data.get('statistics', {}).get('splits', {}).get('categories', [])[4].get('stats', {})
            stat = gen_stats[17]
            # stat_name = stat.get('displayName', 'Unknown')  # Use .get() to handle missing keys
            stat_rank = stat.get('rankDisplayValue', 'N/A')
            main_stats = f"{stat_rank}"
            print(main_stats)
        else:
            print("Api call failed")
        return main_stats


    def get_tackles_for_loss():
        if response.status_code == 200:
            gen_stats = data.get('statistics', {}).get('splits', {}).get('categories', [])[4].get('stats', {})
            stat = gen_stats[20]
            # stat_name = stat.get('displayName', 'Unknown')  # Use .get() to handle missing keys
            stat_rank = stat.get('rankDisplayValue', 'N/A')
            main_stats = f"{stat_rank}"
            print(main_stats)
        else:
            print("Api call failed")
        return main_stats

    def get_total_tackles():
        if response.status_code == 200:
            gen_stats = data.get('statistics', {}).get('splits', {}).get('categories', [])[4].get('stats', {})
            stat = gen_stats[22]
            # stat_name = stat.get('displayName', 'Unknown')  # Use .get() to handle missing keys
            stat_rank = stat.get('rankDisplayValue', 'N/A')
            main_stats = f"{stat_rank}"
            print(main_stats)
        else:
            print("Api call failed")
        return main_stats

    def get_yards_allowed():
        if response.status_code == 200:
            gen_stats = data.get('statistics', {}).get('splits', {}).get('categories', [])[4].get('stats', {})
            stat = gen_stats[23]
            # stat_name = stat.get('displayName', 'Unknown')  # Use .get() to handle missing keys
            stat_rank = stat.get('rankDisplayValue', 'N/A')
            main_stats = f"{stat_rank}"
            print(main_stats)
        else:
            print("Api call failed")
        return main_stats

    def get_points_allowed():
        if response.status_code == 200:
            gen_stats = data.get('statistics', {}).get('splits', {}).get('categories', [])[4].get('stats', {})
            stat = gen_stats[24]
            # stat_name = stat.get('displayName', 'Unknown')  # Use .get() to handle missing keys
            stat_rank = stat.get('rankDisplayValue', 'N/A')
            main_stats = f"{stat_rank}"
            print(main_stats)
        else:
            print("Api call failed")
        return main_stats


    def get_interceptions():
        if response.status_code == 200:
            gen_stats = data.get('statistics', {}).get('splits', {}).get('categories', [])[5].get('stats', {})
            stat = gen_stats[0]
            # stat_name = stat.get('displayName', 'Unknown')  # Use .get() to handle missing keys
            stat_rank = stat.get('rankDisplayValue', 'N/A')
            main_stats = f"{stat_rank}"
            print(main_stats)
        else:
            print("Api call failed")
        return main_stats

    def get_defensive_points():
        if response.status_code == 200:
            gen_stats = data.get('statistics', {}).get('splits', {}).get('categories', [])[9].get('stats', {})
            stat = gen_stats[0]
            # stat_name = stat.get('displayName', 'Unknown')  # Use .get() to handle missing keys
            stat_rank = stat.get('rankDisplayValue', 'N/A')
            main_stats = f"{stat_rank}"
            print(main_stats)
        else:
            print("Api call failed")
        return main_stats

DefensiveStats = {
    "Forced Fumbles": DefensiveStats.get_forced_fumbles(),
    "Fumble Touchdowns": DefensiveStats.get_fumble_touchdowns(),
    "Tackle Assists": DefensiveStats.get_tackle_assists(),
    "Sacks": DefensiveStats.get_sacks(),
    "Solo Tackles": DefensiveStats.get_solo_tackles(),
    "Tackles for Loss": DefensiveStats.get_tackles_for_loss(),
    "Total Tackles": DefensiveStats.get_total_tackles(),
    "Yards Allowed": DefensiveStats.get_yards_allowed(),
    "Points Allowed": DefensiveStats.get_points_allowed(),
    "Interceptions": DefensiveStats.get_interceptions(),
    "Defensive Points": DefensiveStats.get_defensive_points()
}
    
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    for stat, rank in DefensiveStats.items():
        writer.writerow({'Defensive Stat': stat, 'Rank': rank})

print(f"Data fetched and written to '{csv_filename}'")

# Upload the CSV file to GCS
bucket_name = 'bkt-ranking-data'
storage_client = storage.Client()
bucket = storage_client.bucket(bucket_name)
destination_blob_name = f'{csv_filename}'  # The path to store in GCS

blob = bucket.blob(destination_blob_name)
blob.upload_from_filename(csv_filename)

print(f"File {csv_filename} uploaded to GCS bucket {bucket_name} as {destination_blob_name}")