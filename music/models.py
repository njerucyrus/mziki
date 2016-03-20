from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class UserAccount(User):
    user = models.OneToOneField(User)
    FirstName = models.CharField("First Name", max_length=30)
    LastName = models.CharField("Last Name", max_length=30)
    phone_no = models.CharField(max_length=20)
    class Meta:
        verbose_name_plural = 'HITS254 Users'
    def __str__(self):
        return self.phone_no

class Artist(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    other_name = models.CharField(max_length=20, blank=True)
    stage_name = models.CharField(max_length=20)
    phone_no = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    email = models.EmailField("Email Address", blank=True)
    photo = models.FileField(upload_to='images', blank=True)
    slug = models.SlugField(max_length=20)

    class Meta:
        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'

    def __str__(self):
        return self.stage_name

#model for the song category
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

#model for storing the songs in the db
class Song(models.Model):
    SONG_TYPE = (
        ('MP3', 'MP3'),
        ('MP4', 'MP4'),
    )
    song_title = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, related_name='songs', on_delete=models.CASCADE)
    song_type = models.CharField(max_length=3, choices=SONG_TYPE)
    category = models.ForeignKey(Category, related_name='songs', on_delete=models.CASCADE)
    song_url = models.FileField(upload_to='media')
    snippet_url = models.FileField(upload_to='media/snippets', blank=True)
    download_point = models.PositiveIntegerField(default=0)
    slug = models.SlugField(max_length=50)
    date_released = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Song'
        verbose_name_plural = 'Songs'

    def get_absolute_url(self):
        return reverse('music:artists', args=[self.id, self.slug])

    def __str__(self):
        return self.song_title

#store the points of the users who topup credit
class Hits254Ac(models.Model):
    phone_no = models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    point_earned = models.PositiveIntegerField()
    date_update = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Hits254AC'
        verbose_name_plural = 'Hits254ACs'

    def __str__(self):
        return str(self.phone_no)


# holding the Topup transactions
class AirtimeTopUp(models.Model):
    username = models.CharField(max_length=50)
    phone_no = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    point_earned = models.PositiveIntegerField(default=0)
    transaction_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'AirtimeTopUp'
        verbose_name_plural = 'AirtimeTopUps'

    def __str__(self):
        return str(self.phone_no)


class Rates(models.Model):
    amount = models.PositiveIntegerField()
    points = models.PositiveIntegerField()
    date_modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Rate'
        verbose_name_plural = 'Rates'
        ordering = ('amount',)

    def __str__(self):
        return str(self.amount)


class Downloads(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    download_count = models.PositiveIntegerField(default=0)
    # User location
    user_location = models.CharField(max_length=50, blank=True)
    updated = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=50)

    class Meta:
        verbose_name_plural = 'Downloads'
        ordering = ('download_count',)

    def __str__(self):
        return self.song


class ArtistAccount(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song = models.ForeignKey(Downloads, on_delete=models.CASCADE)
    # amount earned from the song download
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    slug =models.SlugField(max_length=50)
    class Meta:
        verbose_name_plural = 'Artist Accounts'
    def __str__(self):
        return self.song



