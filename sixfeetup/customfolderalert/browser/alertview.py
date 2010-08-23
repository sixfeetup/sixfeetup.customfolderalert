import os
from Products.Five import BrowserView
from zope.interface import implements
from sixfeetup.customfolderalert.browser.interfaces import IAlertView

class AlertView(BrowserView):
    """View class for alerts methods"""
    implements(IAlertView)

    def isAlertDisabled(self):
        """Is the custom folder alert disabled?"""
        TRUISMS = ['yes', 'y', 'true', 'on']
        DISABLED = os.environ.get("DISABLE_CUSTOMFOLDER_ALERT", None)

        return DISABLED is not None and DISABLED.lower() in TRUISMS

