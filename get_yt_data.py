import pandas as pd

yt_data = pd.read_csv("youtube_channels_list.csv")


for i in range(len(yt_data["entries"])):
    for item in data["entries"][i]:
        df["uploader"] = item["uploader"]
        df["license"] = item["license"]
        df["creator"] = item["creator"]
        df["title"] = item["title"]
        df["thumbnail"] = item["thumbnail"]
        df["description"] = item["description"]
        df["categories"] = str(item["categories"])
        df["tags"] = str(item["tags"])
        df["duration"] = item["duration"]
        df["age_limit"] = item["age_limit"]
        df["webpage_url"] = item["webpage_url"]
        df["view_count"] = item["view_count"]
        df["like_count"] = item["like_count"]
        df["dislike_count"] = item["dislike_count"]
        df["average_rating"] = item["average_rating"]
        df["formats"] = str(item["formats"])
        df["is_live"] = item["is_live"]
        df["playlist"] = str(item["playlist"])
        df["playlist_title"] = str(item["playlist_title"])
        df["fps"] = item["fps"]



def get_yt_channels():
    return yt_data["channels"]
