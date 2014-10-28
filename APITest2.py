# Another test for the Reascript API.
# Don't forget that this is Python 3.4.
# RPR_Main_OnCommand(actionnumber, 0)
# http://wiki.cockos.com/wiki/index.php/ReaScript_API
# Put "WORKS" at the end of a line if the lines work.
# Keyboard shortcut: capslock button

from reaper_python import *
import os, time

# Calling another script. TODO: figure out the usual file I/O from Reascript.
os.system("python writetest.py")

# The API test. WORKS.
# RPR_APITest();

# Let's try inserting a new track. WORKS.
# Shortcut: 40001.
RPR_Main_OnCommand(40001, 0)

# Let's try actually inserting a media item into the track. WORKS.
# http://wiki.cockos.com/wiki/index.php/RPR_AddMediaItemToTrack
# CURR_PROJ = proj num, 1 = your current project. You can't have 0.
# CURR_TRACK = track number, 0 = the first track; 1 = the second track, etc.
CURR_PROJ, CURR_TRACK = 1, 0
# Check to make sure track is selected
if RPR_CountSelectedTracks(CURR_PROJ) > 0:
    # Get a reference to a track. 0 = the first track.
    MediaTrack = RPR_GetTrack(CURR_PROJ, CURR_TRACK)

    # Use reference to add new, very blank media item
    # get reference if it went okay
    MediaItem = RPR_AddMediaItemToTrack(MediaTrack)
    if (MediaItem):

        # so use reference to make item long enough to see
        # this is essentially setting an attribute for the media item, which
        # is an empty media item. D_LENGTH = length of the item
        RPR_SetMediaItemInfo_Value(MediaItem, "D_LENGTH", 3.0)

# TODO: insert mp3 file into Reaper track's media item.
