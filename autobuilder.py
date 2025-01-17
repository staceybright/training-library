#!/usr/bin/env python
from __future__ import print_function
"""
riatraining autobuilder
========================

This helper script does two things:

 1. Watches the project source directory for changes, rebuilding the docs
    whenever you make changes
 2. Serves the html docs at http://127.0.0.1:8000/ so you can preview your changes

"""
import sys
import time
import logging
import threading
import subprocess
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler
import os.path
import posixpath
import urllib
import shlex

try:
    import BaseHTTPServer
except ImportError:
    import http.server as BaseHTTPServer

try:
    import SimpleHTTPServer
except ImportError:
    import http.server as SimpleHTTPServer

try:
    from urllib import unquote
except ImportError:
    from urllib.parse import unquote

BIND_TO = ('127.0.0.1', 8000)

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

class RequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    document_root = os.path.join(PROJECT_DIR, 'build', 'html')

    def translate_path(self, path):
        # Borrowed from the Python standard library implementation of SimpleHTTPRequestHandler

        # abandon query parameters
        path = path.split('?', 1)[0]
        path = path.split('#', 1)[0]
        # Don't forget explicit trailing slash when normalizing. Issue17324
        trailing_slash = path.rstrip().endswith('/')
        path = posixpath.normpath(unquote(path))
        words = path.split('/')
        words = filter(None, words)
        path = self.document_root
        for word in words:
            drive, word = os.path.splitdrive(word)
            head, word = os.path.split(word)
            if word in (os.curdir, os.pardir):
                continue
            path = os.path.join(path, word)
        if trailing_slash:
            path += '/'
        return path

def build_docs(target='html'):
    print('Building target "{}"...'.format(target))
    cmd = shlex.split('make {}'.format(target))
    with subprocess.Popen(cmd, stdout=subprocess.PIPE) as p:
        while p.poll() is None:
            out = p.stdout.readline().decode('utf-8')
            if out == '' and p.poll() is not None:
                break
            # if out:    # uncomment to see subprocess output
            #     print(out)
    print('Build completed.')

class SphinxRebuildHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if '.pdf' not in event.src_path:
            build_docs()

class LaTeXRebuildHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if '.tex' in event.src_path:
            build_docs(target='riadocs')

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = os.path.join(PROJECT_DIR, 'source')
    latex_path = os.path.join(PROJECT_DIR, 'latexdocs')
    # Serve static files
    server = BaseHTTPServer.HTTPServer(BIND_TO, RequestHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()

    # Watch for filesystem events and rebuild docs as necessary
    event_handler = LoggingEventHandler()
    rebuild_handler = SphinxRebuildHandler()
    latex_rebuild_handler = LaTeXRebuildHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.schedule(rebuild_handler, path, recursive=True)
    observer.schedule(latex_rebuild_handler, latex_path, recursive=True)
    observer.start()

    # Do an initial build, and open a browser window
    build_docs(target='riadocs')
    url = "http://{}:{}/".format(*BIND_TO)
    import webbrowser
    webbrowser.open(url)
    print("*"*72)
    print("\tNow serving the docs preview at ", url)
    print("*"*72)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
