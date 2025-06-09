class SimpleFileVCS:
    def __init__(self):
        self.versions = []
        self.current_content = ""

    def edit(self, new_content):
        self.current_content = new_content
        print("File content updated.")

    def commit(self, message):
        self.versions.append({
            "message": message,
            "content": self.current_content
        })
        print(f"Committed: '{message}'")

    def show(self):
        print("Current file content:")
        print(self.current_content)

    def log(self):
        if not self.versions:
            print("No commits yet.")
            return
        print("Commit history:")
        for i, v in enumerate(self.versions, 1):
            print(f"{i}: {v['message']}")

    def revert(self, commit_number):
        if commit_number < 1 or commit_number > len(self.versions):
            print("Invalid commit number.")
            return
        self.current_content = self.versions[commit_number - 1]["content"]
        print(f"Reverted to commit {commit_number}: '{self.versions[commit_number - 1]['message']}'")

# Example usage
vcs = SimpleFileVCS()

vcs.edit("Hello World!")
vcs.commit("Initial commit")

vcs.edit("Hello World! Version 2")
vcs.commit("Updated greeting")

vcs.show()
vcs.log()

vcs.revert(1)
vcs.show()
