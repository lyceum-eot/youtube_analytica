#from get_channels import get_yt_channels
#from get_yt_data import get_data
import youtube_dl

import pandas as pd

yt_data = pd.read_csv("youtube_channels_list.csv")

ydl = youtube_dl.YoutubeDL()

if __name__ == "__main__":
    data = None
    count = 5
    for channel in yt_data["channels"][count:]:
        pd = pd.DataFrame()
        with ydl:
            data = ydl.extract_info(channel, download=False)
        pd_data = pd.DataFrame.from_records(data['entries'])
        pd_data.to_csv(count + ".csv")
