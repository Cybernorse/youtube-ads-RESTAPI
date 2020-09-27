from .models import ads_feed
from rest_framework import serializers
from django.contrib.auth.models import User

class Ads_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ads_feed
        fields=(
            'ad_title',
            'orgv_url',
            'ad_url',
            'ad_unlisted',
            'upload_date',
            'ad_genre',
            'view_count',
            'length',
            'ad_likes',
            'ad_dislikes',
            'ad_cta_link',
            'ad_description',
            'ad_links',
            'count',
            'channel_name',
            'ad_channel_link',
            'subscribers',
            'creation_date',
            'total_videos',
        )