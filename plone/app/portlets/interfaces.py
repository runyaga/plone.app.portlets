from plone.portlets.interfaces import IPortletManager, IPlacelessPortletManager, IPortletRenderer

class IColumn(IPortletManager):
    """Common base class for left and right columns.
    
    Register a portlet for IColumn if it is applicable to regular columns
    but not to the dashboard.
    """

class ILeftColumn(IColumn):
    """The left column.
    
    Normally, you will register portlets for IColumn instead.
    """

class IRightColumn(IColumn):
    """The right column
    
    Normally, you will register portlets for IColumn instead.
    """
    
class IDashboard(IPlacelessPortletManager):
    """Common base class for dashboard columns
    
    Register a portlet for IDashboard if it is applicable to the dashboard
    only.
    """
    
class IDeferredPortletRenderer(IPortletRenderer):
    """provide refresh and dynamic loading functionality"""

    def deferred_update():
        """refresh portlet data on KSS events (and only then)

        this is similar to update() but it is only called from a KSS action and
        thus can be used to do long computing/retrieval only on loading the portlet
        via KSS but not in the initial page load.

        """

    def render_full():
        """method for rendering the full version of the portlet

        this is usually the one called via KSS events
        """

    def render_preload():
        """method for rendering the portlet in preloading state

        this usually just contains a class to which an KSS event is bound
        """

    def initialized():
        """return whether the portlet is initialized or not

        depending on this the render() method chooses whether to render the preload
        or full version (if initialized==True).

        """
