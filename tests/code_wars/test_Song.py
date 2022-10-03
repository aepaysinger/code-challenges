from code_challenges.code_wars.Song import Song


def test_Song():
    mount_moose = Song('Mount Moose', 'The Snazzy Moose')
    
    assert mount_moose.how_many(['John', 'Fred', 'BOb', 'carl', 'RyAn']) == 5
    assert mount_moose.how_many(['JoHn', 'Luke', 'AmAndA']) == 2