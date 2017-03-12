

class Team(object):
    fullName = "Detroit Red Wings"
    id = 17
    abbreviation = "DET"

    def __str__(self):
        return str(self.__dict__)


class NhlTvTeams(object):
    """
    ==================================================
    Get NHL TV Team names
    ==================================================
    Class parses all teams so that you can pull from it.

    Arguments:
        parseTeam (etree): ElementTree root

    Returns:
        Team: Team object
    """
    team = Team()
    teams = {}

    def parseTeam(self, team):
        # TODO: this shall be replace by a pull during object init
        t = Team()
        t.fullName = team["Team"]
        t.id = int(team["Id"])
        t.abbreviation = team["TriCode"]
        self.teams[t.abbreviation] = t

    def parseGameContentSchedule(self, tree):
        for item in tree.iter("Standing"):
            self.parseTeam(item.attrib)

    def getTeam(self, search):
        """
        ==================================================
        Get Team
        ==================================================

        Arguments:
            search (int): by team id number like 17
            search (STR): search by teams TriCode/abbreviation like "DET"
            search (str): search by team name like "Detroit Red Wings"

        Returns:
            Team: Team object
        """
        if isinstance(search, int):
            return self._searchTeamById(search)
        if search.isupper():
            return self._searchTeamByAbbreviation(search)

    def _searchTeamByAbbreviation(self, search=str):
        return self.teams[search]

    def _searchTeamById(self, search=int):
        for team in self:
            if search is team.id:
                return team
        raise LookupError('Could not find team with id %s' % search)

    def __iter__(self):
        return iter(self.teams.values())

    def __len__(self):
        return len(self.teams.items())
