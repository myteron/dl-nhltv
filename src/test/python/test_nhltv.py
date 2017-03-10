import json
import os
import sys
import unittest

from nhltv import NhlTv


#############
# Expanding PYTHONPATH hack start
# A bit of a hack to make it easier to use cross without project file: 
fullCurrentPath = os.path.realpath(__file__)
currentPath = os.path.dirname(fullCurrentPath)
relativePath = os.path.join(currentPath, "..", "..", "main", "python")
classPath = os.path.realpath(relativePath)
sys.path.insert(0,classPath)

# Expanding PYTHONPATH hack end
#############


class TestStringMethods(unittest.TestCase):
    nhl = NhlTv();
    teams = ""
    
    def setUp(self):
        testFile = os.path.join(currentPath, "..", "resources", "schedule.game.content.media.epg.json")
        with open(testFile, "r") as settingsFile:
            j = json.load(settingsFile)
        self.teams = self.nhl.parseGameContentSchedule(j)

    def test_getTeamFullNameByAbbreviation(self):
        self.assertEqual(self.nhl.getTeam("DET").fullName, "Detroit Red Wings")

    def test_getTeamShortNameByAbbreviation(self):
        self.assertEqual(self.nhl.getTeam("DET").shortName, "Red Wings")

    def test_getTeamIdByAbbreviation(self):
        self.assertEqual(self.nhl.getTeam("DET").id, 17, "expected team id 17")

    def test_iterateOverAllTeams(self):
        for team in self.nhl:
            print str(team.id) + " "  + team.abbreviation + " " + team.fullName

    def test_getTeamAbbreviationById(self):
        self.assertEqual(self.nhl.getTeam(17).abbreviation, "DET", "expected team DET")

    def test_raisesLookupErrorExceptionOnInvalidTeamId(self):
        with self.assertRaises(LookupError) as context:
            self.nhl.getTeam(99)
        exceptionStringContains = 'Could not find team' 
        errMsg =  "Missing text '" + exceptionStringContains + "' but got '" + str(context.exception) + "'"
        self.assertTrue(exceptionStringContains in str(context.exception), errMsg)
        
if __name__ == '__main__':
    unittest.main()