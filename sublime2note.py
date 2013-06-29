#! /usr/bin/env python
import sys
#
# Force Python to notice local-embedded Evernote API libs
#
sys.path.append('./lib')
from thrift.transport.THttpClient import THttpClient
from evernote.edam.type.ttypes import Note as EvernoteTypeNote
from evernote.edam.error.ttypes import EDAMUserException
from evernote.api.client import EvernoteClient
from html import XHTML
import sublime, sublime_plugin

settings = sublime.load_settings("Sublime2Evernote.sublime-settings")

class SaveToEvernote(sublime_plugin.TextCommand):
    def __init__(self, view):
        self.view = view    
        self.window = sublime.active_window()
        self.note = {}
    def process_note(self):
        region = sublime.Region(0L, self.view.size())
        self.note["content"] = self.view.substr(region)
        def do_update(**kwargs):
            for key, value in kwargs.items():
                self.note[key] = value
            self.send()
        def update_title(title):
            def update_tags(tags):
                do_update(title=title, tags=tags)
            self.window.show_input_panel("tags:","",update_tags,None,None)
        self.window.show_input_panel("title:","",update_title,None,None) 
    def send(self):
        note = self.note
        dev_token = "S=s1:U=3a529:E=146e0f0c800:C=13f893f9c03:P=1cd:A=en-devtoken:V=2:H=987718ca0ff7773fee5fe6d1e73fe99f"
        client = EvernoteClient(token=dev_token)
        try:
            noteStore = client.get_note_store()
        except EDAMUserException, e:
            print "Authentication Failed. Error: %s" % e
        else:
            xhtml = XHTML()
            n = EvernoteTypeNote()
            n.title = note["title"]
            n.content = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
            n.content += '<en-note><pre>%s</pre></en-note>' % xhtml.p(note["content"].encode('utf-8'))
            n.tagNames = [x.strip() for x in note["tags"].split(',') if x.strip()]
            try:
                n = noteStore.createNote(n)
            except Exception, e:
                print "Note Creation Failed. Error: %s" % e
    def run(self, edit):
        self.process_note()