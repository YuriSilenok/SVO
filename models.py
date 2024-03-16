from peewee import SqliteDatabase, Model, IntegerField, CharField, ForeignKeyField


db = SqliteDatabase('db.db')

class Table(Model):
    """Промежуточный класс в наследовании, 
что бы не прописывать вс всех наследниках, класс Meta"""

    class Meta:
        database = db

class User(Table):
    """Пользователь телеграма"""

    tg_id = IntegerField()

class Specialty(Table):
    """Военная специальность"""

    name = CharField()

class Player(Table):
    """Игрок"""

    user = ForeignKeyField(User)
    specialty = ForeignKeyField(Specialty)
    nickname = CharField(default = 'Новый игрок', max_length=30)
    x = IntegerField()
    y = IntegerField()

db.connect()
db.create_tables([User, Specialty, Player], safe=True)
db.close()
