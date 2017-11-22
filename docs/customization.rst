********************************************
Customization
********************************************

*The current app is customized to work for the RHEAS database setup for Eastern and Southern Africa. The following instructions will help you customize the app for your case*


VIC Default Schemas
---------------------

The file :file:`model.py` has a global variable called default_schemas. This variable contains the list of schemas that do not appear on the VIC interface. Place the schemas that you would like to ignore in VIC interface. The following is an example of the default_schemas list as seen in :file:`model.py`. This variable is declared at the top of the page.

::

	default_schemas = ['basin','crops','dssat','ken_test','information_schema','lai','precip','public','soilmoist','test','test_ke','test_tza','tmax','tmin','topology','vic','wind','pg_toast','pg_temp_1','pg_toast_temp_1','pg_catalog','ken_vic','tza_vic','eth_vic','tza_nrt']

The following is the path to the :file:`model.py`

.. parsed-literal::

       ../RHEAS-Viewer/tethysapp/rheas_viewer/model.py

DSSAT Default Schemas
---------------------

The file :file:`dssat.js` has a global dictionary called current_schemas. This is a collection of schemas that will appear on the DSSAT interface. Place the schemas that you would like to see in the DSSAT interface with their corresponding year. The following is an example of the current_schemas dictionary as seen in :file:`dssat.js`. This variable is declared through the init_vars function.

::
	
	 current_schemas = {"2010":["ken_2010_mam_high","ken_2010_mam_med"],"2011":["ken_2011_mam_high","ken_2011_mam_med"],"2012":["ken_2012_mam_high"],
            "2013":["ken_2013_mam_high","ken_2013_mam_med"],"2014":["ken_2014_mam_high","ken_2014_mam_med"],"2015":["ken_2015_mam_low"],"2016":["ken_2016_mam_high","ken_2016_mam_med"]};

The following is the path to the :file:`dssat.js`

.. parsed-literal::

       ../RHEAS-Viewer/tethysapp/rheas_viewer/public/js/dssat.js

Uploading DSSAT Agareas Shapefile to GeoServer
-------------------------------------------------

The file :file:`dssat.js` is currently configured to work for the RHEAS instance setup for Eastern and Southern Africa. It is hard coded to show the agareas in Kenya as seen below. 

.. parsed-literal::

        vectorSource = new ol.source.Vector({
            format: new ol.format.GeoJSON(),
            url: function(extent) {
                return wfs_url+'?service=WFS&' +
                    'version=1.1.0&request=GetFeature&typename='+wfs_workspace+':agareas&' +
                    'outputFormat=application/json&srsname=EPSG:3857&' +
                    'bbox=' + extent.join(',') + ',EPSG:3857';
            },
            strategy: ol.loadingstrategy.bbox,
            wrapX: false
        });

You will need to upload the agareas shapefile to your GeoServer to get the above code working. The following instructions will help you get started on uploading a shapefile to GeoServer.

First, export the shapefile from an agareas table in a schema of your choice.You can do it programatically using SQL or through QGIS or ArcGIS. Then zip the folder with the shapefile contents.

Enter the directory with the zipped file and execute the following command

.. parsed-literal::

        curl -u admin:geoserver -v -XPUT -H "Content-type: application/zip" --data-binary @shapefile.zip http://127.0.0.1:8181/geoserver/rest/workspaces/rheas/datastores/agareas/file.shp


.. warning::

    The above code is just a sample, please do not copy it verbatim. Replace `admin` with the admin name for your geoserver. Replace `geoserver` with the password to your geoserver instance. Replace `shapefile.zip` to the name of your zip file. Replace `rheas` with the name of your GeoServer workspace. Finally after datastores you can replace `agareas` with a name of your choice, but be sure that it is changed in the vectorSource code block. Note: file.shp at the end of the url needs to remain unchanged.



