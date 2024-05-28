import subprocess

class GitClient:
    def __init__(self, folder):
        self.folder = folder

    def init(self):
        subprocess.run(["git","init"],cwd=self.folder, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def add(self, file_name):
        subprocess.run(["git", "add", file_name], cwd=self.folder)

    def status(self):
        output = subprocess.run(["git", "status"], capture_output=True, text=True).stdout
        return self.parse_git_status(output)

    def parse_git_status(self, git_status_output):
        all_lines = git_status_output.splitlines()
        all_lines = [line.strip() for line in all_lines if line.strip()]
        lists = {
            'staged': [],
            'untracked': []
        }
        list_name = None

        for line in all_lines:
            if 'Changes to be committed' in line:
                list_name = 'staged'
            elif 'Untracked files' in line:
                list_name = 'untracked'
            elif list_name == 'staged' and (line.startswith('new file:') or line.startswith('modified:') or line.startswith('deleted:')):
                filename = line.split(':', 1)[1].strip()
                lists[list_name].append(filename)
            elif list_name == 'untracked' and line and not line.startswith('(') and not line.startswith('nothing added to commit'):
                lists[list_name].append(line)

        return lists['staged'], lists['untracked']

