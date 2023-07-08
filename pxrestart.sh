
#!/bin/bash
# This remounts all drives and restarts the plex docker container 
echo "Mounting Drives"
sudo /usr/bin/mount -a
echo "Restarting Plex"
sudo /usr/bin/docker restart plex
echo "Complete"
