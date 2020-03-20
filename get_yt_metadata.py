import youtube_dl

import pandas as pd

yt_data = pd.read_csv("youtube_channels_list.csv")

ydl = youtube_dl.YoutubeDL()

if __name__ == "__main__":
    data = None
    count = 0
    for channel in yt_data["channels"]:
        df = pd.DataFrame()
        with ydl:
            data = ydl.extract_info(channel, download=False)
        pd_data = df.from_records(data['entries'])
        pd_data.to_csv(str(count) + ".csv")
        count+=1
