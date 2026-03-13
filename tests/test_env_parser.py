from envsync.env_parser import read_env
from pathlib import Path


def test_read_env(tmp_path):

    env_file = tmp_path / ".env"

    env_file.write_text("API_KEY=123\nPORT=5000\n")

    result = read_env(env_file)

    assert result["API_KEY"] == "123"
    assert result["PORT"] == "5000"