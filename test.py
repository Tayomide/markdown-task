# import necessary modules
from task_service import Tasks
import re
import hashlib
import json
import os

# Set the directory of the to-do list file
TODO_DIR = os.getenv("TODO_DIR")

# Initialize the Tasks service
task_service = Tasks()
tasks = {}
prev_tasks = {}

# Define function to create a task
def create_task(task):
  return task_service.create_task({
    "title": task["text"],
    "notes": task["text"],
    "due": task_service.get_due_date(task["tags"]),
    "status": "completed" if task["completed"] else "needsAction"
  })

# Define function to update a task
def update_task(taskId):
  return task_service.update_task(prev_tasks[taskId]["id"], prev_tasks[taskId])

# Define function to delete a task
def delete_task(calendar_id):
  task_service.delete_task(calendar_id)

# Read the to-do list file and store its content in 'text'
text = ""
with open(TODO_DIR, "r") as f:
  text = f.read()

# Define pattern to find tasks in the to-do list
pattern = r'- \[[x ]\].*'
matches = re.findall(pattern, text)

# Process each task found in the to-do list
for match in matches:
  task_text = re.search(r'\] (.+?)( #|$)', match).group(1).strip()
  tags = re.findall(r'#[\w-]+', match)
  completed = '[x]' in match
  id = hashlib.md5(task_text.encode()).hexdigest()

  if task_text:
    task = {
      "text": task_text,
      "tags": [tag[1:] for tag in tags],
      "completed": completed
    }
  tasks[id] = task

# Try to load previous tasks from 'db.json'
try:
  with open("db.json", "r") as f:
    prev_tasks = json.loads(f.read())
except Exception:
  prev_tasks = {}

# Initialize lists to track new, updated, and deleted tasks
new_tasks = []
updated_tasks = []
deleted_tasks = []

# Determine if tasks are new, updated, or deleted
for taskId in tasks:
  # Check for new tasks
  if(taskId not in prev_tasks):
    new_tasks.append(taskId)
  else:
    # Check for updated tasks
    if (tasks[taskId]["completed"] and "completed" not in prev_tasks[taskId]):
      prev_tasks[taskId]["status"] = "completed"
      updated_tasks.append(taskId)
    elif(not tasks[taskId]["completed"] and "completed" in prev_tasks[taskId]):
      prev_tasks[taskId]["status"] = "needsAction"
      updated_tasks.append(taskId)
    elif("daily" in tasks[taskId]["tags"] or "weekly" in tasks[taskId]["tags"] or "monthly" in tasks[taskId]["tags"]):
      prev_tasks[taskId]["due"] = task_service.update_due_date(tasks[taskId]["tags"], prev_tasks[taskId]["due"])
      updated_tasks.append(taskId)
    else:
      tasks[taskId] = prev_tasks[taskId]

# Check for tasks that are in previous tasks but not in current tasks (deleted tasks)
for taskId in prev_tasks:
  if(taskId not in tasks):
    deleted_tasks.append(taskId)

# Perform delete, create, and update operations for tasks
for taskId in deleted_tasks:
  delete_task(prev_tasks[taskId]["id"])
  print("deleted task", prev_tasks[taskId])

for taskId in new_tasks:
  tasks[taskId] = create_task(tasks[taskId])
  print("created task", tasks[taskId])

for taskId in updated_tasks:
  tasks[taskId] = update_task(taskId)
  print("updated task", tasks[taskId])

# Save the current state of tasks to 'db.json'
with open("db.json", "w") as f:
  f.write(json.dumps(tasks))