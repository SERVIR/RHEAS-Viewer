********************************************
Setup: Web Application
********************************************

*tethysapp-rheas\_viewer*


Prerequisites:
--------------

-  Tethys Platform 2.0 (CKAN, PostgresQL, GeoServer): See:
   http://docs.tethysplatform.org
-  Psycopg2 (Python package).
-  Requests (Python package)
-  Geoserver needs CORS enabled.

Install Psycopg2:
~~~~~~~~~~~~~~~~~~

Note: Before installing Psycopg2 into your python site-packages, activate
your Tethys conda environment using the alias `t`:

::

    rheas@rheas:~$ t

::

    (tethys) rheas@rheas:~$ conda install -c conda-forge psycopg2


Install Requests:
~~~~~~~~~~~~~~~~~~

Note: Before installing Requests into your python site-packages, activate
your Tethys conda environment using the alias `t`:

::

    rheas@rheas:~$ t

::

    (tethys) rheas@rheas:~$ conda install -c conda-forge requests


Installation:
-------------

Installation for App Development:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Clone the app into a directory of your choice. Then do the following:

::

    $ t
    $ git clone https://github.com/SERVIR/RHEAS-Viewer.git
    $ cd tethysapp-rheas_viewer
    $ python setup.py develop
    $ tethys syncstores rheas_viewer

Change the parameters in the config.py file: See:
- :doc:`dbconfig`

Create/Set the Spatial Dataset Service



