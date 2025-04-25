from pymongo import MongoClient      # MongoDB client for Python
from time import sleep              # To introduce delays
import getpass                      # To pause the screen until user presses Enter
import os                           # For clearing the terminal
from bson import ObjectId           # To work with MongoDB document IDs
from dotenv import load_dotenv      # To load environment variables from .env file

# Load environment variables
load_dotenv()

# Fetch DB credentials securely
db_url = os.environ.get("DB_URL")

# UI and delay settings
sub_sign_count = 60
sleep_time = 2

# MongoDB connection (with certificate warning bypass)
client = MongoClient( db_url, tlsAllowInvalidCertificates=True)

# Select database and collection
db = client["ytmanager"]
video_collections = db["videos"]

# ---------------------- Display All Videos ----------------------

def list_all_Videos():
    sub_sign_count = 100
    print("-" * sub_sign_count)
    print("\t\t\tVIDEOS LIST MENU")
    print("-" * sub_sign_count)
    print("ID\t\t\t\tName\t\tDuration(min)")
    print("-" * sub_sign_count)

    # Display each video as a row
    for video in video_collections.find():
        print(f"{video['_id']}\t{video['video_name']}\t\t{video['video_duration']}")

    print("-" * sub_sign_count)

# ---------------------- Utility Functions ----------------------

# Check if a video with the same name already exists
def video_already_present(video_name):
    for video in video_collections.find():
        if video["video_name"] == video_name:
            return True
    return False

# ---------------------- Add New Video ----------------------

def add_video():
    print("-" * sub_sign_count)
    print("\tADD VIDEO MENU")
    print("-" * sub_sign_count)
    
    video_name = input("Enter Video Title: ")
    video_duration = input("Enter Video Duration: ")

    # Prevent duplicate video entries
    if video_already_present(video_name):
        print("-" * sub_sign_count)
        print("Video with this Name Already Present!!!\nFailed to Add!!!")
        print("-" * sub_sign_count)
        return

    print("-" * sub_sign_count)

    # Insert the video into MongoDB
    video_collections.insert_one({
        "video_name": video_name,
        "video_duration": video_duration
    })

    print("Video Added Successfully...")
    print("-" * sub_sign_count)

# ---------------------- Update Existing Video ----------------------

def update_video():
    list_all_Videos()
    print("-" * sub_sign_count)
    print("\tUPDATE VIDEO MENU")
    print("-" * sub_sign_count)

    video_index = ObjectId(input("Enter Video ID: "))
    isFound = False

    # Check if video with given ID exists
    for video in video_collections.find():
        if video["_id"] == video_index:
            isFound = True
            break
            
    if isFound:
        print("-" * sub_sign_count)
        video_name = input("Enter Video's New Title: ")
        video_duration = input("Enter Video's New Duration: ")
        
        # Prevent overwriting with an existing title
        if video_already_present(video_name):
            print("-" * sub_sign_count)
            print("Video with this Name Already Present!!!\nFailed to Add!!!")
            print("-" * sub_sign_count)
            return

        # Update the video document in MongoDB
        video_collections.update_one(
            {"_id": video_index},
            {"$set": {
                "video_name": video_name,
                "video_duration": video_duration
            }}
        )

        print("-" * sub_sign_count)
        print("Video Updated Successfully...")
        print("-" * sub_sign_count)
    else:
        print("-" * sub_sign_count)
        print("ID Not Found!!!\nFailed to Update Video!!!")
        print("-" * sub_sign_count)

# ---------------------- Delete a Video ----------------------

def delete_video():
    list_all_Videos()
    print("-" * sub_sign_count)
    print("\tDELETE VIDEO MENU")
    print("-" * sub_sign_count)

    video_index = ObjectId(input("Enter Video ID: "))
    isFound = False

    # Check if the video exists
    for video in video_collections.find():
        if video["_id"] == video_index:
            isFound = True
            break

    if isFound:
        print("-" * sub_sign_count)

        # Remove the video from MongoDB
        video_collections.delete_one({"_id": video_index})

        print("-" * sub_sign_count)
        print("Video Deleted Successfully...")
        print("-" * sub_sign_count)
    else:
        print("-" * sub_sign_count)
        print("ID Not Found!!!\nFailed to Delete Video!!!")
        print("-" * sub_sign_count)

# ---------------------- Main Menu ----------------------

def main():
    while True:
        sleep(sleep_time)
        os.system('cls')  # Clear terminal (works on Windows)

        # Display main options
        print("-" * sub_sign_count)
        print("\tYoutube Videos Manager (MongoDB)")
        print("-" * sub_sign_count)
        print("[1] List All Videos")
        print("[2] Add a Video")
        print("[3] Update a Video")
        print("[4] Delete a Video")
        print("[5] Exit")
        print("-" * sub_sign_count)

        option = input("Enter Option: ")
        print("-" * sub_sign_count)

        # Route to selected operation
        match option:
            case '1':
                sleep(sleep_time)
                os.system('cls')
                list_all_Videos()
                print("\n" + "-" * sub_sign_count)
                getpass.getpass("Press Enter Key to Continue ")
            case '2':
                sleep(sleep_time)
                os.system('cls')
                add_video()
            case '3':
                sleep(sleep_time)
                os.system('cls')
                update_video()
            case '4':
                sleep(sleep_time)
                os.system('cls')
                delete_video()
            case '5':
                print("-" * sub_sign_count)
                print("\tApp Exiting...")
                print("-" * sub_sign_count)
                break
            case _:
                print("Wrong Option Entered!!!")
                sleep(sleep_time)
                os.system('cls')

# ---------------------- Entry Point ----------------------

if __name__ == "__main__":
    main()