from django.conf import settings

HOME_LABEL = getattr(
    settings, "DYNAMIC_BREADCRUMBS_HOME_LABEL", "Home"
)
SHOW_AT_BASE_PATH = getattr(
    settings, "DYNAMIC_BREADCRUMBS_SHOW_AT_BASE_PATH", False
)

PATH_XSS_SAFE_MODE = getattr(
    settings, "DYNAMIC_BREADCRUMBS_PATH_XSS_SAFE_MODE", True
)
PATH_MAX_DEPTH = getattr(
    settings, "DYNAMIC_BREADCRUMBS_PATH_MAX_DEPTH", 5
)
PATH_MAX_COMPONENT_LENGTH = getattr(
    settings, "DYNAMIC_BREADCRUMBS_PATH_MAX_COMPONENT_LENGTH", 50
)
