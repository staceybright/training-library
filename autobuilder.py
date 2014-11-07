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

import BaseHTTPServer
import SimpleHTTPServer

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
        path = posixpath.normpath(urllib.unquote(path))
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

def build_docs():
    proc = subprocess.Popen(['make', 'html'], stdout=subprocess.PIPE,
                            bufsize=1, cwd=PROJECT_DIR)
    for line in iter(proc.stdout.readline, ''):
        print line,
    proc.stdout.close()
    proc.wait()

class SphinxRebuildHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        build_docs()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = os.path.join(PROJECT_DIR, 'source')
    # Serve static files
    server = BaseHTTPServer.HTTPServer(BIND_TO, RequestHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()

    # Watch for filesystem events and rebuild docs as necessary
    event_handler = LoggingEventHandler()
    rebuild_handler = SphinxRebuildHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.schedule(rebuild_handler, path, recursive=True)
    observer.start()
    
    # Do an initial build, and open a browser window
    build_docs()
    url = "http://{}:{}/".format(*BIND_TO)
    import webbrowser
    webbrowser.open(url)
    print "*"*72
    print "\tNow serving the docs preview at ", url
    print "*"*72
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()