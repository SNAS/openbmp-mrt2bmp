OpenBMP MRT2BMP
===============
This consumer reads MRT files of a router and sends natively in BMP format to a remote collector continuously.

> When you exit MRT2BMP, **router** and **peers** will be shown **down**.

### MRT2BMP Structure

    Router --> MRT --> MRT2BMP --> OpenBMP Collector --> Kafka Message Bus --> MySQL Consumer

Installation
------------
You can either run the code within the **git** directory or you can install it in your python path.

> If you are going to run it within the **git** directory, see running instructions.

### Install Dependencies:

    sudo pip install pyyaml
    sudo apt-get install python-setuptools-git (for Ubuntu)

### Install:

    git clone https://github.com/OpenBMP/openbmp-mrt2bmp.git
    cd openbmp-mrt2bmp
    sudo python setup.py install

### Running:

Configure
-----------------------------------------
Default config file path is **src/etc/openbmp-mrt2bmp.yml**
> Change **collector address** and **collector port** in the config file.

1-) Running a router with your MRT files
-----------------------------------------

If you install the python code, then you should be able to run from a terminal

    nohup openbmp-mrt2bmp -c <configuration file> -r <router name> > /dev/null 2>&1 &

If you are running from within the **git** directory, you can run it as follows:

     nohup PYTHONPATH=./src/site-packages python src/bin/openbmp-mrt2bmp -c src/etc/openbmp-mrt2bmp.yml -r <router name> > /dev/null 2>&1 &

> **IMPORTANT**: Router directory structure must follow directory structure below.
You can find example router directory structure in **src/etc/example_routers**. "example_routers" directory is the example root directory in which router directories are.

> **Router Directory Structure Explaination**
> - **Root/Base directory:** Directory in which router directories are stored. Name of this directory must be the same as root/base directory name in config file.
> - **Router directory:** Directory in which router's subdirectories are stored. Name of this directory will be the router name.
> - **Subdirectory:** Subdirectories in which **RIBS** and **UPDATES** directories are stored. Name of these directories must be in format **YYYY.MM**. e.g. "2017.03"
> - **RIBS Directory:** Directory in which **RIB** files are stored. Name of this directory must be "RIBS".
<br> - File name of a **RIB** file must be in format **"rib.YYYYMMDD.HHMM"** or **"bview.YYYYMMDD.HHMM"**. e.g. **"rib.20170222.1600"**, **"bview.20170222.1600"**
> - **UPDATES Directory:** Directory in which **UPDATES** files are stored. Name of this directory must be "UPDATES".
<br> - File name of a **UPDATES** file must be in format **"updates.YYYYMMDD.HHMM"**. e.g. **"updates.20170222.1600"**

> **RIB** and **UPDATES** files can have **.gzip**, **.bz2** and **.gz** file format extensions in their file names. e.g. "rib.20170222.1600.gzip", "rib.20170222.1600.bz2", "updates.20170222.1600.gz"

### Router Directory Structure

    Root/base directory
        |
        |---- DIR: <router name>                            # e.g. "route-views2.oregon-ix.net","rrc00.ripe.net"
            |
            |---- DIR: <subdirectory name>                  # e.g. "2016.11"
                |
                |---- DIR: RIBS
                |    |
                |    |---- FILE: rib.20161128.0800.bz2      # Rib file
                     |---- FILE: bview.20170222.1600.gz      # Bview file
                |
                |---- DIR: UPDATES
                     |
                     |---- FILE: updates.20161128.0800.bz2  # Update file
                     |---- FILE: updates.20161128.0815.bz2  # Update file
                     |---- FILE: updates.20161128.0830.bz2  # Update file
                     |---- FILE: updates.20161128.0845.bz2  # Update file

- Compressed MRT files in **.gzip**, **.bz2** and **.gz** formats are supported.

2-) Running a router with MRT files from routeviews.org
-------------------------------------------------------

You can see list of routers from routeviews.org by running it as follows:

    openbmp-mrt2bmp --rv list

If you install the python code, then you should be able to run from a terminal

    nohup openbmp-mrt2bmp -c <configuration file> --rv <router name> > /dev/null 2>&1 &

#### Example Run:

    nohup openbmp-mrt2bmp -c src/etc/openbmp-mrt2bmp.yml --rv route-views2.oregon-ix.net > /dev/null 2>&1 &

If you are running from within the **git** directory, you can run it as follows:

    nohup PYTHONPATH=./src/site-packages python src/bin/openbmp-mrt2bmp -c src/etc/openbmp-mrt2bmp.yml --rv <router name> > /dev/null 2>&1 &

3-) Running a router with MRT files from ripe.net
-------------------------------------------------

You can see list of routers from ripe.net by running it as follows:

    openbmp-mrt2bmp --rp list

If you install the python code, then you should be able to run from a terminal

    nohup openbmp-mrt2bmp -c <configuration file> --rp <router name> > /dev/null 2>&1 &

#### Example Run:

    nohup openbmp-mrt2bmp -c src/etc/openbmp-mrt2bmp.yml --rp rrc00.ripe.net > /dev/null 2>&1 &

If you are running from within the **git** directory, you can run it as follows:

    nohup PYTHONPATH=./src/site-packages python src/bin/openbmp-mrt2bmp -c src/etc/openbmp-mrt2bmp.yml --rp <router name> > /dev/null 2>&1 &

#### Usage
```
Usage: ./openbmp-mrt2bmp [OPTIONS]

OPTIONS:
  -h, --help                        Print this help menu
  -c, --config                      Config filename (default is src/etc/openbmp-mrt2bmp.yml)
  -r, --router                      Router name which you want to run with your MRT files
  --rv, --routeviews                Router name which you want to run from routeviews.org
  --rv list, --routeviews list      Print name of routers from routeviews.org
  --rp, --ripe                      Router name which you want to run from ripe.net
  --rp list, --ripe list            Print name of routers from ripe.net
```

#### Configuration
Configuration is in YAML format via the **openbmp-mrt2bmp.yml** file.  See the file for details.

> ** You should provide **directory paths** that are **writable** by the consumer.

