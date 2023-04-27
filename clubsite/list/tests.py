from django.test import TestCase
from django.urls import reverse
from .models import SponsorName

# Create your tests here.

# Working on making sure all future changes preserve the commas...


def create_multiple_sponsors(n: int, email="example@example.com", name="example"):
    """
    Creates `n` sponsors with the default email being `example@example.com` and the default name being `example`. 
    """

    return SponsorName.objects.bulk_create(
        [
            [SponsorName(sponsor_name=name, sponsor_email=email) for _ in range(n)]
        ]
    )

class ListIndexViewTests(TestCase):
    def test_three_sponsors(self):
        """
        Validates comma separation.
        """
        sponsors = create_multiple_sponsors(3)
        url = reverse("list:clubtemplate")
        self.assertContains(url.context["sponsors"], "example@example.com, example@example.com and example@example.com")
