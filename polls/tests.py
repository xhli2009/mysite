import datetime
from django.utils import timezone
from django.test import TestCase

from .models import Question

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_futhre_question(self):
        timet =timezone.now() + datetime.timedelta(days=30)
        future_question =Question(pub_date=timet)
        self.assertIs(future_question.was_published_recently(),False)
