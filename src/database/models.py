from peewee import *

sqlite_db = SqliteDatabase('database.db')

class BaseModel(Model):
    class Meta:
        database = sqlite_db

class users(BaseModel):
    user_id = BigIntegerField(primary_key=True)
    step    = TextField(null=True)

class accounts(BaseModel):
    user_id      = BigIntegerField(primary_key=True)
    name         = CharField(max_length=100)
    username     = CharField(max_length=100, default = None, null = True)
    phone_number = CharField(max_length=50)
    session_file = CharField(max_length=100)

class hamsterKombat(BaseModel):
    user_id      = ForeignKeyField(accounts, backref='hamsterKombat')
    url          = CharField(max_length=1000)
    token        = CharField(max_length=500, default = None, null = True)
    last_login   = IntegerField(default=0)
    balance      = IntegerField(default=0)
    profit       = IntegerField(default=0)
    last_check   = IntegerField(default=0)

class config(BaseModel):
    hamsterKombat = BooleanField(default=False)

sqlite_db.connect()
sqlite_db.create_tables([users, config, accounts, hamsterKombat])