from tethys_sdk.base import TethysAppBase, url_map_maker


class DamInventory(TethysAppBase):
    """
    Tethys app class for Dam Inventory.
    """

    name = 'Dam Inventory'
    index = 'dam_inventory:home'
    icon = 'dam_inventory/images/icon.gif'
    package = 'dam_inventory'
    root_url = 'dam-inventory'
    color = '#006666'
    description = ''
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='dam-inventory',
                controller='dam_inventory.controllers.home'
            ),
            UrlMap(
                name='map',
                url='dam-inventory/map',
                controller='dam_inventory.controllers.map'
            ))

        return url_maps
