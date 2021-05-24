from main.models import CustomUser, Subscription, Watchlist, Thumb
from rest_framework import serializers


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'name', 'api_provider_id', 'user']


class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watchlist
        fields = ['id', 'title', 'api_movie_id', 'user']


class ThumbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thumb
        fields = ['id', 'title', 'api_movie_id', 'up', 'api_actor_id', 'api_director_id', 'api_genre_id', 'api_similar_id', 'user']

class UserSerializer(serializers.ModelSerializer):
    subscriptions = SubscriptionSerializer(many=True, read_only=True)
    watchlist = WatchlistSerializer(many=True, read_only=True)
    thumbs = ThumbSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'language', 'region', 'subscriptions', 'watchlist', 'thumbs' ]

    # def create_subscriptions(self, validated_data):
    #     subscriptions_data = validated_data.pop('subscriptions')
    #     user = CustomUser.objects.create(**validated_data)
    #     for subscriptions_data in subscriptions_data:
    #         Subscription.objects.create(user=user, **subscription_data)
    #     return subscription
  
    # def create_watchlist(self, validated_data):
    #     watchlists_data = validated_data.pop('watchlists')
    #     user = CustomUser.objects.create(**validated_data)
    #     for watchlists_data in watchlists_data:
    #         Watchlist.objects.create(user=user, **watchlists_data)
    #     return watchlist
    
    # def create_thumbs(self, validated_data):
    #     thumbs_data = validated_data.pop('thumbs')
    #     user = CustomUser.objects.create(**validated_data)
    #     breakpoint ()
    #     for thumbs_data in thumbs_data:
    #         Thumbs.objects.create(user=user, **thumbs_data)
    #     return thumb
