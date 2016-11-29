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
                                          
Installation
------------
You can either run the code within the **git** directory or you can install it in your python path. 

> If you are going to run it within the **git** directory, see running instructions.  

### Install Dependencies:
    
    sudo pip install pyyaml

### Install:

    git clone https://github.com/OpenBMP/openbmp-mrt2bmp.git
    cd openbmp-mrt2bmp
    sudo python setup.py install

Running
-------
If you install the python code, then you should be able to run from a terminal

    openbmp-mrt2bmp -c <configuration file>
    
If you are running from within the **git** directory, you can run it as follows:

    PYTHONPATH=./src/site-packages python src/bin/openbmp-mrt2bmp -c src/etc/openbmp-mrt2bmp.yml

#### Usage
```
Usage: src/bin/openbmp-mrt2bmp [OPTIONS]

OPTIONS:
  -h, --help                  Print this help menu
  -c, --config                Config filename (default is sys.prefix/etc/openbmp-forwarder.yml)
```

#### Configuration
Configuration is in YAML format via the **openbmp-mrt2bmp.yml** file.  See the file for details.
