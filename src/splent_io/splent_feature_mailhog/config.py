"""
Mailhog development configuration.

Overrides the mail feature's SMTP settings to point to the local
Mailhog container. This runs AFTER mail's inject_config because
UVL constraints ensure mailhog loads after mail.
"""

import os


def inject_config(app):
    app.config.update(
        {
            "MAIL_SERVER": os.getenv("MAILHOG_HOST", "splent_feature_mailhog"),
            "MAIL_PORT": int(os.getenv("MAILHOG_SMTP_PORT", "1025")),
            "MAIL_USE_TLS": False,
            "MAIL_USE_SSL": False,
            "MAIL_USERNAME": "",
            "MAIL_PASSWORD": "",
            "MAIL_DEFAULT_SENDER": os.getenv("MAIL_DEFAULT_SENDER", "dev@splent.local"),
            "MAILHOG_UI_HOST_PORT": os.getenv("MAILHOG_UI_HOST_PORT", "8025"),
        }
    )
