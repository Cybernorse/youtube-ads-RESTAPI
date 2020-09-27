import csv 
import os
from ads_app.models import ads_feed
# from rest_api_app.models.

def run():
    db_file=open('/code/scripts/dataset_v16.csv')
    readfile=csv.reader(db_file)

    ads_feed.objects.all().delete()

    count=1

    for data in readfile:
        if count==1:
            pass
        else:
            print(data)
            ads_feed.objects.create(
                ad_title=data[0],
                orgv_url=data[1],
                ad_url=data[2],
                ad_unlisted=data[3],
                upload_date=data[4],
                ad_genre=data[5],
                view_count=data[6],
                length=data[7],
                ad_likes=data[8],
                ad_dislikes=data[9],
                ad_cta_link=data[10],
                ad_description=data[11],
                ad_links=data[12],
                count=data[13],
                channel_name=data[14],
                ad_channel_link=data[15],
                subscribers=data[16],
                creation_date=data[17],
                total_videos=data[18],
                )
        count+=1
