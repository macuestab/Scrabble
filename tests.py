import unittest
import scrabble

class CheckScrabbleTest(unittest.TestCase):
    def test_score_world(self):
        self.assertEqual(scrabble.score_word("BROWNIE"), 15, "Expected score_word(\"BROWNIE\") to return 15")
        
    def test_play_game(self):   
        player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexy Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
        expected_result = {}
        for player in player_to_words.keys():
            with self.subTest(player):
                result_sum = 0
                for word in player_to_words[player]:         
                    result_sum += scrabble.score_word(word)
                expected_result.update({player: result_sum})
                message = "Expected play_game(" + str(player) + ": " + str(player_to_words[player]) + ") to return " + str(expected_result)
                self.assertEqual(scrabble.play_game({player: player_to_words[player]}), expected_result, message)
                

# Run tests
unittest.main()