import pytest
from main.models import CustomUser, Thumb
from django.test import TestCase

class ThumbTestCase(TestCase):
    def thumb(self):
        user = CustomUser(password="123456", first_name="john", last_name="doe",
                          email="johndoe@blah.com", language='1234', region='NA')
        user.save()
        thumb = Thumb(
            user_id=user.id, title="TheGreatEscape", api_movie_id=123, api_actor_id=423, api_director_id=412, up=True, api_genre_id=321, api_similar_id=234)
        thumb2 = Thumb(
            user_id=user.id, title="DonkeyKong", api_movie_id=532, api_actor_id=234, api_director_id=876, up=True, api_genre_id=123, api_similar_id=874)
        thumb.save()
        thumb2.save()
        record = Thumb.objects.get(id=1)
        self.assertEqual(record.user.first_name, "john")
        self.assertEqual(thumb.user_id, 3)
        self.assertEqual(thumb.title, "TheGreatEscape")
        self.assertEqual(thumb.api_movie_id, 123)
        self.assertEqual(thumb.api_actor_id, 423)
        self.assertEqual(thumb.api_director_id, 412)
        self.assertEqual(thumb.up, True)
        self.assertEqual(thumb.api_genre_id, 321)
        self.assertEqual(thumb.api_similar_id, 234)
        self.assertEqual(thumb2.user_id, 3)
        self.assertEqual(thumb2.title, "DonkeyKong")
        self.assertEqual(thumb2.api_movie_id, 532)
        self.assertEqual(thumb2.api_actor_id, 234)
        self.assertEqual(thumb2.api_director_id, 876)
        self.assertEqual(thumb2.up, True)
        self.assertEqual(thumb2.api_genre_id, 123)
        self.assertEqual(thumb2.api_similar_id, 874)
