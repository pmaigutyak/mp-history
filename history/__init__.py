
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class HistoryConfig(AppConfig):
    name = 'history'
    verbose_name = _("Histories")


default_app_config = 'history.HistoryConfig'
