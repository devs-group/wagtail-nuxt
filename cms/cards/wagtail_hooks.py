from wagtail.contrib.modeladmin.options import modeladmin_register

from .admin_panel.infocard import InfoCardAdminMenu

# -------------------- Register Buttons in admin panel --------------------
modeladmin_register(InfoCardAdminMenu)
