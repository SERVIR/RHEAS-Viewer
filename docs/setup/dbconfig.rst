********************************************
Setup: Configuration File
********************************************

*This app requires you to have a working instance of the RHEAS database
completed separately. See:*
http://rheas.readthedocs.io/en/latest/


Connection Settings:
---------------------
Enter the connection parameters to the RHEAS database in the connection json dictionary. The following is a sample do not copy the parameters verbatim.

::

   connection = {
	      'host': 'localhost',
              'user': 'rheas',
              'password': 'pass',
              'dbname': 'rheas'
		}

-  'host': The ip address of the database
-  'user': The username for the rheas database
-  'password': The password for the rheas database
-  'dbname': The name for the rheas database

GeoServer Settings:
---------------------
Enter the GeoServer parameters for the Tethys GeoServer instance in the geoserver json dictionary. The following is a sample do not copy the parameters verbatim.

::

    geoserver = {
     'rest_url':'http://tethys.servirglobal.net:8181/geoserver/rest',
     'wms_url':'http://tethys.servirglobal.net:8181/geoserver/wms',
     'wfs_url':'http://tethys.servirglobal.net:8181/geoserver/wfs',
     'user':'admin',
     'password':'pass',
     'workspace':'rheas'
		}

- 'rest_url': The REST URL to the geoserver instance
- 'wms_url': The WMS URL to the geoserver instance
- 'wfs_url':The WFS URL to the geoserver instance
- 'user': The username for the geoserver instance
- 'password': The password for the geoserver instance
- 'workspace': The workspace where the WMS layers will be stored
