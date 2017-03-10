
class Team(object):
    fullName = "Detroit Red Wings"
    id = 17
    shortName = "Red Wings"
    abbreviation = "DET"
    def __str__(self):
        return str(self.__dict__)

class NhlTv(object):
    """Parsing NHL TV """
    team = Team()
    teams = {}
    
    def parseTeam(self,team):    
        t = Team()
        t.shortName = team["teamName"] 
        t.fullName = team["name"] 
        t.id = team["id"]
        t.abbreviation = team["abbreviation"]
        self.teams[t.abbreviation]=t
        
    def parseGameContentSchedule(self, schedule):

        for dates in schedule["dates"]:
            for games in dates["games"]:
                self.parseTeam(games["teams"]["home"]["team"])
                self.parseTeam(games["teams"]["away"]["team"])
                
    def getTeam(self, search):
        if isinstance(search, int):
            return self.searchTeamById(search)
        if search.isupper():
            return self.searchTeamByAbbreviation(search)

    def searchTeamByAbbreviation(self, search=str):   
        return self.teams[search]
    
    def searchTeamById(self, search=int):   
        for team in self:
            if search is team.id:
                return team
        raise LookupError('Could not find team with id %s' % search)

    def __iter__(self):
        return iter(self.teams.values())
        
    def __len__(self):
        return len(self.teams.items())