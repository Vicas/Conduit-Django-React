# File for all of our common models that show up all over the project

from django.db import models


class TimestampedModel(models.Model):
    # A timestamp representing when this object was created.
    created_at = models.DateTimeField(auto_now_add=True)

    # A timestamp representing when this object was last updated
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

        # By default, any model that inherits from TimestampedModel should
        # be ordered in reverse-chronological order. We can override this on a
        # per-model basis as needed, but it should be a good ordering for most models.
        ordering = ['-created_at', '-updated_at']

