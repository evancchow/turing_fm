# Another test for the Reascript API.
# Don't forget that this is Python 3.4.
# RPR_Main_OnCommand(actionnumber, 0)
# http://wiki.cockos.com/wiki/index.php/ReaScript_API
# Put "WORKS" at the end of a line if the lines work.
# Keyboard shortcut: F12
# Make sure you save the project between running the script; history messes
# some things up I think.

from reaper_python import *
import os, time

# Calling another script. 
# TODO: figure out the usual file I/O from Reascript.
# TODO: figure out how to get terminal to wait so you can see the output.
os.system("python writetest.py; ping -n 3 127.0.0.1 >nul")

# The API test. --WORKS--
# RPR_APITest();

# Set cursor to beginning of the time (time 0).
# Keep this at the beginning of your scripts to ensure things work correctly.
RPR_SetEditCurPos(0, False, False)

# Before doing stuff: open the file with the filenames.
madeon_loc = ("C:\\Users\\Evan Chow\\Desktop\\turing_fm\\scr" +
                "ipts\\APITest2_filenames.txt")
file_names = open(madeon_loc)

# Let's try inserting a new track. --WORKS--
# Shortcut: 40001.
RPR_Main_OnCommand(40001, 0)

# Let's try actually inserting a media item into the track. --WORKS--
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

# Insert mp3 file into Reaper track's media item. --WORKS--
# Also test pulling information from another file. --WORKS--
# To call other files, etc. you probably need to specify the absolute path.
# TODO: I suspect using absolute path works for calling an external script too.
# see http://wiki.cockos.com/wiki/index.php/RPR_InsertMedia
# http://forum.cockos.com/archive/index.php/t-45037.html
# Note that the actual text file "APITest2_filenames.txt" cannot have trailing
# newlines at the end (affects filename), hence the rstrip().
madeon_file = file_names.readline().rstrip()
RPR_InsertMedia(madeon_file, 0)

# Now, let's get rid of that empty media item we initially inserted. --WORKS--
# Note that you need pointers to both the track and the item to delete.
# In finding the tracks, you can think of them as a stack: if you push
# an empty track, then a nonempty track, the nonempty will be at index 0 
# and the empty will be at index 1.
initial_track = RPR_GetTrack(CURR_PROJ, CURR_TRACK)
empty_track_item = RPR_GetMediaItem(CURR_PROJ, 1)
RPR_DeleteTrackMediaItem(initial_track, empty_track_item)

# Set cursor offset vertically to where you'll insert the track.
RPR_SetEditCurPos(2, False, False)

# Let's add another track.
RPR_Main_OnCommand(40001, 0)

# Add another Madeon sample at that new cursor offset in the new track
# you just added.
# RPR_InsertMedia: again, running "0" inserts it on that new track.
madeon_file2 = file_names.readline().rstrip()
RPR_InsertMedia(madeon_file2, 0)

# TODO
# Add fade-in, fade-out for that second MP3 track. See the Cockos link
# from before, http://forum.cockos.com/archive/index.php/t-45037.html .



