OpenBMP Route Views Syncronizer
===============================
This downloads MRT files of routers from http://routeviews.org.

### MRT Directory Structure

    Root/base directory
        |
        |---- DIR: <router name>
            |
            |---- DIR: <subdirectory name>                  # e.g. "2016.11"
                |
                |---- DIR: RIBS
                |    |
                |    |---- FILE: rib.20161128.0800.bz2      # Rib file
                |
                |---- DIR: UPDATES
                     |
                     |---- FILE: updates.20161128.0800.bz2  # Update file
                     |---- FILE: updates.20161128.0815.bz2  # Update file
                     |---- FILE: updates.20161128.0830.bz2  # Update file
                     |---- FILE: updates.20161128.0845.bz2  # Update file
 
Running
-------
If you install the python code, then you should be able to run from a terminal

    openbmp-route_views_sync -c <configuration file>
    
If you are running from within the **git** directory, you can run it as follows:

    PYTHONPATH=./src/site-packages python src/bin/route_views_sync/openbmp-route_views_sync -c src/bin/route_views_sync/openbmp-route_views_sync.yml

#### Usage
```
Usage: src/bin/route_views_sync/openbmp-route_views_sync [OPTIONS]

OPTIONS:
  -h, --help                  Print this help menu
  -c, --config                Config filename (default is sys.prefix/bin/route_views_sync/openbmp-forwarder.yml)
```

#### Configuration
Configuration is in YAML format via the **openbmp-route_views_sync.yml** file.  See the file for details.
