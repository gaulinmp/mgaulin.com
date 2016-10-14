# mgaulin.com static website generator source

Code for my personal website mgaulin.com. Theme is pared down version of Pelican's default theme `notmyidea`.


## To use:

First get it:

    git clone https://github.com/gaulinmp/mgaulin.com.git

Then you need the support files (pelican-plugins needs to live next door, or point to it in pelicanconf.py):

    git clone --recursive https://github.com/getpelican/pelican-plugins
    cd mgaulin.com
    pip install -r requirements.txt

Make your changes to the content (in /content/) or look and feel (in /theme/cv/), and build to test:

    make devserver

Or build final version:

    make clean
    make publish

To deploy, remove --dry-run to actually sync with server. Assumes you have your server (here ``mgaulin``) configured via ssh config:
    
    rsync ./output mgaulin:~/public_html/ --verbose --recursive --checksum --exclude=".*" --dry-run
