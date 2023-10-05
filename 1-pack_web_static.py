# from datetime import datetime
# from fabric.api import local, env
# from os.path import isdir

# """
# Fabric script to genereate tgz archive
# execute: fab -f 1-pack_web_static.py do_pack
# """

# # Set the environment to use local host
# env.hosts = ['localhost']


# def do_pack():
#     """
#     Generate a .tgz archive from the web_static folder.

#     Returns:
#         Archive path if successful, None if there was an error.
#     """
#     # try:
#     # Create the versions folder if it doesn't exist
#     if isdir("version") is False:
#         if local("mkdir -p versions").failed is True:
#             return None
#     # Generate the archive filename based on the current date and time
#     now = datetime.now()
#     archive_name = "versions/web_static_{}.tgz".format(
#         now.strftime("%Y%m%d%H%M%S")
#     )
#     # Create the .tgz archive
#     if local(f"tar -cvzf {archive_name} web_static").failed is True:
#         return None
#     # Return the archive path
#     return archive_name
#     # except Exception as e:
#     #     return None


#!/usr/bin/python3
"""
Fabric script to genereate tgz archive
execute: fab -f 1-pack_web_static.py do_pack
"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """
    making an archive on web_static folder
    """

    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    if create is not None:
        return archive
    else:
        return None