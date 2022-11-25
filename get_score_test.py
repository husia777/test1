from unittest import main, TestCase
from main import get_score, game_stamps


class TestGet_score(TestCase):
    def test_a(self):
        self.assertEqual(get_score(game_stamps, 0), game_stamps[0])

    def test_index_not_found(self):
        with self.assertRaises(IndexError) as e:
            get_score(game_stamps, -6)
        self.assertEqual('Индекс должен находиться примерно в диапазоне от 0 до 100100', e.exception.args[0])



if __name__ == '__main__':
    main()
