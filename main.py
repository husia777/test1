from pprint import pprint
import random
import math

TIMESTAMPS_COUNT = 50000

PROBABILITY_SCORE_CHANGED = 0.0001

PROBABILITY_HOME_SCORE = 0.45

OFFSET_MAX_STEP = 3

INITIAL_STAMP = {
    "offset": 0,
    "score": {
        "home": 0,
        "away": 0
    }
}


def generate_stamp(previous_value):
    score_changed = random.random() > 1 - PROBABILITY_SCORE_CHANGED
    home_score_change = 1 if score_changed and random.random() > 1 - \
                             PROBABILITY_HOME_SCORE else 0
    away_score_change = 1 if score_changed and not home_score_change else 0
    offset_change = math.floor(random.random() * OFFSET_MAX_STEP) + 1

    return {
        "offset": previous_value["offset"] + offset_change,
        "score": {
            "home": previous_value["score"]["home"] + home_score_change,
            "away": previous_value["score"]["away"] + away_score_change
        }
    }


def generate_game():
    stamps = [INITIAL_STAMP, ]
    current_stamp = INITIAL_STAMP
    for _ in range(TIMESTAMPS_COUNT):
        current_stamp = generate_stamp(current_stamp)
        stamps.append(current_stamp)

    return stamps


game_stamps = generate_game()

pprint(game_stamps[1:100])


def get_score(game_stamps_, offset):
    '''
        Takes list of game's stamps and time offset for which returns the scores for the home and away teams.
        Please pay attention to that for some offsets the game_stamps list may not contain scores.
    '''

    if game_stamps_ != game_stamps:
        raise ValueError('Входные данные(game_stamps_) должны быть результатом работы функции generate_game')


    try:
        a = [i for i in game_stamps if i['offset'] == offset]
        res = {'offset': a[0]['offset'], 'score': {'away': a[0]['score']['away'] if a[0]['score']['away'] else 0,
                                                   'home': a[0]['score']['home'] if a[0]['score']['home'] else 0}}
        return res
    except KeyError:
        print(f'В списке game_stamps не были сгенерированны результаты для игры под номером {offset}')
    except IndexError:
        raise IndexError('Индекс должен находиться примерно в диапазоне от 0 до 100100')



print(get_score(game_stamps, 3))
