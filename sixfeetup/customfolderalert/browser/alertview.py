import os
from Products.CMFCore.utils import getToolByName
from Products.Five import BrowserView


class AlertView(BrowserView):
    """View class for alerts methods"""

    def is_alert_disabled(self):
        """Is the custom folder alert disabled?"""
        TRUISMS = ['yes', 'y', 'true', 'on']
        DISABLED = os.environ.get("DISABLE_CUSTOMFOLDER_ALERT", None)

        return DISABLED is not None and DISABLED.lower() in TRUISMS

    def check_for_evil(self):
        """Check to see if any non filesystem directories have
        any items.
        """
        stool = getToolByName(self.context, 'portal_skins')
        skin_folders = stool.objectIds()
        # loop through all the skins dirs
        for folder in skin_folders:
            folder = stool[folder]
            # only return true if it's not a fs dir and has something in it
            zope_folder = folder.meta_type != 'Filesystem Directory View'
            if zope_folder and folder.objectIds():
                return True
        return False
