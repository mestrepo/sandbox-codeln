from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField

from django.db.models.signals import post_save
from django.dispatch import receiver


class Base(models.Model):
    GENDER_CHOICES = (
        ('male', 'male'),
        ('female', 'female'),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True, null=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, null=True, blank=True, max_length=30)
    phone_number = models.CharField(null=True, max_length=30)

    def __str__(self):
        return self.user.username

    def photo(self, default_path="default_user_photo.png"):
        if self.profile_photo:
            return self.profile_photo
        return default_path

    def get_absolute_url(self):
        return '/marketplace/base/'

    @property
    def full_name(self):
        return self.user.get_full_name()

    @property
    def date_joined(self):
        return self.user.date_joined

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Base.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.base.save()


class Developer(Base):
    YEARS_ACTIVE_CHOICES = (
        ('1-2', '1-2'),
        ('2-4', '2-4'),
        ('4-above', '4-above'),
    )

    CONTRACT_CHOICES = (
        ('full_time', 'Full-time'),
        ('part_time', 'Part-time'),
        ('contract', 'Contract'),
        ('remote', 'Remote'),
        ('freelance', 'Freelance'),
    )

    linkedin_url = models.CharField(max_length=500, null=True, )
    portfolio = models.CharField(max_length=500, blank=True, null=True)
    github_repo = models.CharField(max_length=500, null=True, )
    language = models.CharField(max_length=140, null=True, blank=True)
    framework = models.CharField(max_length=140, null=True, blank=True)
    years = models.CharField(choices=YEARS_ACTIVE_CHOICES, null=True, max_length=30)
    country = CountryField(null=True, max_length=30)
    availability = models.CharField(choices=CONTRACT_CHOICES, null=True, max_length=30)


class Recruiter(Base):
    company = models.CharField(max_length=140, null=True, blank=True)
    job_role = models.CharField(max_length=140, null=True, blank=True)
    industry = models.CharField(max_length=80, null=True, blank=True)
    company_url = models.CharField(max_length=500, null=True, blank=True)


class JobDetail(models.Model):
    ENGAGEMENT_TYPE = (
        ('full_time', 'Full-time'),
        ('part_time', 'Part-time'),
        ('contract', 'Contract'),
        ('remote', 'Remote'),
        ('freelance', 'Freelance'),
    )

    JOB_ROLE = (
        ('full_stack_developer', 'Full Stack Developer'),
        ('frontend_developer', 'Frontend Developer'),
        ('backend_developer', 'Backend  Developer'),
        ('android_developer', 'Android  Developer'),
        ('graphic_designer', 'Graphic Designer'),
        ('ios_developer', 'IOS Developer'),
        ('data_scientist', 'Data Scientist'),
    )

    DEV_EXPERIENCE = (
        ('entry', 'Entry'),
        ('junior', 'Junior'),
        ('mid-level', 'Mid-Level'),
        ('senior', 'Senior'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    job_role = models.CharField(max_length=30, choices=JOB_ROLE, default='full_stack_developer')
    dev_experience = models.CharField(max_length=30, choices=DEV_EXPERIENCE, default='mid-level')
    engagement_type = models.CharField(max_length=30, choices=ENGAGEMENT_TYPE, default='full_time')
    tech_stack = models.CharField(max_length=500)
    num_devs_wanted = models.IntegerField(default=1)
    # monthly remuneration for fulltime, contract etc. budget project for freelance
    remuneration_dollars = models.CharField(max_length=45)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.title


class Job(models.Model):
    job_detail = models.OneToOneField(JobDetail, on_delete=models.CASCADE)
    posted_by = models.ForeignKey(Recruiter, related_name='posted_jobs', on_delete=models.CASCADE)
    applied_by = models.ManyToManyField(Developer, related_name='applied_jobs')
    recommended_devs = models.ManyToManyField(Developer, related_name='recommended_jobs')
    selected_devs = models.ManyToManyField(Developer, related_name='jobs_picked_for')
    position_filled = models.BooleanField(default=False)

    class Meta:
        ordering = ('position_filled',)

    def __str__(self):
        return self.job_detail
