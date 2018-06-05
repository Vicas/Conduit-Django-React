# We're finally getting into user profiles, baby!

from django.db import models

from conduit.apps.core.models import TimestampedModel


class Profile(TimestampedModel):
    # There is an inherent relationship between the Profile and User models. By creating a one-to-one
    # relationship between the two, we are formalizing this relationship. Every user will have one 
    # (and only one!) related Profile model.
    user = models.OneToOneField(
        'authentication.User', on_delete=models.CASCADE
    )

    # Each user profile will have a field where they can tell other users something about themselves.
    # This field will be empty when the user creates their account, so we specify blank=True
    bio = models.TextField(blank=True)

    # In addition to the bio field, each user may have a profile image or avatar. This field isn't
    # required and may be blank.
    image = models.URLField(blank=True)

    # This is an example of a Many-to-Many relationship, where both sides of the relationship are
    # of the same model. In this case, the model is Profile. As mentioned in the text, this
    # relationship will be one-way. Just because you are following me does not mean I am following
    # you. This is what symmetrical=False does for us.
    follows = models.ManyToManyField(
        'self', 
        related_name='followed_by', 
        symmetrical=False
    )

    favorites = models.ManyToManyField(
        'articles.Article',
        related_name='favorited_by'
    )

    def __str__(self):
        return self.user.username

    def follow(self, profile):
        """
        Follow profile, if we are not already following them
        """
        self.follows.add(profile)

    def unfollow(self, profile):
        """
        Unfollow profile, if we are already following them
        """
        self.follows.remove(profile)

    def is_following(self, profile):
        """
        Returns True if we're following profile, False otherwise
        """
        return self.follows.filter(pk=profile.pk).exists()

    def is_followed_by(self, profile):
        """
        Returns True if profile is following us, False otherwise
        """
        return self.followed_by.filter(pk=profile.pk).exists()

    def favorite(self, article):
        """
        Favorite article, if we haven't already.
        """
        self.favorites.add(article)

    def unfavorite(self, article):
        """
        Unfavorite article, if it is already faved.
        """
        self.favorites.remove(article)

    def has_favorited(self, article):
        """
        Returns True if we have favorited article, False otherwise
        """
        return self.favorites.filter(pk=article.pk).exists()

