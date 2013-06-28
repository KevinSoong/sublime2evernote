#! /usr/bin/env python
#from evernote import edam
import sys
#
# Force Python to notice local-embedded Evernote API libs
#
#sys.path.append('lib')

#from evernote.edam.type.ttypes import Note as EvernoteTypeNote
#from evernote.edam.error.ttypes import EDAMUserException
#from evernote.api.client import EvernoteClient
import sublime, sublime_plugin

class SaveToEvernote(sublime_plugin.TextCommand):
  def run(self, edit):
    print "Hello World!"

title = "test from S2N"
content = "Lorem ipsum"
tags = "1, 23123,3, 4214 4242 , 24, "

'''
dev_token = "1S=s1:U=3a529:E=146e0f0c800:C=13f893f9c03:P=1cd:A=en-devtoken:V=2:H=987718ca0ff7773fee5fe6d1e73fe99f"
client = EvernoteClient(token=dev_token)
try:
    noteStore = client.get_note_store()
except EDAMUserException, e:
    print "Authentication Failed. Error: %s" % e
    sys.exit(-1)
note = EvernoteTypeNote()
note.title = title
note.content = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
note.content += '<en-note>' + content + '</en-note>'
note.tagNames = [x.strip() for x in tags.split(',') if x.strip()]
try:
    note = noteStore.createNote(note)
except Exception, e:
    print "Note Creation Failed. Error: %d" % e
'''

