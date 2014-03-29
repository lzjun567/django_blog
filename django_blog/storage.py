#! encoding=utf-8
from django.core.files.storage import Storage

import qiniu.conf
import os
import errno
import itertools
from datetime import datetime
from datetime import datetime

from django.core.files.storage import FileSystemStorage, get_storage_class
from django.conf import settings
from django.core.exceptions import SuspiciousFileOperation
from django.core.files import locks, File
from django.core.files.move import file_move_safe
from django.utils.encoding import force_text, filepath_to_uri
from django.utils.functional import LazyObject
from django.utils.module_loading import import_by_path
from django.utils.six.moves.urllib.parse import urljoin
from django.utils.text import get_valid_filename
from django.utils._os import safe_join, abspathu

qiniu.conf.ACCESS_KEY="5cBxinktzyscACMOJ_12oZt5HL"

qiniu.conf.SECRET_KEY="UEkKWa02jAViPijy0xRQULapet"

import qiniu.rs

policy = qiniu.rs.PutPolicy('foofish')
uptoken = policy.token()

class PutExtra(object):
    params = {}
    mime_type = 'application/octet-stream'
    crc32 = ""
    check_crc = 0

import qiniu.io
localfile = "%s" % __file__



class QiniuStorage(Storage):
    """
    Standard file system storage for files handled by django-compressor.

    The defaults for ``location`` and ``base_url`` are ``COMPRESS_ROOT`` and
    ``COMPRESS_URL``.

    """


    def _open(self, name, mode='rb'):
        import urllib2
        return  urllib2.urlopen('http://foofish.qiniu.com/'+name)
   
    def url(self, name):
        return name
