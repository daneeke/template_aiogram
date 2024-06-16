from environs import Env

env = Env()
env.read_env()

token = env('TOKEN')

DATABASE_PATH = 'app/data/sql.db'
