"""Install matplotlib stylelib files.

This script installs copies of stylelib files to a target directory::

    python3 install.py ~/myproject -j aip

By default, it will install **all** styles to your matplotlib configdir,
which makes them accessible anywhere you import matplotlib. Specifying a
directory allows you to localize the files to a particular project. You
can also specify a particular journal style to limit the number of files
that are installed to the project using the ``-j`` option.

You can load the style using matplotlib::

    plt.style.use(['mphowardlab','aip'])
    plt.style.use(['./mphowardlab.mplstyle','./aip.mplstyle'])

Always load ``mphowardlab.mplstyle`` first, as the journal styles are
intended to override options in this base style.

"""
import argparse
import os
import matplotlib
import shutil
import sys

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('dest', type=str, default=None, help='Destination')
parser.add_argument('-j', dest='journal', type=str, choices=['all','acs','aip'], nargs='+', default=['all'], help='Journal styles')
args = parser.parse_args()

# create list of source files
src = os.path.dirname(os.path.realpath(__file__))
src = os.path.join(src,'stylelib')
files = []
if 'all' not in args.journal:
    for f in os.listdir(src):
        # skip any non-style files
        if 'mplstyle' not in f:
            continue
        # always use the basestyle, then add additional journal styles
        keep = (f == 'mphowardlab.mplstyle')
        for j in args.journal:
            if j in f:
                keep = True
                break
        if keep:
            files.append(f)
else:
    files = [f for f in os.listdir(src) if 'mplstyle' in f]

# configure destination
dest = args.dest
if dest is None:
    dest = matplotlib.get_configdir()
    print('matplotlib automatically detected at {}'.format(dest))
    dest = os.path.join(dest,'stylelib')

# install files
print('Installing {} to {}'.format(str(files),dest))
if not os.path.exists(dest):
    os.makedirs(dest)
for f in files:
    shutil.copyfile(os.path.join(src,f),os.path.join(dest,f))
