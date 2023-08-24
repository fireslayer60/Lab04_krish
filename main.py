class FlightTable:
    def __init__(self):
        self.data = [
            {"Location": "Mumbai", "Team 01": "India", "Team 02": "Sri Lanka", "Timing": "DAY"},
            {"Location": "Delhi", "Team 01": "England", "Team 02": "Australia", "Timing": "DAY-NIGHT"},
            {"Location": "Chennai", "Team 01": "India", "Team 02": "South Africa", "Timing": "DAY"},
            {"Location": "Indore", "Team 01": "England", "Team 02": "Sri Lanka", "Timing": "DAY-NIGHT"},
            {"Location": "Mohali", "Team 01": "Australia", "Team 02": "South Africa", "Timing": "DAY-NIGHT"},
            {"Location": "Delhi", "Team 01": "India", "Team 02": "Australia", "Timing": "DAY"}
        ]
    
    def search_team_matches(self, team_name):
        matches = [match for match in self.data if team_name in (match["Team 01"], match["Team 02"])]
        return matches
    
    def search_location_matches(self, location):
        matches = [match for match in self.data if match["Location"] == location]
        return matches
    
    def search_timing_matches(self, timing):
        matches = [match for match in self.data if match["Timing"] == timing]
        return matches

def main():
    flight_table = FlightTable()

    print("Choose search parameter:")
    print("1. List of all the matches of a Team")
    print("2. List of Matches on a Location")
    print("3. List of Matches based on timing")
    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        team_name = input("Enter team name: ")
        matches = flight_table.search_team_matches(team_name)
    elif choice == 2:
        location = input("Enter location: ")
        matches = flight_table.search_location_matches(location)
    elif choice == 3:
        timing = input("Enter timing: ")
        matches = flight_table.search_timing_matches(timing)
    else:
        print("Invalid choice!")
        return

    if matches:
        print("Search Results:")
        for match in matches:
            print(match)
    else:
        print("No matches found.")

if __name__ == "__main__":
    main()
