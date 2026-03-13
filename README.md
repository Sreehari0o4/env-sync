# EnvSync

EnvSync is a lightweight CLI tool that securely synchronizes `.env` environment variables across development teams.

Instead of sharing `.env` files through chat, email, or manually copying environment variables, EnvSync encrypts the environment variables and stores them in a private GitHub Gist. Team members can then securely pull the encrypted secrets and restore them locally.

This helps prevent one of the most common developer issues:

> "It works on my machine."

---

# Features

* Secure AES encryption for environment variables
* Sync secrets through GitHub Gist
* Simple CLI workflow
* Automatic configuration storage
* Lightweight developer tool
* Easy team collaboration

---

# How It Works

EnvSync encrypts your `.env` file before syncing it.

```
.env
  ↓
Read variables
  ↓
Encrypt (AES)
  ↓
Upload to GitHub Gist
  ↓
Teammates pull
  ↓
Decrypt
  ↓
Restore .env
```

---

# Installation

## From PyPI (recommended)

Install the EnvSync CLI globally:

```
pip install envsync0o2
```

After installation, the CLI is available as:

```
envsync
```

## From source

Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/env-sync.git
cd env-sync
```

Create a virtual environment:

```
python -m venv venv
```

Activate the environment.

Windows:

```
venv\Scripts\activate
```

Linux / macOS:

```
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Install the CLI tool locally:

```
pip install -e .
```

You can now use the `envsync` command in your terminal.

---

# Requirements

* Python 3.8+
* GitHub account
* GitHub Personal Access Token with `gist` permission

---

# First-Time Setup

Before using EnvSync, you need a **GitHub Personal Access Token**.

### Generate a GitHub Token

1. Go to:

```
https://github.com/settings/tokens
```

2. Click **Generate new token (classic)**
3. Give it a name like:

```
envsync-cli
```

4. Select the permission:

```
gist
```

5. Generate the token and copy it.

Example token:

```
ghp_xxxxxxxxxxxxxxxxx
```

---

# Usage

## 1. Create a `.env` file

Example:

```
API_KEY=123456
DB_PASSWORD=mysecret
PORT=5000
```

---

# First Developer Setup

The first developer creates the shared secret store.

```
envsync push
```

The CLI will ask for the GitHub token.

EnvSync will then:

* Read the `.env` file
* Encrypt the environment variables
* Create a private GitHub Gist
* Save local configuration

Example output:

```
✔ New secret store created

Share this with teammates:

envsync init --gist abcd1234 --key XyZ987
```

---

# Teammate Setup

Teammates initialize EnvSync using the shared credentials.

```
envsync init --gist abcd1234 --key XyZ987
```

This creates a local configuration file:

```
.envsync/config.json
```

---

# Pull Environment Variables

To download the shared environment variables:

```
envsync pull
```

This will:

* Download encrypted secrets
* Decrypt them
* Recreate the `.env` file locally

Example output:

```
.env restored successfully
```

---

# Updating Secrets

When environment variables change, run:

```
envsync push
```

This will update the encrypted secrets stored in the GitHub Gist.

---

# Example Team Workflow

Team leader:

```
envsync push
```

Teammate:

```
envsync init --gist <gist_id> --key <encryption_key>
envsync pull
```

Now both machines share identical `.env` variables.

---

# Project Structure

```
env-sync
│
├── envsync
│   ├── cli.py
│   ├── config.py
│   ├── crypto.py
│   ├── env_parser.py
│   └── gist_api.py
│
├── .envsync
│   └── config.json
│
├── .env
├── requirements.txt
├── setup.py
└── README.md
```

---

# Security Notes

* `.env` files are encrypted before uploading
* Only users with the encryption key can decrypt the secrets
* `.envsync/config.json` is excluded from Git
* Never commit your `.env` file to a repository

Recommended `.gitignore` entries:

```
venv/
__pycache__/
.env
.envsync/
*.pyc
```

---

# Future Improvements

* Token login command (`envsync login`)
* `.env.example` generator
* Environment validation
* Team role management
* Docker integration

---

# License

MIT License

---

# Author

Sreehari S Kumar
