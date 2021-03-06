import mongoengine as me
from flask_login import UserMixin
import app.blueprints.matchmaking.models as m
import app.blueprints.friends.mixins as f
# import app.models.party as p


class Admin(UserMixin, me.Document, f.PartyMixin, m.MatchmakingMixin, f.FriendsMixin):

    meta = {'strict': False}
    username = me.StringField(min_length=3, max_length=16)
    user_tag = me.StringField()
    password_hash = me.StringField(required=True)
    mmr = me.IntField(default=1000)
    datetime_joined_queue = me.DateTimeField()
    party_id = me.StringField()
    in_game_id = me.ListField()
    doodl_coins = me.IntField(default=100)

    def __init__(self, *args, **kwargs):
        super(Admin, self).__init__(*args, **kwargs)
        self.user_tag = f'{self.username}#admin'
