from pathlib import Path

from dotenv import dotenv_values


def read_env(path: Path | str = ".env"):
    """Read environment variables from a .env file.

    Parameters
    ----------
    path: Path | str, optional
        Path to the .env file. Defaults to ".env" in the current directory.
    """
    env_path = Path(path)
    env = dotenv_values(env_path)
    return dict(env)