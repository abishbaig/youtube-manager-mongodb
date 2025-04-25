# YouTube Videos Manager (MongoDB)


## Description  
A terminal-based Python application that lets you manage a collection of YouTube videos using **MongoDB** as the backend. You can **list**, **add**, **update**, and **delete** videos with ease from the terminal.

---

## Features

- List all saved YouTube videos from the MongoDB database
- Add new videos with title and duration
- Update existing videos by entering their unique MongoDB ID
- Delete videos from the collection
- Uses `pymongo` to connect to MongoDB Atlas
- Environment variables are used to secure credentials with `.env` file
- Handles duplicates and invalid IDs gracefully

---

## How It Works

- Connects to a MongoDB Atlas cluster using credentials stored in environment variables (`DB_USERNAME`, `DB_PASSWORD`)
- Videos are stored as documents in a collection named `videos` inside the `ytmanager` database
- Utilizes Python packages: `pymongo`, `bson`, `dotenv`, `os`, `time`, and `getpass`
- Terminal interface supports smooth navigation with screen clearing and pauses

---

## Run It Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/abishbaig/youtube-manager-mongodb.git
   cd youtube-manager-mongodb
2. **Install Required Packages:**
    ```bash
    pip install pymongo python-dotenv
3. **Create a .env file in the root directory and add your credentials:**
    ```bash
    DB_USERNAME=your_mongodb_username
    DB_PASSWORD=your_mongodb_password
4. **Run the application:**
    ```bash
    python your_script_name.py