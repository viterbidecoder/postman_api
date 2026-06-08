

# Flask Task Manager API

A simple REST API built using Flask for managing tasks with full CRUD operations (Create, Read, Update, Delete).

## Features
- Add new tasks  
- View all tasks  
- View single task  
- Update tasks  
- Delete tasks  
- JSON-based responses  

## Tech Stack
- Python  
- Flask  
- SQLite (or any DB you used)  
- Postman for testing  

## Project Structure
flask-api-project/
├── app.py
├── requirements.txt
├── database.db
└── README.md

## Setup Instructions

1. Clone the repository  
git clone https://github.com/your-username/your-repo-name.git  
cd your-repo-name  

2. Create virtual environment  
python -m venv venv  

Activate:  
Windows → venv\Scripts\activate  
Mac/Linux → source venv/bin/activate  

3. Install dependencies  
pip install -r requirements.txt  

4. Run the application  
python app.py  

Server runs at:  
http://127.0.0.1:5000/

## API Endpoints

GET /tasks → Get all tasks  
GET /tasks/<id> → Get task by ID  
POST /tasks → Create task  
PUT /tasks/<id> → Update task  
DELETE /tasks/<id> → Delete task  

## Example JSON (POST / PUT)
{
  "title": "Learn Flask",
  "completed": false
}

## Testing
Use Postman to test all endpoints.

## Author
Your Name
