from django.db import models


# Create your models here.
class Topic(models.Model):
    """For the learning topics of the user."""

    text = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Modifies the class' string representation."""
        return self.text


class Entry(models.Model):
    """For the entries of the user's learning topics."""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        if len(self.text) <= 50:
            return self.text
        else:
            str = f"{self.text[:50]}..."
            count = 0
            for c in self.text[50:60]:
                if c == " " or c == "\n" or c == "\t" or c == "\r" or c == ",":
                    str = f"{self.text[:50 + count]}..."
                    break
                count += 1
            return str
