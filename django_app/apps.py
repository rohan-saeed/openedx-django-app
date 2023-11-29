"""
django_app Django application initialization.
"""
from django.apps import AppConfig

from edx_django_utils.plugins.constants import (
    PluginURLs, PluginSettings, PluginContexts
)

from openedx.core.djangoapps.plugins.constants import ProjectType


class DjangoAppConfig(AppConfig):
    """
    Configuration for the django_app Django application.
    """

    name = 'django_app'
    plugin_app = {
        PluginURLs.CONFIG: {
            ProjectType.LMS: {
                PluginURLs.NAMESPACE: 'django_app',
                PluginURLs.REGEX: r'^api/list_and_filter/',
                PluginURLs.RELATIVE_PATH: 'urls',
            },
        },
    }
