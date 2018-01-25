from __future__ import unicode_literals
import youtube_dl
import time

youtube_watch_url = 'https://www.youtube.com/watch?v='
fast_ai_video_id_array = ['IPBSB1HLNLo',
                          'JNxcznsrRb8',
                          '9C06ZPF8Uuc',
                          'gbceqO8PpBg',
                          'J99NV9Cr75I',
                          'sHcLkfRrgoQ',
                          'H3g26EVADgY']

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


if __name__=='__main__':
    ydl_opts = {
        'skip_download': True,
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
        'writeautomaticsub': True,
    }

    for video_url in [(youtube_watch_url + id_str) for id_str in fast_ai_video_id_array]:
        print(video_url)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        time.sleep(30)