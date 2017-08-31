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

