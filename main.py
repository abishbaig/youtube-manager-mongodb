from pymongo import MongoClient
from time import sleep
import getpass
import os
from bson import ObjectId

sub_sign_count = 60
sleep_time = 2

client = MongoClient("mongodb+srv://ytpyab:ytpyab@tutorialcluster.1p9uugg.mongodb.net/", tlsAllowInvalidCertificates=True)

db = client["ytmanager"]

video_collections = db["videos"]

# Display all stored videos in a tabular format
def list_all_Videos():
    print("-" * sub_sign_count)
    print("\tVIDEOS LIST MENU")
    print("-" * sub_sign_count)
    print("ID\t\tName\t\tDuration(min)")
    print("-" * sub_sign_count)

    for video in video_collections.find():
        print(f"{video["_id"]}\t{video["video_name"]}\t\t{video["video_duration"]}")

    print("-" * sub_sign_count)

# --------------------- Utility Functions ---------------------

# Check if a video with the same title (case-insensitive) already exists
def video_already_present(video_name):
    for video in video_collections.find():
        if video["video_name"] == video_name:
            return True
    return False

# --------------------- Core Functionalities ---------------------

# Add a new video entry if it doesn't already exist
def add_video():
    print("-" * sub_sign_count)
    print("\tADD VIDEO MENU")
    print("-" * sub_sign_count)
    
    video_name = input("Enter Video Title: ")
    video_duration = input("Enter Video Duration: ")

    if video_already_present(video_name):
        print("-" * sub_sign_count)
        print("Video with this Name Already Present!!!\nFailed to Add!!!")
        print("-" * sub_sign_count)
        return

    print("-" * sub_sign_count)

    # Insert the new video into the database
    video_collections.insert_one({
        "video_name": video_name,
        "video_duration":video_duration
        })

    print("Video Added Successfully...")
    print("-" * sub_sign_count)

# Update an existing video’s title and duration by its ID
def update_video():
    list_all_Videos()
    print("-" * sub_sign_count)
    print("\tUPDATE VIDEO MENU")
    print("-" * sub_sign_count)

    video_index = ObjectId(input("Enter Video ID: "))
    
    isFound = False
    
    for video in video_collections.find():
        if video["_id"] == video_index:
            isFound = True
            break
            
    if isFound:
        print("-" * sub_sign_count)
        video_name = input("Enter Video's New Title: ")
        video_duration = input("Enter Video's New Duration: ")
        
        if video_already_present(video_name):
            print("-" * sub_sign_count)
            print("Video with this Name Already Present!!!\nFailed to Add!!!")
            print("-" * sub_sign_count)
            return
        
        # Update the selected video in the database
        video_collections.update_one({
            "_id":video_index
        },{
            "video_name":video_name,
            "video_duration":video_duration
        })

        print("-" * sub_sign_count)
        print("Video Updated Successfully...")
        print("-" * sub_sign_count)
    else:
        print("-" * sub_sign_count)
        print("ID Not Found!!!\nFailed to Update Video!!!")
        print("-" * sub_sign_count)

# Delete a video by its ID
def delete_video():
    list_all_Videos()
    print("-" * sub_sign_count)
    print("\tDELETE VIDEO MENU")
    print("-" * sub_sign_count)

    video_index = ObjectId(input("Enter Video ID: "))
    
    isFound = False
    
    for video in video_collections.find():
        if video["_id"] == video_index:
            isFound = True
            break
       


    if isFound:
        print("-" * sub_sign_count)
        # Delete the video from the database
        video_collections.delete_one({"_id":video_index})

        print("-" * sub_sign_count)
        print("Video Deleted Successfully...")
        print("-" * sub_sign_count)
    else:
        print("-" * sub_sign_count)
        print("ID Not Found!!!\nFailed to Delete Video!!!")
        print("-" * sub_sign_count)


def main():
    while True:
        sleep(sleep_time)        # Add delay for smoother transitions
        os.system('cls')              # Clear terminal screen (Windows only)

        # Display main menu
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

        # Match user option to corresponding function
        match option:
            case '1':
                sleep(sleep_time)
                os.system('cls')
                list_all_Videos()
                print("\n" + "-" * sub_sign_count)
                getpass.getpass("Press Enter Key to Continue ")  # Wait for user input
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


if __name__ == "__main__":
    main()
