
# ToDo List

ToDo list is a simple web application for short tasks management.

## How to Run

### Prerequisites

1. Install Python 3.8+
2. Install pip

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Yakubovich17/todo-list.git
cd todo-list
```

2. Create and activate a virtual environment:

```bash
python -m venv venv

#On Linux/macOS
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

3. Install dependecies

```bash
pip install -r requirements.txt
```

4. Set Up Environment Variables

Set the following environment variables:

```bash
#On Linux/macOS
export USE_SQLITE=True
export INVITE_CODE="your_invite_code"
export SECRET_KEY="your_secret_key"

#On Windows
set USE_SQLITE=True
set INVITE_CODE="your_invite_key_here"
set SECRET_KEY="your_secret_key_here"
```

**Important:**

- USE_SQLITE: Set to True for local development using SQLite. For production, use a different database and do not set this to True.
- SECRET_KEY: Generate a strong secret key for your application. This is crucial for security and should never be shared or committed to version control.
- INVITE_CODE: Create a unique key used to create new profiles. This should also be kept secure.

5. Run the application

```bash
python run.py
```

The application should now be running on http://localhost:5000
