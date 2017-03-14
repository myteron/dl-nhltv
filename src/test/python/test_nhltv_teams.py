import xml.etree.ElementTree as ET
import os
import sys
import unittest

#############
# Expanding PYTHONPATH hack start
# A bit of a hack to make it easier to use cross without project file:
import os
import sys
fullCurrentPath = os.path.realpath(__file__)
currentPath = os.path.dirname(fullCurrentPath)
relativePath = os.path.join(currentPath, "..", "..", "main", "python")
classPath = os.path.realpath(relativePath)
sys.path.insert(0, classPath)
#
#############

from nhltv.teams import Teams

class TestNhlTvTeams(unittest.TestCase):
    """ 
    To run this do the following from anywhere in the project:
    python -m unittest discover -v
    """
    nhlTeams = Teams();
    teams = ""
    
    def setUp(self):
#TODO: extend test to test from sample file(unit) and then from web(integration test)
#       testFile = os.path.join(currentPath, "..", "resources", "Standings")
#       self.teams = self.nhlTeams.parseGameContentSchedule(ET.parse(testFile))
        pass

    def test_getTeamFullNameByAbbreviation(self):
        self.assertEqual(self.nhlTeams.getTeam("DET").fullName, "Detroit Red Wings")

    def test_getTeamIdByAbbreviation(self):
        self.assertEqual(self.nhlTeams.getTeam("DET").id, 17, "expected team id 17")

    def test_iterateOverAllTeams(self):
        print ""
        for team in self.nhlTeams:
            print str(team.id) + " "  + team.abbreviation + " " + team.fullName

    def test_getTeamAbbreviationById(self):
        self.assertEqual(self.nhlTeams.getTeam(17).abbreviation, "DET", "expected team DET")

    def test_raisesLookupErrorExceptionOnInvalidTeamId(self):
        with self.assertRaises(LookupError) as context:
            self.nhlTeams.getTeam(99)
        exceptionStringContains = 'Could not find team' 
        errMsg =  "Missing text '" + exceptionStringContains + "' but got '" + str(context.exception) + "'"
        self.assertTrue(exceptionStringContains in str(context.exception), errMsg)
        
if __name__ == '__main__':
    unittest.main()