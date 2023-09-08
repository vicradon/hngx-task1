import uvicorn
from datetime import datetime
import os
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get('/')
def main():
    return RedirectResponse("/docs")


@app.get('/api/')
def root(slack_name, track):
    current_date = datetime.now()
    day_of_week = current_date.weekday()
    day_name = current_date.strftime("%A")

    return {
        "slack_name": slack_name,
        "current_day": day_name,
        "utc_time": current_date.isoformat(),
        "track": track,
        "github_file_url": "https://github.com/vicradon/hngx-task1/blob/main/main.py",
        "github_repo_url": "https://github.com/vicradon/hngx-task1",
        "status_code": 200
    }

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", port=port, log_level="info", reload=True)