import click
import json

from envsync.env_parser import read_env
from envsync.crypto import generate_key, encrypt_data, decrypt_data
from envsync.gist_api import create_gist, get_gist, update_gist
from envsync.config import save_config, load_config


@click.group()
def cli():
    pass

@cli.command()
@click.option("--token", prompt=True)
@click.option("--gist_id", prompt=True)
@click.option("--key", prompt=True)
def init(token, gist_id, key):

    config = {
        "token": token,
        "gist_id": gist_id,
        "key": key
    }

    save_config(config)

    print("Configuration saved successfully!")

@cli.command()
@click.option("--token", prompt=True)
def push(token):

    config = load_config()

    env = read_env()

    env_string = json.dumps(env)

    if not config:
        key = generate_key().decode()
    else:
        key = config["key"]

    encrypted = encrypt_data(env_string, key.encode())

    encrypted_text = encrypted.decode()

    if not config:

        gist = create_gist(token, encrypted_text)

        gist_id = gist["id"]

        save_config({
            "token": token,
            "gist_id": gist_id,
            "key": key
        })

        print("\n✔ New secret store created")

        print("\nShare this with teammates:\n")

        print(f"envsync init --gist {gist_id} --key {key}")

    else:

        gist_id = config["gist_id"]

        update_gist(token, gist_id, encrypted_text)

        print("✔ Secrets updated successfully")


@cli.command()
def pull():

    config = load_config()

    if not config:
        print("Run envsync init first!")
        return

    token = config["token"]
    gist_id = config["gist_id"]
    key = config["key"]

    encrypted_text = get_gist(gist_id, token)

    encrypted_bytes = encrypted_text.encode()

    decrypted = decrypt_data(encrypted_bytes, key.encode())

    env_data = json.loads(decrypted)

    with open(".env", "w") as f:
        for k, v in env_data.items():
            f.write(f"{k}={v}\n")

    print(".env file restored successfully!")

if __name__ == "__main__":
    cli()