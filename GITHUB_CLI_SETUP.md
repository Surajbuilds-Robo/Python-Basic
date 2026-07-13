# 🔗 Connect Your GitHub Account to Ubuntu CLI

> A step-by-step guide to authenticate Git operations for the `Surajbuilds-Robo/Python-Basic` repository (and any other GitHub repo) from the Ubuntu terminal.

---

## 📋 Prerequisites

- Ubuntu (any recent LTS version, e.g. 20.04 / 22.04 / 24.04)
- `git` installed (`sudo apt update && sudo apt install git -y`)
- A GitHub account (e.g. **Surajbuilds-Robo**)

---

## 1️⃣ Configure Git Identity

These values are embedded in every commit you make.

```bash
git config --global user.name  "Surajbuilds-Robo"
git config --global user.email "your-email@example.com"
```

Verify the settings:

```bash
git config --global --list
```

---

## 2️⃣ Choose an Authentication Method

GitHub no longer accepts plain passwords over HTTPS. Use **one** of the two methods below.

---

### Option A — SSH Key (recommended for daily use)

#### Step 1 — Generate an SSH key pair

```bash
ssh-keygen -t ed25519 -C "your-email@example.com"
```

- Press **Enter** to accept the default location (`~/.ssh/id_ed25519`).
- Set a passphrase (optional but recommended).

#### Step 2 — Start the SSH agent and add your key

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

#### Step 3 — Copy the public key

```bash
cat ~/.ssh/id_ed25519.pub
```

Select and copy the entire output (starts with `ssh-ed25519 …`).

#### Step 4 — Add the key to GitHub

1. Go to **GitHub → Settings → SSH and GPG keys**
   (<https://github.com/settings/keys>)
2. Click **New SSH key**.
3. Give it a title (e.g. `Ubuntu Laptop`) and paste the public key.
4. Click **Add SSH key**.

#### Step 5 — Test the SSH connection

```bash
ssh -T git@github.com
```

Expected response:
```
Hi Surajbuilds-Robo! You've successfully authenticated, but GitHub does not provide shell access.
```

#### Step 6 — Clone / set remote over SSH

```bash
# Clone a repo
git clone git@github.com:Surajbuilds-Robo/Python-Basic.git

# Or update an existing remote to use SSH
git remote set-url origin git@github.com:Surajbuilds-Robo/Python-Basic.git
```

---

### Option B — GitHub CLI (`gh`) with HTTPS Token

#### Step 1 — Install GitHub CLI

```bash
sudo apt update
sudo apt install gh -y
```

> If `gh` is not in the default apt repo, install it from GitHub's official package:
> ```bash
> curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg \
>   | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
> echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] \
>   https://cli.github.com/packages stable main" \
>   | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
> sudo apt update && sudo apt install gh -y
> ```

#### Step 2 — Authenticate

```bash
gh auth login
```

Follow the interactive prompts:
1. **What account do you want to log into?** → `GitHub.com`
2. **What is your preferred protocol?** → `HTTPS`
3. **Authenticate Git with your GitHub credentials?** → `Yes`
4. **How would you like to authenticate?** → `Login with a web browser`
5. Copy the one-time code shown in the terminal, press **Enter**, and paste the code in the browser page that opens.

#### Step 3 — Verify authentication

```bash
gh auth status
```

Expected output:
```
✓ Logged in to github.com as Surajbuilds-Robo
✓ Git operations for github.com configured to use https protocol.
```

#### Step 4 — Clone / push over HTTPS

```bash
git clone https://github.com/Surajbuilds-Robo/Python-Basic.git
```

`gh auth login` configures a credential helper automatically, so `git push` / `git pull` will work without a password prompt.

---

## 3️⃣ Verify the Connection — Clone → Pull → Push

```bash
# 1. Clone the repo
git clone git@github.com:Surajbuilds-Robo/Python-Basic.git   # SSH
# OR
git clone https://github.com/Surajbuilds-Robo/Python-Basic.git  # HTTPS

# 2. Enter the directory
cd Python-Basic

# 3. Pull latest changes
git pull

# 4. Make a small change and push
echo "# test" >> test.md
git add test.md
git commit -m "test: verify CLI auth"
git push
```

If the push succeeds without a password prompt, your authentication is working. (Delete `test.md` and push again to clean up.)

---

## 🛠️ Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| `Permission denied (publickey)` | SSH key not added to GitHub or agent not running | Re-run `eval "$(ssh-agent -s)"` + `ssh-add ~/.ssh/id_ed25519`; verify key on GitHub |
| `remote: Support for password authentication was removed` | Using plain password over HTTPS | Switch to SSH or `gh auth login` |
| `fatal: Authentication failed` (HTTPS) | Expired or missing token | Run `gh auth login` again; or update stored credentials with `git credential reject` |
| `Could not resolve hostname github.com` | No network / DNS issue | Check internet connection: `ping github.com` |
| SSH key passphrase asked every time | SSH agent not persisted | Add `ssh-add ~/.ssh/id_ed25519` to `~/.bashrc` or use a keychain tool |
| `gh: command not found` | GitHub CLI not installed | Follow Option B Step 1 above |
| Changes pushed to wrong branch | Wrong branch checked out | Run `git branch` to check; `git checkout main` to switch |

---

## 🔒 Security Tips

- **Never share** your private key (`~/.ssh/id_ed25519`) or personal access tokens.
- Use a **passphrase** when generating your SSH key.
- Revoke any key or token on GitHub as soon as it is no longer needed (**Settings → SSH keys / Tokens**).

---

## 📚 Useful References

- [GitHub Docs — Connecting to GitHub with SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
- [GitHub CLI manual](https://cli.github.com/manual/)
- [GitHub Docs — Caching credentials](https://docs.github.com/en/get-started/getting-started-with-git/caching-your-github-credentials-in-git)
