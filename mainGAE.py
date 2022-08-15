import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'gae/lib'))

# Monkeypatch some youtube_dl functions that use features not available in GAE
from yt_dlp import YoutubeDL
with yt_dlp.YoutubeDL() as ydl:
# Modifying youtube_dl.utils.get_cachedir doesn't work
ydl.extractor.youtube.get_cachedir = lambda *args, **kargs: None


from youtube_dl_server.app import app  # noqa: app is used by GAE
