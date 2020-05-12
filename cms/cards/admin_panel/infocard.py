from cards.models import InfoCard
from wagtail.contrib.modeladmin.options import ModelAdmin


class InfoCardAdminMenu(ModelAdmin):
    model = InfoCard
    menu_icon = 'form'
    menu_label = 'Info Card'
    search_fields = ('title',)
