from environnement_Test import Environment
from ia import Agent
import main_Test
import unittest

# python -m unittest
class testUnitaires(unittest.TestCase):

    def setUp(self):
        self.good_anticipe_count = 0
        self.hedonist_table2=[[2,-2,-2],[2,-2,-2],[3,-1,4]]
        

    def test_1(self):
        e = Environment(19,21,18,[1,2])        
        e.mode_Test = True
        e.temp_Test = [18,18.5,19,19.5,20,20.5,21]
        a = Agent(self.hedonist_table2, 4,e)

        main_Test.boucle_action(e,a)
        self.assertEqual(e.temperatureInterieur, e.temperatureVoulue)

    def test_2(self):
        e = Environment(28,21,17,[1,2])
        e.mode_Test = True
        e.temp_Test = [27,26,25,24,23,22,21]
        a = Agent(self.hedonist_table2, 4,e)

        main_Test.boucle_action(e,a)
        self.assertEqual(e.temperatureInterieur, e.temperatureVoulue)

    def test_3(self):
        e = Environment(19,21,25,[1,2])
        e.mode_Test = True
        e.temp_Test = [19.5,20,21]
        a = Agent(self.hedonist_table2, 4,e)

        main_Test.boucle_action(e,a)
        self.assertEqual(e.temperatureInterieur, e.temperatureVoulue)

    def test_4(self):
        e = Environment(10,21,0,[1,2])
        e.mode_Test = True
        e.temp_Test = [9,8,9,10,11,12,13,14,15,16,17,18,19,19,19,20,21]
        a = Agent(self.hedonist_table2, 4,e)

        main_Test.boucle_action(e,a)
        self.assertEqual(e.temperatureInterieur, e.temperatureVoulue)

    # def test_5(self,e):
    #     e = Environment(10,21,0,[1,2])
    #     a = Agent(self.hedonist_table2, 4)
    #     main.world(a, e)

if __name__ == '__main__':
    unittest.main()
