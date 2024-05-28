import os


class GitEmulator:
    def __init__(self, folder):
        self.folder = folder
        self.staged_files = []

    def add(self, file_name):
        self.staged_files.append(file_name)

    def status(self):
        staged_files = []
        untracked_files = []
        all_files = os.listdir(self.folder)
        for file_name in self.staged_files:
            staged_files.append(file_name)
        for file_name in all_files:
            if file_name not in self.staged_files and file_name not in [".DS_Store",".git"]:
                untracked_files.append(file_name)
        return staged_files ,untracked_files       

