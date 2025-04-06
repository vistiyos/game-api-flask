import pytest
from assertpy import assert_that, soft_assertions

from src.domain.models import Game


@pytest.fixture(scope='function', autouse=True)
def clean_up(app):
    yield

    with app.app_context():
        Game.query.delete()

def test_get_all_games(client, db_interface):
    game = Game(title="Test Game")
    db_interface.session.add(game)
    db_interface.session.commit()

    response = client.get("/games")
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.json[0]).is_equal_to(dict(id=1,title="Test Game"))

def test_post_game(client):
    game_data = {
        "title": "Test Game",
    }

    response = client.post("/games", json=game_data)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(201)
        assert_that(response.json["title"]).is_equal_to(game_data["title"])
        assert_that(response.json).contains_key("id")

def test_get_game_by_id(client, db_interface):
    game = Game(title="Test Game")
    db_interface.session.add(game)
    db_interface.session.commit()

    response = client.get(f'/games/{game.id}')
    assert_that(response.status_code).is_equal_to(200)
    with soft_assertions():
        assert_that(response.json).is_equal_to(dict(id=game.id, title=game.title))

def test_patch_game(client, db_interface):
    game = Game(title="Test Game")
    db_interface.session.add(game)
    db_interface.session.commit()

    response = client.patch(f'/games/{game.id}', json={ "title": "Another Title"})
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.json['title']).is_equal_to("Another Title")

def test_delete_game_by_id(client, db_interface):
    game = Game(title="Test Game")
    db_interface.session.add(game)
    db_interface.session.commit()

    response = client.delete(f'/games/{game.id}')
    assert_that(response.status_code).is_equal_to(204)
    