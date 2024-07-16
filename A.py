                   
import os
import subprocess
import unittest
import git
from getpass import getpass

def build_project():
    print("Building the project...")
    subprocess.run(["python", "setup.py", "sdist", "bdist_wheel"], check=True)
    print("Build completed.")

def run_tests():
    print("Running tests...")
    loader = unittest.TestLoader()
    suite = loader.discover('.')
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    if result.wasSuccessful():
        print("All tests passed.")
    else:
        print("Some tests failed.")
        exit(1)

def deploy_to_github():
    print("Preparing to deploy to GitHub...")
    repo_path = input("Enter the path to your local git repository: ")
    repo = git.Repo(repo_path)
    
    repo.git.add(update=True)
    commit_message = input("Enter the commit message: ")
    repo.index.commit(commit_message)
    
    origin = repo.remote(name='origin')
    
    username = input("Enter your GitHub username: ")
    password = getpass("Enter your GitHub password: ")
    
    print("Pushing code to GitHub...")
    origin.push()
    
    print("Deployment completed.")

def main():
    print("Python Project CLI Tool")
    print("=======================")
    while True:
        print("1: Build")
        print("2: Test")
        print("3: Deploy")
        print("4: Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            build_project()
        elif choice == "2":
            run_tests()
        elif choice == "3":
            deploy_to_github()
        elif choice == "4":
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()