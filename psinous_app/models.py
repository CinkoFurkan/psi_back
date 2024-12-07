from django.db import models

class Link(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    position = models.PositiveIntegerField(default=0, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['position']


class Sublink(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    link = models.ForeignKey(Link, on_delete=models.CASCADE, related_name='sublinks')
    position = models.PositiveIntegerField(default=0, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['position']

class About(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=30,blank=True, null=True)
    text= models.TextField()
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    phone_image = models.ImageField(upload_to='about/', blank=True, null=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50,blank=True, null=True)
    location= models.CharField(max_length=255)
    registration_link= models.URLField(max_length=255)
    summary_link = models.FileField(upload_to='event_summaries/', blank=True, null=True) 
    event_date= models.DateTimeField()
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='event/', blank=True, null=True)

    def __str__(self):
        return self.title

class Announcement(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30,blank=True, null=True)
    text= models.TextField()
    image = models.ImageField(upload_to='announcement/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    phone_image = models.ImageField(upload_to='announcement/', blank=True, null=True)

    def __str__(self):
        return self.title

class Team(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    position = models.PositiveIntegerField(default=0, blank=True, null=True)
    year = models.CharField(max_length=255,blank=True, null=True)
    image = models.ImageField(upload_to='teams/', blank=True, null=True)


    def __str__(self):
        return self.title

class Member(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='members')
    title = models.CharField(max_length=50)
    bio = models.TextField(blank=True, null=True)
    university = models.CharField(max_length=100, blank=True, null=True)
    linkedin = models.URLField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    image = models.ImageField(upload_to='members/', blank=True, null=True)
    position = models.PositiveIntegerField(default=1, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    
class MemberYear(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.CharField(max_length=9) 
    members = models.ManyToManyField('Member', related_name='member_years')

    def _str_(self):
        return self.year

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    short_text = models.TextField()
    text = models.TextField()
    writer = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='blogs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    image = models.ImageField(upload_to='blogs/', blank=True, null=True)
    views_count = models.PositiveIntegerField(default=0) 
    likes_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Subscribe(models.Model):
    id = models.AutoField(primary_key=True)
    mail = models.EmailField(unique=True)
    subscribed_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mail

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255)
    user_email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.TextField()
    title = models.CharField(max_length=255, blank=True, null=True)
    sub_title= models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    image = models.ImageField(upload_to="message/", blank=True, null=True)

class Sponsor(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='sponsor/',blank=True, null=True)
    position = models.PositiveIntegerField(default=0, blank=True, null=True)
    