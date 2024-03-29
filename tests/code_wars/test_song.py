from code_challenges.code_wars.song import Song


def test_song():
    mount_moose = Song("Mount Moose", "The Snazzy Moose")

    assert mount_moose.how_many(["John", "Fred", "BOb", "carl", "RyAn"]) == 5
    assert mount_moose.how_many(["JoHn", "Luke", "AmAndA"]) == 2
    assert mount_moose.title == "Mount Moose"
    assert mount_moose.artist == "The Snazzy Moose"
