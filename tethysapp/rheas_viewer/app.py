from tethys_sdk.base import TethysAppBase, url_map_maker
from tethys_sdk.app_settings import PersistentStoreDatabaseSetting, PersistentStoreConnectionSetting,SpatialDatasetServiceSetting

class RheasViewer(TethysAppBase):
    """
    Tethys app class for RHEAS Viewer.
    """

    name = 'RHEAS Viewer'
    index = 'rheas_viewer:home'
    icon = 'rheas_viewer/images/logo.png'
    package = 'rheas_viewer'
    root_url = 'rheas-viewer'
    color = '#27ae60'
    description = 'View RHEAS data'
    tags = 'Hydrology'
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
                url='rheas-viewer',
                controller='rheas_viewer.controllers.home'
            ),
            UrlMap(
                name='vic',
                url='rheas-viewer/vic',
                controller='rheas_viewer.controllers.vic'
            ),
            UrlMap(
                name='variables',
                url='rheas-viewer/vic/variables',
                controller='rheas_viewer.ajax_controllers.get_vars'
            ),
            UrlMap(
                name='dates',
                url='rheas-viewer/vic/dates',
                controller='rheas_viewer.ajax_controllers.get_dates'
            ),
            UrlMap(
                name='raster',
                url='rheas-viewer/vic/raster',
                controller='rheas_viewer.ajax_controllers.get_raster'
            ),
            UrlMap(
                name='get-vic-plot',
                url='rheas-viewer/vic/get-vic-plot',
                controller='rheas_viewer.ajax_controllers.get_vic_plot'
            ),
            UrlMap(
                name='dssat',
                url='rheas-viewer/dssat',
                controller='rheas_viewer.controllers.dssat'
            ),
            UrlMap(
                name='dsensemble',
                url='rheas-viewer/dssat/get-ensemble',
                controller='rheas_viewer.ajax_controllers.get_ensemble'
            ),
            UrlMap(
                name='dsensval',
                url='rheas-viewer/dssat/get-ens-values',
                controller='rheas_viewer.ajax_controllers.get_ens_values'
            ),
            UrlMap(
                name='dsyield',
                url='rheas-viewer/dssat/get-schema-yield',
                controller='rheas_viewer.ajax_controllers.get_schema_yield'
            ),
            # UrlMap(
            #     name='get-vars',
            #     url='rheas-viewer/get-vars',
            #     controller='rheas_viewer.ajax_controllers.get_vars'
            # ),
        )

        return url_maps
        
    
    def persistent_store_settings(self):
        """
        Example persistent_store_settings method.
        """
    
        ps_settings = (
            # Connection only, no database
            PersistentStoreConnectionSetting(
                name='rheas',
                description='Connection with superuser role needed.',
                required=True
            ),
            )
            
        return ps_settings

    def spatial_dataset_service_settings(self):
        """
        Example spatial_dataset_service_settings method.
        """
        sds_settings = (
            SpatialDatasetServiceSetting(
                name='main_geoserver',
                description='spatial dataset service for app to use',
                engine=SpatialDatasetServiceSetting.GEOSERVER,
                required=True,
            ),
        )

        return sds_settings