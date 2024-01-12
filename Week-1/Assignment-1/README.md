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
