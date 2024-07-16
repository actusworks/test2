import os
import subprocess
from git import Repo
import getpass

def build_program():
    print("Building the program...")
    # Here, you would typically run a command to build your program.
    # For a Python program, this might just involve checking that the file exists.
    if not os.path.exists("main.py"):
        print("Error: main.py does not exist.")
        return False
    print("Build successful.")
    return True

def test_program():
    print("Testing the program...")
    # Here, you would typically run a command to test your program.
    # For a Python program, this might involve running a test suite using a testing framework.
    test_result = subprocess.run(["python", "-m", "unittest", "test_main.py"])
    if test_result.returncode != 0:
        print("Error: Tests failed.")
        return False
    print("Tests passed.")
    return True

def deploy_program(username, password, repo_url):
    print("Deploying the program to GitHub...")
    repo = Repo(".")
    repo.git.add(".")
    repo.git.commit("-m", "Deploying the program.")
    repo.git.push("origin", "master")
    print("Deployment successful.")

def main():
    if not build_program():
        return
    if not test_program():
        return

    username = input("Enter your GitHub username: ")
    password = getpass.getpass("Enter your GitHub password: ")
    repo_url = input("Enter your GitHub repository URL: ")

    deploy_program(username, password, repo_url)

if __name__ == "__main__":
    main()