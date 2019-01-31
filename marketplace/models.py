from django.db import models


class JobDetails(models.Model):
    ENGAGEMENT_TYPE = (
        ('full_time', 'Full-time'),
        ('remote', 'Remote'),
        ('part_time', 'Part-time'),
        ('contract', 'Contract'),
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
    pass

    class Meta:
        pass

    def __str__(self):
        pass
