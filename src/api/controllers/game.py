from typing import List

from flask.views import MethodView
from flask_smorest import Blueprint, abort

from src.api.schemas import GameSchema
from src.infrastructure.db import db
from src.domain.models import Game

api: Blueprint = Blueprint("game","game")

@api.route("/games")
class GameResource(MethodView):

    @api.response(status_code=200,schema=GameSchema(many=True))
    def get(self) -> List[Game]:
        """
        Get all games
        """
        return Game.query.all()

    @api.arguments(GameSchema)
    @api.response(status_code=201, schema=GameSchema)
    def post(self, new_game_data: Game) -> Game:
        db.session.add(new_game_data)
        db.session.commit()
        return new_game_data


def _load_game(game_id):
    persisted_game = Game.query.get(game_id)

    if persisted_game is None:
        abort(status_code=404, message=f"Game with id {game_id} not found")

    return persisted_game


@api.route('/games/<int:game_id>')
class GameByIdResource(MethodView):

    @api.response(status_code=200, schema=GameSchema)
    def get(self, game_id):
        return _load_game(game_id)

    @api.arguments(GameSchema)
    @api.response(status_code=200, schema=GameSchema)
    def patch(self, game_data_to_patch, game_id):
        persisted_game = _load_game(game_id)

        persisted_game.title = game_data_to_patch.title

        db.session.commit()
        return persisted_game

    @api.response(status_code=204)
    def delete(self, game_id):
        persisted_game = _load_game(game_id)
        db.session.delete(persisted_game)
        db.session.commit()


