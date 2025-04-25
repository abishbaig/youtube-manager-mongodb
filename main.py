from pymongo import MongoClient

client = MongoClient("mongodb+srv://ytpyab:ytpyab@tutorialcluster.1p9uugg.mongodb.net/")

db = client["ytmanager"]

video_collections = db["videos"]



def main():
    print(video_collections)


if __name__ == "__main__":
    main()
