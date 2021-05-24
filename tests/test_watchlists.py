import pytest
from main.models import Watchlist, CustomUser
from django.test import TestCase

class WatchlistTestCase(TestCase):
    def test_watchlist(self):
        user = CustomUser(password="123456", first_name="john", last_name="doe",
                          email="johndoe@blah.com", language='1234', region='NA')
        user.save()
        watchlist = Watchlist(
            user_id=user.id, title="TheGreatEscape", api_movie_id=123)
        watchlist2 = Watchlist(
            user_id=user.id, title="KingKong", api_movie_id=456)
        watchlist3 = Watchlist(
            user_id=user.id, title="James Bond", api_movie_id=789)
        watchlist.save()
        watchlist2.save()
        watchlist3.save()
        # user.save()
        record = Watchlist.objects.get(id=1)
        # breakpoint()
        self.assertEqual(record.user.first_name, "john")
        self.assertEqual(watchlist.api_movie_id, 123)
        self.assertEqual(watchlist.user_id, 2)
        self.assertEqual(watchlist.title, "TheGreatEscape")
        self.assertEqual(watchlist2.title, "KingKong")
        self.assertEqual(watchlist2.user_id, 2)
        self.assertEqual(watchlist2.api_movie_id, 456)
        self.assertEqual(watchlist3.title, "James Bond")
        self.assertEqual(watchlist3.user_id, 2)
        self.assertEqual(watchlist3.api_movie_id, 789)
        self.assertEqual(len(user.watchlist.all()), 3)
