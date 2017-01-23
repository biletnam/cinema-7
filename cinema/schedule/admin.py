from cinema.schedule.models import Seance, Row, Hall, Seat
from django.contrib import admin
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.timezone import localtime


class SeanceAdminForm(ModelForm):
    class Meta:
        model = Seance
        fields = ("start_time", "hall", "movie")

    def clean(self):
        # run the standard clean method first
        cleaned_data = super(SeanceAdminForm, self).clean()
        current_seance_time = cleaned_data.get("start_time")
        hall = cleaned_data.get("hall")

        for seance in Seance.objects.all():
            if seance.hall == hall:
                movie = seance.movie
                start_time = seance.start_time
                end_time = seance.end_time
                if start_time <= current_seance_time <= end_time:
                    start_time_str = localtime(start_time).strftime("%H:%M")
                    end_time_str = localtime(end_time).strftime("%H:%M")
                    raise ValidationError("В это время в зале %s уже идет фильм %s начинающийся в %s и заканчивающийся в %s" % (hall, movie,start_time_str,end_time_str))
        return cleaned_data

class SeanceAdmin(admin.ModelAdmin):
    list_display = ('movie', 'start_time', 'end_time')
    list_filter = ['hall']
    admin_order_field = 'start_time'
    form = SeanceAdminForm


admin.site.register(Seance,SeanceAdmin)
admin.site.register(Row)
admin.site.register(Hall)
admin.site.register(Seat)