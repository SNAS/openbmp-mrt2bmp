OpenBMP MRT2BMP
===============
This reads MRT files of a router and sends natively in BMP format to a remote collector continuously.

### MRT Directory Structure

    Root/base directory
        |
        |---- DIR: <router name>                            # e.g. "route-views2.oregon-ix.net"
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
                     
- Compressed MRT files in **.gzip** and **.bz2** formats are supported.               
                
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

### Running:

1-) Running with provided MRT files.
------------------------------------
If you will provide mrt2bmp with your MRT files, you must change config file.

If you install the python code, then you should be able to run from a terminal

    openbmp-mrt2bmp -c <configuration file> -r <router name>
    
If you are running from within the **git** directory, you can run it as follows:

    PYTHONPATH=./src/site-packages python src/bin/openbmp-mrt2bmp -c src/etc/openbmp-mrt2bmp.yml -r <router name>

2-) Running with MRT files from routeviews.org
----------------------------------------------



#### Usage
```
Usage: src/bin/openbmp-mrt2bmp [OPTIONS]

OPTIONS:
  -h, --help                  Print this help menu
  -c, --config                Config filename (default is sys.prefix/etc/openbmp-forwarder.yml)
  -r, --router                Router name
```

#### Configuration
Configuration is in YAML format via the **openbmp-mrt2bmp.yml** file.  See the file for details.
