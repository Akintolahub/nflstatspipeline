import requests

url = "https://nfl-football-api.p.rapidapi.com/nfl-team-statistics"

querystring = {"year":"2024","id":"25"}

headers = {
	"x-rapidapi-key": "db828f1485msh78216986a709b58p1c92edjsn81bad99a5993",
	"x-rapidapi-host": "nfl-football-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()

if response.status_code == 200:
    defensive_stats = data.get('statistics', {}).get('splits', {}).get('categories', [])[4].get('stats', {})
    for i in range(min(len(defensive_stats),50)):  # Safe limit to avoid IndexError
        stat = defensive_stats[i]
        stat_name = stat.get('name', 'Unknown')  # Use .get() to handle missing keys
        stat_value = stat.get('displayValue', 'N/A')
        stat_rank = stat.get('rankDisplayValue', 'N/A')
        
        main_stats = f"{stat_name}: {stat_value} Rank: {stat_rank}"
        print(main_stats)
else:
    print("Api call failed")