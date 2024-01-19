# Import necessary libraries and modules
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import os.path
import pickle
from datetime import datetime, timezone, timedelta

# Define the scope for Google API access
SCOPES = ['https://www.googleapis.com/auth/tasks']

# Class to handle operations related to Google Tasks
class Tasks:
  def __init__(self):
    creds = None
    # Check if the authentication token is already stored
    if os.path.exists('token.pickle'):
      with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
    # If credentials are not valid or expired, refresh or create new credentials            
    if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
      else:
        flow = InstalledAppFlow.from_client_secrets_file(
          'credentials.json', SCOPES
        )
        creds = flow.run_local_server(port=0)
      with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)
    # Initialize the Google Tasks API service
    self.service = build('tasks', 'v1', credentials=creds)
  
  # Retrieve tasks from Google Tasks
  def get_tasks(self):
    return self.service.tasks().list(tasklist='@default', showCompleted=True, showHidden=True, showDeleted=True).execute()

  # Delete a task in Google Tasks
  def delete_task(self, taskId):
    self.service.tasks().delete(tasklist='@default', task=taskId).execute()
    pass

  # Create a new task in Google Tasks
  def create_task(self, task):
    return self.service.tasks().insert(tasklist='@default', body=task).execute()

  # Mark a task as complete in Google Tasks
  def complete_task(self, taskId):
    self.service.tasks().complete(tasklist='@default', task=taskId).execute()
  
  # Update an existing task in Google Tasks
  def update_task(self, taskId, task):
    return self.service.tasks().update(tasklist='@default', task=taskId, 
      body={
       "id": task["id"],
       "title": task["title"],
       "notes": task["notes"],
       "due": task["due"],
       "status": task["status"]
      }
    ).execute()
  
  # Calculate the due date for a task based on given tags
  def get_due_date(self, tags):
    tags = [tag.lower() for tag in tags]
    current_date = datetime.now(timezone.utc)
    current_day = current_date.weekday()
    days_left = 7
    # Assign days left based on the tag
    # 'today', 'tomorrow', specific weekdays, 'week', or 'month'
    if(len(tags) == 0):
      days_left = 7
    elif "today" in tags:
      days_left = 0
    elif "tomorrow" in tags:
      days_left = 1
    elif "week" in tags:
      days_left = 7
    elif "month" in tags:
      days_left = 30
    elif "monday" in tags:
      days_left = (0 - current_day) % 7
    elif "tuesday" in tags:
      days_left = (1 - current_day) % 7
    elif "wednesday" in tags:
      days_left = (2 - current_day) % 7
    elif "thursday" in tags:
      days_left = (3 - current_day) % 7
    elif "friday" in tags:
      days_left = (4 - current_day) % 7
    elif "saturday" in tags:
      days_left = (5 - current_day) % 7
    elif "sunday" in tags:
      days_left = (6 - current_day) % 7

    # Calculate the due date and return in RFC 3339 format
    return (
      datetime.now(timezone.utc) +
      timedelta(days=days_left)
    ).isoformat().replace("+00:00", "Z")
