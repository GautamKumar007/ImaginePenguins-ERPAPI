from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

from .serializer import FeedSerializer
from UserApi.models import User
from . models import Feed, Feed_Like, Feed_Tag, Comment, Comments_Comment, Comments_Like, Tag

# Create your views here.

# For Feeds
class Feedlist(APIView):

    def get(self, request):
        l = []
        item = Feed.objects.all()
        print(len(item))
        for i in range(len(item)):
            data = {}
            email = item[i].user_id
            feed_id = item[i].id
            print('\nThis is id : ', feed_id)

            username = User.objects.get(email=email).username
            print('the username is : ',username)

            data['username'] = username
            data['no_of_likes'] = len(Feed_Like.objects.filter(feed_id=feed_id))
            data['no_of_comments'] = len(Comment.objects.filter(feed_id=feed_id))
            data['img'] = item[i].img
            data['place'] = item[i].place
            data['time'] = item[i].post_time
            data['desc'] = item[i].description
            l.append(data)
        return Response(l)

    def post(self, request):
        serializer = FeedSerializer(data=request.POST)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = 'Successfully registerd as User'
            print(data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(data)


class Feeditem(APIView):

    def get_item(self, pk):
        try:
            return Feed.objects.get(id=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        item = self.get_item(pk)
        data={}
        data['username'] = User.objects.get(email=item.user_id).username
        data['no_of_likes'] = len(Feed_Like.objects.filter(feed_id=item.id))
        data['no_of_comments'] = len(Comment.objects.filter(feed_id=item.id))
        data['img'] = item.img
        data['place'] = item.place
        data['time'] = item.post_time.now()
        data['desc'] = item.description
        return Response(data)
