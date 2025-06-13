**# SimpleFileVCS

A basic Python implementation of a version control system for a single file.  
This script allows you to **edit**, **commit**, **view history**, and **revert** to previous versions of a file's content — ideal for learning core VCS concepts.

## Features

- Edit the content of a simulated file.
- Commit changes with descriptive messages.
- View commit history.
- Revert to any previous version by commit number.

## Usage

```python
vcs = SimpleFileVCS()

vcs.edit("Hello World!")
vcs.commit("Initial commit")

vcs.edit("Updated content")
vcs.commit("Second commit")

vcs.log()       # View history
vcs.revert(1)   # Revert to the first commit
vcs.show()      # Show current file content
**.,,,,,,
