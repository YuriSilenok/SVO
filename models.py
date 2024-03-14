from peewee import SqliteDatabase, Model, IntegerField, CharField, ForeignKeyField


db = SqliteDatabase('db.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    tg_id = IntegerField()

class Specialty(BaseModel):
    name = CharField()

class Player(BaseModel):
    user = ForeignKeyField(User)
    specialty = ForeignKeyField(Specialty)
    nickname = CharField(default = 'Новый игрок', max_length=30)
    x = IntegerField()
    y = IntegerField()

db.connect()
db.create_tables([User, Specialty, Player], safe=True)
db.close()