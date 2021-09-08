# Hw1 editors An ELizabeth Henry and Jacob Smith
# Project designed to 



# Helpful Commands 
The Git add command moves changes to the staging area.
Here is a basic example of using add:
git add <file>       This one i think is the most helpful for us to add but once you add i don't think you need to add again cause it is already tracked i could be wrong though
# 

# ADD command
During the Git add session, you can pick the changes you would like to commit. Before that, you need to start an interactive session:
git add -p   This one is the best command for us 

- These are just because
Use y to stage a specific portion.
Use n to ignore a specific portion.
Use s to divide the portion into smaller parts.
Use e to edit the portion manually.
Use q to exit the interactive session.
#

# Commit command
Git commit command takes a snapshot representing the staged changes.

git commit

After running the Git commit command, you need to type in the description of the commit in the text editor.
This Git commit example shows how you set the description with the commit function:

git commit -m "<message>"     I feel this is the best one for us 

The following example shows how to save a snapshot of changes done in the whole working directory. This code only works for tracked files.
git commit -a
#