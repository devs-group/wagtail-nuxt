from wagtail.contrib.modeladmin.options import ModelAdmin
from home.models import InfoCard


class InfoCardAdminMenu(ModelAdmin):
    model = InfoCard
    menu_icon = 'form'
    menu_label = 'Info Karte'
    search_fields = ('title',)
