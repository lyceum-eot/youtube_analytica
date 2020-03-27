import youtube_dl

import pandas as pd

#set args for youtube-dl, added ignore errors to continue after error
ytargs = {'ignoreerrors': True}

#get the youtube channels list that need to be downloaded
yt_data = pd.read_csv("youtube_channels_list.csv")

ydl = youtube_dl.YoutubeDL(ytopts)

if __name__ == "__main__":
    data = None
    count = 0
    for channel in yt_data["channels"]:
        df = pd.DataFrame()
        with ydl:
            data = ydl.extract_info(channel, download=False)
        entry = [i for i in data['entries'] if i] # remove any none entries
        pd_data = df.from_records(entry, exclude={'formats'}) # load pd.DataFrame
        pd_data.to_csv(str(count) + ".csv") 
        count+=1
