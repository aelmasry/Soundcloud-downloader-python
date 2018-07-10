#!/usr/bin/env python
# encoding: utf-8
##############################################
## Sound cloud playlist downloader			##
## Ali AbdelHafez <ali.elmasery@gmail.com>	##
## https://github.com/aelmasry				##
## python run.php							##
##############################################
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os, os.path, soundcloud, wget

# client id from registerd app YOU HAVE TO GET YOUR OWN FROM SOUNDCLOUD
CLIENT_ID ="bfb9a84d6ad2caaadd49e6c3e67ab935"
# add playlist url
PLAYLIST_URL = raw_input("Please enter Soundcloud playlist URL ")

def createClient(client_id):
	# create client instance
	client = soundcloud.Client(client_id="bfb9a84d6ad2caaadd49e6c3e67ab935")
	return client

def getPlaylist(client, playlist_url):
	# get playlist
	playlist = client.get('/resolve', url=playlist_url)
	return playlist

def getTracks(playlist):
	# get tracks which is a list of dictionaries each one containing track info
	if playlist.kind == 'playlist' :
		return playlist.tracks
	else :
		return playlist	
	
	# return tracks


def downloadTrack(tracks):
	counter = 0
	if tracks.kind == 'playlist' :
		print "Playlist has %d tracks" % len(tracks)
		for track in tracks:
			# print(track)
			# exit()
			if track['streamable'] :
				# track_title = track['title'].encode("utf-8") + '.mp3'
				track_title = track['permalink']+ '.mp3'
				if os.path.exists(track_title) == False:
					dl_url = str(track['uri'])  + '/stream?client_id=' + CLIENT_ID
					# print(dl_url)
					# exit()
					print "Currently Downloading " + track_title
					wget.download(dl_url, out=os.getcwd() +'/' + track_title)
					print "\nSuccess"
				counter += 1
			# else:
			# 	print "No files to Download (probably not allowed)"
			# # remove break to download the whole playlist
			# break
		print "\n\n Successfully downloaded %d tracks" % counter
	else :
		if tracks.streamable :
			# track_title = track['title'].encode("utf-8") + '.mp3'
			track_title = tracks.permalink+ '.mp3'
			if os.path.exists(track_title) == False:
				dl_url = str(tracks.uri)  + '/stream?client_id=' + CLIENT_ID
				# print(dl_url)
				# exit()
				print "Currently Downloading " + track_title
				wget.download(dl_url, out=os.getcwd() +'/' + track_title)
				print "\nSuccess"
			
		


def printTracksInfo(tracks):
	print "Playlist has %d tracks and they are: \n\n" % len(tracks)
	for track in tracks:
		print "Id: %s" % track['id']
		print "title: %s " % track['title']
		print "duration: %s " % track['duration']
		print "URI: %s " % track['uri']
		print "---------------------------------------------------"

# print info about tracks in the list
# printTracksInfo(getTracks(getPlaylist(createClient(CLIENT_ID), PLAYLIST_URL)))

# download tracks
downloadTrack(getTracks(getPlaylist(createClient(CLIENT_ID), PLAYLIST_URL)))