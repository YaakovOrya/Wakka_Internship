import os
import shutil
from GitClient import GitClient
from GitEmulator import GitEmulator


def setup_files(folder_path, files):
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.makedirs(folder_path)
    
    for file_name in files:
        with open(os.path.join(folder_path, file_name), 'w') as file:
            file.write("")
    os.chdir(folder_path)


def run_test(folder_path, files):
    setup_files(folder_path, files)

    # Setup emulator
    emulator = GitEmulator(folder_path)
    emulator.add("file.py")
    emulator.add("file2.py")

    # Setup real git
    git_client = GitClient(folder_path)
    git_client.init()
    git_client.add("file.py")
    git_client.add("file2.py")

    # Get git status results
    emulator_staged_files, emulator_untracked_files = emulator.status()
    real_git_staged_files, real_git_untracked_files  = git_client.status()

    # Compare results
    if set(emulator_staged_files) != set(real_git_staged_files):
        print("Mismatch in staged files:")
        print("Emulator staged files:", emulator_staged_files)
        print("Real Git staged files:", real_git_staged_files)

    if set(emulator_untracked_files) != set(real_git_untracked_files):
        print("Mismatch in untracked files:")
        print("Emulator untracked files:", emulator_untracked_files)
        print("Real Git untracked files:", real_git_untracked_files)

    # Cleanup
    shutil.rmtree(folder_path)


if __name__ == "__main__":
    folder_path = os.path.join(os.path.expanduser('~'), 'temp', 'yaakov', 'files')
    files = ["file.py", "file2.py", "file3.py"]
    setup_files(folder_path, files)
    run_test(folder_path, files)

