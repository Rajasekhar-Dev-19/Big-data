# Git Workflow: From Initialization to Push

## 1. Initialize a Git Repository (If Not Cloned)
```bash
git init
```

## 2. Set Up Remote Repository (If Not Cloned)
```bash
git remote add origin https://github.com/Username/sample_repo.git
```

## 3. Clone an Existing Repository (If Not Initialized)
```bash
git clone https://github.com/Username/sample_repo.git
cd YourRepo
```

## 4. Copy Files from Another Directory (Windows)
```bash
xcopy /E /I "F:\source-folder" "D:\YourRepo"
```
(Linux/macOS: `cp -r /source-folder/. .`)

## 5. Check the Status of Your Repository
```bash
git status
```

## 6.1. Stage All Changes for Commit
```bash
git add .
```
## 6.2. Only specific folder
```bash
git add path/to/your/folder you/can/add/many/folders/like/this
```

## 7. Commit the Changes
```bash
git commit -m "Your commit message"
```

## 8. Pull Latest Changes Before Pushing (Avoid Conflicts)
```bash
git pull origin main --rebase
```

## 9. Push Your Changes to GitHub
```bash
git push origin main
```

## 10. Ignore Unwanted Files (`.gitignore`)
Create a `.gitignore` file and add:
```plaintext
venv/
*.log
*.tmp
```
Then commit:
```bash
git add .gitignore
git commit -m "Added .gitignore"
git push origin main
```

## Thank you for your walk-through.....
