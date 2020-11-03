import unittest
from game_core.player import Player

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.player = Player(100,100)
        self.MOVE_RIGHT=1
        self.MOVE_LEFT =2
    # def test_move(self):
    #     self.player.move("MOVE_RIGHT")
    #     self.assertEqual(self.player.state, self.MOVE_RIGHT)
    #     self.player.move("MOVE_LEFT")
    #     self.assertEqual(self.player.state, self.MOVE_LEFT)

    def test_change_state(self):
        self.assertEqual("BEGIN",self.player.state)
        self.player.update('Jump')
        self.assertEqual("JUMP",self.player.state)
if __name__ == '__main__':
    unittest.main()
