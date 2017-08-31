********************************************
Setup: Web Application
********************************************

*RHEAS-Viewer*


Prerequisites
--------------

-  Tethys Platform 2.0 (CKAN, PostgresQL, GeoServer): See:
   http://docs.tethysplatform.org
-  RHEAS Database Instance: See:
   http://rheas.readthedocs.io/en/latest/
-  Psycopg2 (Python package).
-  Requests (Python package).
-  Geoserver needs CORS enabled.


Install Psycopg2
~~~~~~~~~~~~~~~~~~

Note: Before installing Psycopg2 into your python site-packages, activate
your Tethys conda environment using the alias `t`:

::

    $ t

::

    (tethys)$ conda install -c conda-forge psycopg2


Install Requests
~~~~~~~~~~~~~~~~~~

Note: Before installing Requests into your python site-packages, activate
your Tethys conda environment using the alias `t`:

::

    $ t

::

    (tethys)$ conda install -c conda-forge requests


Installation
--------------

Installation for App Development
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


**Step 1. Clone the app into a directory of your choice.**

::

    $ t
    (tethys)$ git clone https://github.com/SERVIR/RHEAS-Viewer.git

**Step 2. Change the config.py file**

::

    (tethys)$ cd RHEAS-Viewer/tethysapp/rheas_viewer
    (tethys)$ sudo vi config.py

.. note::

    You can use any editor of your choice. Here's a link to a vim sheet: https://vim.rtorr.com/. For a detailed explanation of the parameters in config.py see :doc:`dbconfig`

**Step 3. Customize the schemas listed within the app**

This app is currently customized to work for the Eastern and Southern Africa RHEAS instance. You will need to make a few customizations to make it work for your instance. See :doc:`../customization` 

**Step 4. Install the app by returning to the main directory**

::

    (tethys)$ cd RHEAS-Viewer
    (tethys)$ python setup.py develop


**Step 5. Start the Tethys Server**

::

    (tethys)$ tms

You should now have the RHEAS Viewer running on a development server on your machine. Tethys Platform provides a web called the Tethys Portal. You can access the app through the Tethys portal by opening http://localhost:8000/ (or if you provided custom host and port options to the install script then it will be <HOST>:<PORT>) in a new tab in your web browser.

Installation for Production
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Installing apps in a Tethys Platform configured for production can be challenging. Most of the difficulties arise, because Tethys is served by Nginx in production and all the files need to be owned by the Nginx user. The following instructions will allow you to deploy the RHEAS Viewer on your own Tethys production server. You can find the Tethys Production installation instructions `here. <http://docs.tethysplatform.org/en/stable/installation/production.html>`_

**Step 1. Change the Ownership of Files to the Current User**

During the production installation any Tethys related files were change to be owned by the Nginx user. To make any changes on the server it is easiest to change the ownership back to the current user. This is easily done with an alias that was created in the tethys environment during the production installation process::


    $ t
    (tethys)$ tethys_user_own

**Step 2. Download App Source Code from GitHub**

::

    $ cd $TETHYS_HOME/apps/
    $ sudo git clone https://github.com/SERVIR/RHEAS-Viewer.git

.. tip::

    Substitute $TETHYS_HOME with the path to the tethys main directory.

**Step 3. Change the config.py file**

For a detailed explanation of the parameters in config.py see :doc:`dbconfig`

::

    (tethys)$ cd $TETHYS_HOME/apps/RHEAS-Viewer/tethysapp/rheas_viewer
    (tethys)$ sudo vi config.py

**Step 4. Customize the schemas listed within the app**

This app is currently customized to work for the Eastern and Southern Africa RHEAS instance. You will need to make a few customizations to make it work for your instance. See :doc:`../customization` 

**Step 5. Install the App**

Return to the main directory of the app. Then, execute the setup script (:file:`setup.py`) with the ``install`` command to make Python aware of the app and install any of its dependencies::

    (tethys)$ cd $TETHYS_HOME/apps/RHEAS-Viewer
    (tethys)$ python setup.py install

**Step 6. Collect Static Files and Workspaces**

The static files and files in app workspaces are hosted by Nginx, which necessitates collecting all of the static files to a single directory and all workspaces to another single directory. These directory is configured through the ``STATIC_ROOT`` and ``TETHYS_WORKSPACES_ROOT`` setting in the :file:`settings.py` file. Collect the static files and workspaces with this command::

    (tethys)$ tethys manage collectall

**Step 7. Change the Ownership of Files to the Nginx User**


The Nginx user must own any files that Nginx is serving. This includes the source files, static files, and any workspaces that your app may have. The following alias will accomplish the change in ownership that is required::


    (tethys)$ tethys_server_own


**Step 8. Restart uWSGI and Nginx**

Restart uWSGI and Nginx services to effect the changes::

    $ sudo systemctl restart tethys.uwsgi.service
    $ sudo systemctl restart nginx

.. note::

    For updating the app on production server, simply pull the app from GitHub. Once you have made a pull request (at times you may have to stash your local changes), follow steps 3 to 7.


.. warning::

    This app is configured for the RHEAS Instance setup for Eastern and Southern Africa. You will need to make certain changes in the app to make it work for your instance. For a detailed explanation of the customizations see :doc:`../customization` 


You should now have the RHEAS Viewer running on your production server. You can now access the RHEAS Viewer through the Tethys Apps Library.

