from marshmallow import post_load

from src.domain.models import Game
from src.infrastructure import ma


class GameSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Game

    @post_load
    def make_game(self, data, **kwargs):
        return Game(**data)
