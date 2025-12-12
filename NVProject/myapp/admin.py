from django.contrib import admin
from myapp.models import DailyRecordSIAF, FemaleBirdsMortality,FemaleBirdsStock, FeedStock, MaleBirdsStock, MaleBirdsMortality, EggOut
# Register your models here.
admin.site.register(DailyRecordSIAF)
admin.site.register(FeedStock)
admin.site.register(MaleBirdsStock)
admin.site.register(MaleBirdsMortality)
admin.site.register(FemaleBirdsStock)
admin.site.register(FemaleBirdsMortality)
admin.site.register(EggOut)