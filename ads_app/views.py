from django.shortcuts import render
from .models import ads_feed
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from ads_app.serializer import Ads_Serializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from django_filters.filterset import FilterSet

class adsFilter(FilterSet):
    class Meta:
        model = ads_feed
        fields = [ 
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
            ]

class UserViewSet(viewsets.ModelViewSet):

    queryset = ads_feed.objects.all().order_by('upload_date')
    serializer_class = Ads_Serializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend,OrderingFilter,]
    filter_class = adsFilter
    paginate_by=10
    # ordering_fields = [ 
    #         'ad_title',
    #         'orgv_url',
    #         'ad_url',
    #         'ad_unlisted',
    #         'upload_date',
    #         'ad_genre',
    #         'view_count',
    #         'length',
    #         'ad_likes',
    #         'ad_dislikes',
    #         'ad_cta_link',
    #         'ad_description',
    #         'ad_links',
    #         'count',
    #         'channel_name',
    #         'ad_channel_link',
    #         'subscribers',
    #         'creation_date',
    #         'total_videos',
    #         ]

    # def upload_dates1(request):
    #     queryset=module_feed.objects.all().order_by('-upload_date')

    # def view_counts(request):
    #     queryset=module_feed.objects.all().order_by('view_count')

    # def view_counts1(request):
    #     queryset=module_feed.objects.all().order_by('-view_count')

    # def yesterdays(request):
    #     queryset=module_feed.objects.all().order_by('yesterday')

    # def yesterdays1(request):
    #     queryset=module_feed.objects.all().order_by('-yesterday')

    # def lastdays(request):
    #     queryset=module_feed.objects.all().order_by('last_30_days')

    # def lastdays1(request):
    #     queryset=module_feed.objects.all().order_by('-last_30_days')

    # def length(request):
    #     queryset=module_feed.objects.all().order_by('length')

    # def length1(request):
    #     queryset=module_feed.objects.all().order_by('-length')