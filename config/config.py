import databases
import sqlalchemy

## Preencer os campos abaixo com os dados de sua conexão
userPostgres = ''
passworldPostgres = ''
host = ''
bdname = ''

bdUsuariosURL = "postgresql+asyncpg://" + userPostgres + ":" + passworldPostgres + "@" + host + "/" + bdname

metadata = sqlalchemy.MetaData()
database = databases.Database(bdUsuariosURL)

