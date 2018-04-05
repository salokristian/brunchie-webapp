from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=50, unique=True)
    street_name = models.CharField(max_length=50, default="")
    property_number = models.CharField(max_length=10, default="")
    city = models.CharField(max_length=30, default="")

    def __str__(self):
        return self.name


class Serving(models.Model):
    ALA_CARTE = 1
    BUFFET = 2
    BOTH = 3
    SYSTEM_CHOICES = (
        (ALA_CARTE, "Ala carte"),
        (BUFFET, "Buffet"),
        (BOTH, "Buffet and Ala carte"),
    )

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    restaurant = models.ForeignKey(
        Restaurant,
        models.CASCADE,
        related_name="servings"
        )
    system = models.IntegerField(choices=SYSTEM_CHOICES)
    valid_until = models.DateField(blank=True, null=True)

    def __str__(self):
        return "{}, {}".format(self.name, self.restaurant.name)


class AlaCarteDish(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    serving = models.ForeignKey(
        Serving,
        models.CASCADE,
        related_name="alacarte_dishes"
        )

    def __str__(self):
        return "{}, {}".format(self.name, self.serving)


class BuffetMenu(models.Model):
    name = models.CharField(max_length=50)
    items = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    serving = models.ForeignKey(
        Serving,
        models.CASCADE,
        related_name="buffet_menus"
        )

    def __str__(self):
        return "{}, {}".format(self.name, self.serving)


class OccursAt(models.Model):

    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6
    WEEKDAY_CHOICES = (
        (MONDAY, "Monday"),
        (TUESDAY, "Tuesday"),
        (WEDNESDAY, "Wednesday"),
        (THURSDAY, "Thursday"),
        (FRIDAY, "Friday"),
        (SATURDAY, "Saturday"),
        (SUNDAY, "Sunday")
    )

    starts_at = models.TimeField()
    ends_at = models.TimeField()
    weekday = models.IntegerField(choices=WEEKDAY_CHOICES)
    serving = models.ForeignKey(
        Serving,
        models.CASCADE,
        related_name="occurs_at"
        )

    def __str__(self):
        return "{} {}-{}, {}".format(
            self.WEEKDAY_CHOICES[self.weekday][1],
            self.starts_at.hour,
            self.ends_at.hour,
            self.serving
            )


class Review(models.Model):
    score = models.IntegerField()
    comment = models.TextField(max_length=1000)
    # a review is related to a restaurant via a serving by default
    serving = models.ForeignKey(
        Serving,
        models.CASCADE,
        blank=True,
        null=True,
        related_name="reviews"
    )
    # only needed if a restaurant has not updated its servings
    restaurant = models.ForeignKey(
        Restaurant,
        models.CASCADE,
        blank=True,
        null=True,
        related_name="reviews"
    )
    review_datetime = models.DateTimeField(auto_now_add=True)
    visited_date = models.DateField()

    def __str__(self):
        return "{}/5, {}".format(
            self.score,
            self.serving if self.serving else self.restaurant.name
        )
