from dotenv import dotenv_values

def read_env():
    env = dotenv_values(".env")
    return dict(env)