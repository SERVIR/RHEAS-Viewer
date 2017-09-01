********************************************
Connecting to an External RHEAS database
********************************************

*Follow these instructions to open up your RHEAS database to external connections. This is necessary when the RHEAS instance is on a separate machine than the Tethys instance*


**Go to the postgres directory inside the RHEAS directory**

::

	rheas@rheas~$ cd ../RHEAS/data/postgres

**Edit the postgresql.conf file to listen to all addresses**

::

	$ sudo vi postgresql.conf

**Put * in listen_addresses, under the connection settings**

It should look similar to the following once the settings are changed

::

	listen_addresses = '*'      # what IP address(es) to listen on;
	     # comma-separated list of addresses;
	      # defaults to 'localhost'; use '*' for all
	      # (change requires restart)
	port = 5432             # (change requires restart)
	max_connections = 100           # (change requires restart)
	# Note:  Increasing max_connections costs ~400 bytes of shared memory per
	# connection slot, plus lock space (see max_locks_per_transaction).
	#superuser_reserved_connections = 3 # (change requires restart)
	#unix_socket_directories = '/tmp'   # comma-separated list of directories
	      # (change requires restart)

**Edit the pg_hba.conf file to allow your Tethys server to access the RHEAS database**

::

	$ sudo vi pg_hba.conf

**Place the ip address of the development/production server at the end of the file**

Include port 24 along with your ip address

::

	
	host    all             all             xxx.xxx.xxx.xxx/24       trust


**Restart the postgres service to apply the changes**

Enter the bin directory in the RHEAS directory. Then use pg_ctl to restart the database.


::

	$ cd ../RHEAS/bin
	$ ./pg_ctl -D ../RHEAS/data/postgres/ restart
