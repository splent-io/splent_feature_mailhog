from splent_framework.hooks.template_hooks import register_template_hook
from flask import current_app


def mailhog_sidebar_link():
    port = current_app.config.get("MAILHOG_UI_HOST_PORT", "8025")
    return (
        '<li class="sidebar-item">'
        f'<a class="sidebar-link" href="http://localhost:{port}" target="_blank">'
        '<i class="align-middle" data-feather="mail"></i> '
        '<span class="align-middle">Mailhog</span>'
        "</a>"
        "</li>"
    )


register_template_hook("layout.authenticated_sidebar", mailhog_sidebar_link)
