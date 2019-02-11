from django.conf import settings
from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField


class Person(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    auth_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True, null=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, null=True, blank=True, max_length=30)
    phone_number = models.CharField(null=True, max_length=30)

    def photo(self, default_path="default_user_photo.png"):
        if self.profile_photo:
            return self.profile_photo
        return default_path

    def __str__(self):
        return self.auth_user.username


class Developer(Person):
    YEARS_ACTIVE_CHOICES = (
        ('1-2', '1-2'),
        ('2-4', '2-4'),
        ('4-above', '4-above'),
    )

    CONTRACT_CHOICES = (
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Contract', 'Contract'),
        ('Remote', 'Remote'),
        ('Freelance', 'Freelance'),
    )

    linkedin_url = models.CharField(max_length=500, null=True, )
    portfolio = models.CharField(max_length=500, blank=True, null=True)
    github_repo = models.CharField(max_length=500, null=True, )
    language = models.CharField(max_length=140, null=True, blank=True)
    framework = models.CharField(max_length=140, null=True, blank=True)
    years = models.CharField(choices=YEARS_ACTIVE_CHOICES, null=True, max_length=30)
    country = CountryField(null=True, max_length=30)
    availability = models.CharField(choices=CONTRACT_CHOICES, null=True, max_length=30)


class Recruiter(Person):
    company = models.CharField(max_length=140, null=True, blank=True)
    job_role = models.CharField(max_length=140, null=True, blank=True)
    industry = models.CharField(max_length=80, null=True, blank=True)
    company_url = models.CharField(max_length=500, null=True, blank=True)


class Job(models.Model):
    ENGAGEMENT_TYPE = (
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Contract', 'Contract'),
        ('Remote', 'Remote'),
        ('Freelance', 'Freelance'),
    )

    JOB_ROLE = (
        ('Full Stack Developer', 'Full Stack Developer'),
        ('Frontend Developer', 'Frontend Developer'),
        ('Backend  Developer', 'Backend  Developer'),
        ('Android  Developer', 'Android  Developer'),
        ('Graphic Designer', 'Graphic Designer'),
        ('IOS Developer', 'IOS Developer'),
        ('Data Scientist', 'Data Scientist'),
    )

    DEV_EXPERIENCE = (
        ('Entry', 'Entry'),
        ('Junior', 'Junior'),
        ('Mid-Level', 'Mid-Level'),
        ('Senior', 'Senior'),
    )

    posted_by = models.ForeignKey(Recruiter, related_name='posted_jobs', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    # field to build beautiful, SEO-friendly URLs for job posts
    # prevent multiple jobs from having the same slug for the same date
    slug = models.SlugField(max_length=250, unique_for_date='created')
    description = models.TextField()
    job_role = models.CharField(max_length=30, choices=JOB_ROLE, default='Full Stack Developer')
    dev_experience = models.CharField(max_length=30, choices=DEV_EXPERIENCE, default='Mid-Level')
    engagement_type = models.CharField(max_length=30, choices=ENGAGEMENT_TYPE, default='Full-time')
    tech_stack = models.CharField(max_length=500)
    num_devs_wanted = models.IntegerField(default=1)
    # monthly remuneration for fulltime, contract etc. budget project for freelance
    remuneration = models.CharField(max_length=45, help_text='in dollars ($)')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    position_filled = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.title

    def get_absolute_url_dev(self):
        """build the canonical URL for Job objects"""
        return reverse(
            'marketplace:dev_job_detail',
            args=[
                self.created.year,
                self.created.strftime('%m'),
                self.created.strftime('%d'),
                self.slug,
            ]
        )


class JobApplication(models.Model):
    job = models.ForeignKey(Job, related_name='job_applications', on_delete=models.CASCADE)
    applied_by = models.ManyToManyField(Developer, related_name='applied_jobs')
    selected_devs = models.ManyToManyField(Developer, related_name='jobs_picked_for', blank=True)
    recommended_devs = models.ManyToManyField(Developer, related_name='recommended_jobs', blank=True)

    class Meta:
        # ordering = ('position_filled',)
        pass

    def __str__(self):
        return self.job.title
