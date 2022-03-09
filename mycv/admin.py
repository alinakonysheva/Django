from django.contrib import admin

# Register your models here.
from mycv.models import Skill, ResumeItem, SkillCategory
# Register your models here.


admin.site.register(Skill)
admin.site.register(SkillCategory)
admin.site.register(ResumeItem)