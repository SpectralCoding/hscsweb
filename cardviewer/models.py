from django.db import models
import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

# Create your models here.
class Cards(Model):
    cardid = columns.Text(primary_key=True)
    COUNTGAME_ARMOR_GAIN = columns.Map(columns.Integer, columns.Integer)
    COUNTGAME_CARDS_CREATED = columns.Map(columns.Integer, columns.Integer)
    COUNTGAME_CARDS_DRAWN = columns.Map(columns.Integer, columns.Integer)
    COUNTGAME_MINIONS_SUMMONED = columns.Map(columns.Integer, columns.Integer)
    COUNT_ATK = columns.Map(columns.Integer, columns.Integer)
    COUNT_DAMAGE = columns.Map(columns.Integer, columns.Integer)
    COUNT_IN_ZONE_DECK = columns.Map(columns.Integer, columns.Integer)
    COUNT_IN_ZONE_GRAVEYARD = columns.Map(columns.Integer, columns.Integer)
    COUNT_IN_ZONE_HAND = columns.Map(columns.Integer, columns.Integer)
    COUNT_IN_ZONE_PLAY = columns.Map(columns.Integer, columns.Integer)
    COUNT_IN_ZONE_REMOVEDFROMGAME = columns.Map(columns.Integer, columns.Integer)
    COUNT_IN_ZONE_SECRET = columns.Map(columns.Integer, columns.Integer)
    COUNT_IN_ZONE_SETASIDE = columns.Map(columns.Integer, columns.Integer)
    COUNT_MULLIGAN_KEEP = columns.Integer()
    COUNT_MULLIGAN_OPPORTUNITY = columns.Integer()
    COUNT_SEEN = columns.Integer()
    COUNT_ZONE_DECK_TO_GRAVEYARD = columns.Map(columns.Integer, columns.Integer)
    COUNT_ZONE_DECK_TO_HAND = columns.Map(columns.Integer, columns.Integer)
    COUNT_ZONE_DECK_TO_PLAY = columns.Map(columns.Integer, columns.Integer)
    COUNT_ZONE_DECK_TO_SECRET = columns.Map(columns.Integer, columns.Integer)
    COUNT_ZONE_DECK_TO_SETASIDE = columns.Map(columns.Integer, columns.Integer)
    COUNT_ZONE_GRAVEYARD_TO_DECK = columns.Map(columns.Integer, columns.Integer)
    COUNT_ZONE_GRAVEYARD_TO_GRAVEYARD = columns.Map(columns.Integer, columns.Integer)
    COUNT_ZONE_GRAVEYARD_TO_HAND = columns.Map(columns.Integer, columns.Integer)
    COUNT_ZONE_HAND_TO_DECK = columns.Map(columns.Integer, columns.Integer)
    COUNT_ZONE_HAND_TO_GRAVEYARD = columns.Map(columns.Integer, columns.Integer)
    COUNT_ZONE_HAND_TO_HAND = columns.Map(columns.Integer, columns.Integer)
    COUNT_ZONE_HAND_TO_PLAY = columns.Map(columns.Integer, columns.Integer)
    COUNT_ZONE_HAND_TO_SECRET = columns.Map(columns.Integer, columns.Integer)
    COUNT_ZONE_HAND_TO_SETASIDE = columns.Map(columns.Integer, columns.Integer)
    COUNT_ZONE_PLAY_TO_DECK = columns.Map(columns.Integer, columns.Integer)
    COUNT_ZONE_PLAY_TO_GRAVEYARD = columns.Map(columns.Integer, columns.Integer)
    COUNT_ZONE_PLAY_TO_HAND = columns.Map(columns.Integer, columns.Integer)
    COUNT_ZONE_PLAY_TO_PLAY = columns.Map(columns.Integer, columns.Integer)
    COUNT_ZONE_PLAY_TO_REMOVEDFROMGAME = columns.Map(columns.Integer, columns.Integer)
    COUNT_ZONE_PLAY_TO_SETASIDE = columns.Map(columns.Integer, columns.Integer)
    COUNT_ZONE_POSITION = columns.Map(columns.Integer, columns.Integer)
    COUNT_ZONE_REMOVEDFROMGAME_TO_GRAVEYARD = columns.Map(columns.Integer, columns.Integer)
    COUNT_ZONE_REMOVEDFROMGAME_TO_REMOVEDFROMGAME = columns.Map(columns.Integer, columns.Integer)
    COUNT_ZONE_SECRET_TO_GRAVEYARD = columns.Map(columns.Integer, columns.Integer)
    COUNT_ZONE_SETASIDE_TO_HAND = columns.Map(columns.Integer, columns.Integer)
    COUNT_ZONE_SETASIDE_TO_PLAY = columns.Map(columns.Integer, columns.Integer)
    COUNT_ZONE_SETASIDE_TO_SETASIDE = columns.Map(columns.Integer, columns.Integer)
    MAX_ATK = columns.Integer()
    MAX_DAMAGE = columns.Integer()
    MAX_NUM_TURNS_IN_PLAY = columns.Integer()

class Games(Model):
    id = columns.UUID(primary_key=True)
    filename = columns.Text()
    submitted = columns.DateTime()
    xmlmd5 = columns.Text()