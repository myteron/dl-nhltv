
class Team(object):
    fullName = "Detroit Red Wings"
    id = 17
    shortName = "Red Wings"
    abbreviation = "DET"
    def __str__(self):
        return str(self.__dict__)

class NhlTvTeams(object):
    """Parsing NHL TV """
    team = Team()
    teams = {}
    
    def parseTeam(self,team):    
        t = Team()
        t.fullName = team["Team"]
        t.id = int(team["Id"])
        t.abbreviation = team["TriCode"]
        self.teams[t.abbreviation]=t
        
    def parseGameContentSchedule(self, tree):
        for item in tree.iter("Standing"):
            self.parseTeam(item.attrib)
                
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