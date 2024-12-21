import requests,json,time

team_stats = 'team_stats.json'
team_path = 'teams.json'

url = "https://nfl-football-api.p.rapidapi.com/nfl-team-statistics"

querystring = {"year":"2024","id":"5"}

headers = {
	"x-rapidapi-key": "db828f1485msh78216986a709b58p1c92edjsn81bad99a5993",
	"x-rapidapi-host": "nfl-football-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

class database: #perform vague actions

	# def write(info):
	# 	Jsonfile = open(f"{team_stats}", "w")
	# 	writtenInfo = json.dumps(info, indent=4)
	# 	return Jsonfile.write(writtenInfo)

	def write(info):
		try:
			with open(team_stats, "w") as Jsonfile:
				writtenInfo = json.dumps(info, indent=4)
				Jsonfile.write(writtenInfo)
				print("Write successful")
			return Jsonfile.write(writtenInfo)
		except Exception as e:
			print(f"Error writing to file: {e}")
			return

	def read():
		Jsonfile = open(f"{team_stats}", "r")
		readfile = json.load(Jsonfile)
		return readfile
	
gen_stats = database.read()['statistics']['splits']['categories'][0]['stats']
passing_stats = database.read()['statistics']['splits']['categories'][1]['stats']
rushing_stats = database.read()['statistics']['splits']['categories'][2]['stats']
receiving_stats = database.read()['statistics']['splits']['categories'][3]['stats']
defensive_stats = database.read()['statistics']['splits']['categories'][4]['stats']
int_stats = database.read()['statistics']['splits']['categories'][5]['stats']
kicking_stats = database.read()['statistics']['splits']['categories'][6]['stats']
returning_stats = database.read()['statistics']['splits']['categories'][7]['stats']
punting_stats = database.read()['statistics']['splits']['categories'][8]['stats']
scoring_stats = database.read()['statistics']['splits']['categories'][9]['stats']
misc_stats = database.read()['statistics']['splits']['categories'][10]['stats']

class stats:

	def getgenstats():
		if isinstance(gen_stats, list):
			print(database.read()['statistics']['splits']['categories'][0]['displayName'] + " stats")
			# Loop through the stats list up to its length
			for i in range(min(len(gen_stats), 50)):  # Safe limit to avoid IndexError
				stat = gen_stats[i]
				stat_name = stat.get('name', 'Unknown')  # Use .get() to handle missing keys
				stat_value = stat.get('displayValue', 'N/A')
				stat_rank = stat.get('rankDisplayValue', 'N/A')
				
				main_stats = f"{stat_name}: {stat_value} Rank: {stat_rank}"
				print(main_stats)
		else:
			print("Error: 'general stats' is not a list.")

		return main_stats 

	def getpassingstats():
		if isinstance(passing_stats, list):
			print(database.read()['statistics']['splits']['categories'][1]['displayName'] + " stats")
			# Loop through the stats list up to its length
			for i in range(min(len(passing_stats),50)):  # Safe limit to avoid IndexError
				stat = passing_stats[i]
				stat_name = stat.get('name', 'Unknown')  # Use .get() to handle missing keys
				stat_value = stat.get('displayValue', 'N/A')
				stat_rank = stat.get('rankDisplayValue', 'N/A')

				main_stats = f"{stat_name}: {stat_value} Rank: {stat_rank}"
				print(main_stats)
		else:
			print("Error: 'passing stats' is not a list.")

		return main_stats
	
	def getrushingstats():
		if isinstance(rushing_stats, list):
			print(database.read()['statistics']['splits']['categories'][2]['displayName'] + " stats")
			# Loop through the stats list up to its length
			for i in range(min(len(rushing_stats),50)):  # Safe limit to avoid IndexError
				stat = rushing_stats[i]
				stat_name = stat.get('name', 'Unknown')  # Use .get() to handle missing keys
				stat_value = stat.get('displayValue', 'N/A')
				stat_rank = stat.get('rankDisplayValue', 'N/A')
				
				main_stats = f"{stat_name}: {stat_value} Rank: {stat_rank}"
				print(main_stats)
		else:
			print("Error: 'passing stats' is not a list.")
		return main_stats
	
	def receivingstats():
		if isinstance(receiving_stats, list):
			print(database.read()['statistics']['splits']['categories'][3]['displayName'] + " stats")
			# Loop through the stats list up to its length
			for i in range(min(len(receiving_stats),50)):  # Safe limit to avoid IndexError
				stat = receiving_stats[i]
				stat_name = stat.get('name', 'Unknown')  # Use .get() to handle missing keys
				stat_value = stat.get('displayValue', 'N/A')
				stat_rank = stat.get('rankDisplayValue', 'N/A')
				
				main_stats = f"{stat_name}: {stat_value} Rank: {stat_rank}"
				print(main_stats)
		else:
			print("Error: 'passing stats' is not a list.")
		return main_stats

	def defensivestats():
		if isinstance(defensive_stats, list):
			print(database.read()['statistics']['splits']['categories'][4]['displayName'] + " stats")
			# Loop through the stats list up to its length
			for i in range(min(len(defensive_stats),50)):  # Safe limit to avoid IndexError
				stat = defensive_stats[i]
				stat_name = stat.get('name', 'Unknown')  # Use .get() to handle missing keys
				stat_value = stat.get('displayValue', 'N/A')
				stat_rank = stat.get('rankDisplayValue', 'N/A')

				main_stats = f"{stat_name}: {stat_value} Rank: {stat_rank}"
				print(main_stats)
				
		else:
			print("Error: 'passing stats' is not a list.")
		return main_stats

	def getintstats():
		if isinstance(int_stats, list):
			print(database.read()['statistics']['splits']['categories'][5]['displayName'] + " stats")
			# Loop through the stats list up to its length
			for i in range(min(len(int_stats),50)):  # Safe limit to avoid IndexError
				stat = int_stats[i]
				stat_name = stat.get('name', 'Unknown')  # Use .get() to handle missing keys
				stat_value = stat.get('displayValue', 'N/A')
				stat_rank = stat.get('rankDisplayValue', 'N/A')
				
				main_stats = f"{stat_name}: {stat_value} Rank: {stat_rank}"
				print(main_stats)
				
		else:
			print("Error: 'passing stats' is not a list.")
		return main_stats

	def getkickingstats():
		if isinstance(kicking_stats, list):
			print(database.read()['statistics']['splits']['categories'][6]['displayName'] + " stats")
			# Loop through the stats list up to its length
			for i in range(min(len(kicking_stats),50)):  # Safe limit to avoid IndexError
				stat = kicking_stats[i]
				stat_name = stat.get('name', 'Unknown')  # Use .get() to handle missing keys
				stat_value = stat.get('displayValue', 'N/A')
				stat_rank = stat.get('rankDisplayValue', 'N/A')
				
				main_stats = f"{stat_name}: {stat_value} Rank: {stat_rank}"
				print(main_stats)
				
		else:
			print("Error: 'passing stats' is not a list.")
		return main_stats

	def getreturningstats():
		if isinstance(returning_stats, list):
			print(database.read()['statistics']['splits']['categories'][7]['displayName'] + " stats")
			# Loop through the stats list up to its length
			for i in range(min(len(returning_stats),50)):  # Safe limit to avoid IndexError
				stat = returning_stats[i]
				stat_name = stat.get('name', 'Unknown')  # Use .get() to handle missing keys
				stat_value = stat.get('displayValue', 'N/A')
				stat_rank = stat.get('rankDisplayValue', 'N/A')
				
				main_stats = f"{stat_name}: {stat_value} Rank: {stat_rank}"
				print(main_stats)
				
		else:
			print("Error: 'passing stats' is not a list.")
		return main_stats

	def getpuntingstats():
		if isinstance(punting_stats, list):
			print(database.read()['statistics']['splits']['categories'][8]['displayName'] + " stats")
			# Loop through the stats list up to its length
			for i in range(min(len(punting_stats),50)):  # Safe limit to avoid IndexError
				stat = punting_stats[i]
				stat_name = stat.get('name', 'Unknown')  # Use .get() to handle missing keys
				stat_value = stat.get('displayValue', 'N/A')
				stat_rank = stat.get('rankDisplayValue', 'N/A')
				
				main_stats = f"{stat_name}: {stat_value} Rank: {stat_rank}"
				print(main_stats)
				
		else:
			print("Error: 'passing stats' is not a list.")
		return main_stats

	def getscoringstats():
		if isinstance(scoring_stats, list):
			print(database.read()['statistics']['splits']['categories'][9]['displayName'] + " stats")
			# Loop through the stats list up to its length
			for i in range(min(len(scoring_stats),50)):  # Safe limit to avoid IndexError
				stat = scoring_stats[i]
				stat_name = stat.get('name', 'Unknown')  # Use .get() to handle missing keys
				stat_value = stat.get('displayValue', 'N/A')
				stat_rank = stat.get('rankDisplayValue', 'N/A')
				
				main_stats = f"{stat_name}: {stat_value} Rank: {stat_rank}"
				print(main_stats)
				
		else:
			print("Error: 'passing stats' is not a list.")
		return main_stats

	def getmiscstats():
		if isinstance(misc_stats, list):
			print(database.read()['statistics']['splits']['categories'][10]['displayName'] + " stats")
			# Loop through the stats list up to its length
			for i in range(min(len(misc_stats),50)):  # Safe limit to avoid IndexError
				stat = misc_stats[i]
				stat_name = stat.get('name', 'Unknown')  # Use .get() to handle missing keys
				stat_value = stat.get('displayValue', 'N/A')
				stat_rank = stat.get('rankDisplayValue', 'N/A')
				
				main_stats = f"{stat_name}: {stat_value} Rank: {stat_rank}"
				print(main_stats)
				
		else:
			print("Error: 'passing stats' is not a list.")
		return main_stats

database.write(response.json())
time.sleep(1)
# stats.getgenstats()
stats.getintstats()
# stats.getkickingstats()
# stats.getmiscstats()
# stats.getpassingstats()
# stats.getpuntingstats()
# stats.getreturningstats()
# stats.getrushingstats()
# stats.getscoringstats()

#print("DONE!!")