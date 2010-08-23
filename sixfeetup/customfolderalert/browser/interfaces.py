from zope.interface import Interface

class IAlertView(Interface):
    """View class for alerts methods"""

    def isAlertDisabled():
        """Is the custom folder alert disabled?"""

