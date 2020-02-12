from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Tweet
from .forms import TweetForm
from . import serializers


def index(request):
    return render(request, 'microblogging/index.html')


@api_view(['POST'])
@permission_classes((AllowAny, ))
def save_tweet(request):
    """
        Saves tweet to database.
        Receives required fields (name, message) through POST data.
    """
    params = request.data
    name = params['name']
    message = params['message']

    form = TweetForm(data={'name': name,
                           'message': message})

    if form.is_valid():
        form.save()
    else:
        return Response({'error': True, 'msg': ', '.join(form.errors['message'])})

    return Response({'error': False, 'msg': 'Tweet saved'})


class TweetViewSet(viewsets.ReadOnlyModelViewSet):
    """
        Tweets view set
        Returns all tweets
        URL: /tweets/
    """
    permission_classes = (AllowAny,)
    serializer_class = serializers.TweetSerializer
    queryset = Tweet.objects.all()
