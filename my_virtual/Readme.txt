pipenv shell — spawns a shell within the virtualenv.
pipenv install [package] — installs the provided 
   package and adds them to Pipfile.
pipenv install —installs all packages from Pipfile.
pipenv install -r requirements.txt 
  — installs all libraries from the requirements.txt file and adds them to the Pipfile.
pipenv install --ignore-pipfile 
  — installs all dependencies, according
     to the Pipfile.lock file ignoring the Pipfile current version.
pipenv lock — generates Pipfile.lock.
pipenv install [package]--dev 
    — installs package and adds it with the dev-package mark
pipenv check — checks for vulnerabilities.
pipenv graph — displays currently–installed dependency graph information.

1. pipenv shell
2. cat Pipfile
3. python --version
4. pipenv install requests
5. pipenv install nose --dev
6. cat Pipfile
7. vi requirements.txt
8. pipenv install -r requirements.txt
9. cat Pipfile
10. pipenv check
11. pipenv graph
12. vi .env
14. pipenv run python
    >>> import os
    >>> os.environ['API_KEY']
