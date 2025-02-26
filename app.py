
from fastapi import FastAPI
from realtime import get_recent_emails

app = FastAPI()

@app.get("/fetch-emails")
async def fetch_emails():
    
    emails = get_recent_emails()
    return {"Emails": emails}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host = "0.0.0.0", port = 8000)
    