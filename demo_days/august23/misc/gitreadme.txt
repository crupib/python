Git stuff to help with mistakes

Spelled last commit message wrong
git commit --amend

Spelling mistake on branch name
git branch -m feature-brunch feature-branch
if already pushed you need to do the following:
git push origin --delete feature-brunch
git push origin feature-branch

Accidentally committed all changes to the master branch
git branch feature-branch
git reset HEAD~ --hard
git checkout feature-branch

Forgot to add a file to that last commit
git add missed-file.txt
git commit --amend

Added a wrong file in the repo
git reset /assets/img/misty-and-pepper.jpg

git reset --soft HEAD~1
git reset /assets/img/misty-and-pepper.jpg
rm /assets/img/misty-and-pepper.jpg
git commit

Oops… I did it again

git reflog

git reset HEAD@{index}
