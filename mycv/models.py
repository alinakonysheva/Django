from django.db import models

# Create your models here.


class Skill(models.Model):
    name = models.CharField(max_length=200)
    category =  models.ForeignKey('SkillCategory', on_delete=models.PROTECT)
   
    def __str__(self):
        return '{} - {}'.format(self.name, self.category.name)


class SkillCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ResumeItem(models.Model):
    class Meta:
       ordering = ['-date_from', '-date_till', 'company']

    title = models.CharField(max_length=200)
    date_from = models.DateField()
    date_till = models.DateField()
    description = models.TextField()
    company = models.CharField(max_length=200)
    company_url = models.CharField(max_length=200)
    skills = models.ManyToManyField('Skill', related_name='resume_items')

    def __str__(self):
        return '{} - {} ({}-{})'.format(self.title, self.company, self.date_from.year, self.date_till.year)

