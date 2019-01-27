import peewee

db = peewee.SqliteDatabase("users.db")


class BaseModel(peewee.Model):
    class Meta:
        database = db


class User(BaseModel):
    username = peewee.CharField()