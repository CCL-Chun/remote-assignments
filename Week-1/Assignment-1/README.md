# Create a new repository named remote-assignments in your GitHub account
Create a new repository named remote-assignments in your GitHub account

# Generating a Personal Access Token (PAT)
Generate a PAT in Developer settings and save it.

# Create folders in this repository for assignments of each week
## Go back to the mac terminal
GO to the dir you are ready to clone the repo and clone the remote-assignments repo
```
git clone https://github.com/<your name>/remote-assignments.git
cd remote-assignments/
```
## Make Week-1/ to Week-4/ dirs and Assignment-1/ to 4/ in Week-1/ also
```
mkdir Week-{1..4}
mkdir Week-1/Assignment-{1..4}
```
### Add README.md in each dir
```
touch Week-{1..4}/README.md
touch Week-1/Assignment-{1..4}/README.md
```
# Manage and submit your work to GitHub
```
git add .
git commit -m "Create folders in this repository for assignments of each week"
git push origin main
```
* enter the username and password
* use PAT here as password or it will show the error:
***
remote: Support for password authentication was removed on August 13, 2021.
remote: Please see https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
***
* update the credentials stored on your device to avoid entering your PAT every time you push
```
git config --global credential.helper osxkeychain
```

# Connecting to GitHub using SSH keys
* convenient authentication for one or more github accounts
1. First generate your SSH key pair
```
ssh-keygen \
  -t rsa \ 
  -b 4096 \ # 4096 bits encrpytion
  -C "XXX@gmail.com" # optional / comment for your account email
```
  - the key file id\_rsa saved in ~/.ssh by default
  - enter passphrase or keep it empty to next step
2. Put the public key(~/.ssh/id\_rsa.pub) to GitHub(Add new SSH Key)
3. Setup the config file
```
Host            kevin-github
HostName        github.com
User            git
IdentityFile    ~/.ssh/id_rsa
IdentitiesOnly  yes
```
4. Check the setting
```
ssh -T git@kevin-github
# result
Hi CCL-Chun! You've successfully authenticated, but GitHub does not provide shell access.
```
5. Finally, change the HTTPS to SSH authentication
```
git remote set-url origin git@kevin-github:CCL-Chun/test.git
```

