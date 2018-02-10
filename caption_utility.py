from __future__ import unicode_literals
import youtube_dl
import time

youtube_watch_url = 'https://www.youtube.com/watch?v='
fast_ai_video_id_array = [#'IPBSB1HLNLo',
                          #'JNxcznsrRb8',
                          #'9C06ZPF8Uuc',
                          #'gbceqO8PpBg',
                          #'J99NV9Cr75I',
                          #'sHcLkfRrgoQ',
                          #'H3g26EVADgY',
                          #'cRjPVN3oo4s', # Deep Learning Part Two Lesson 8
                          #'I-P363wSv0Q',
                          #'uv0gmrXSXVg',
                          #'bZmJvmxfH6I',
                          #'jy1w0mPCHb0',
                          #'-lx2shfA-5s',
                          #'1-NYPQw5THU', # Deep Learning Part Two Lesson 14
                          #'CzdWqFTmn0Y', # Machine Learning 1
                          #'blyXCk4sgEg',
                          #'YSFG_W8JxBo',
                          #'0v93qHDqq_g',
                          #'3jl2h9hSRvc', # Machine Learning 5
                          #BFIYUvBRTpE',
                          #'O5F9vR2CNYI',
                          #'DzE0eSdy5Hk',
                          #'PGC0UxakTvM',
                          #'37sFIak42Sc', # Machine Learning 10
                          #'XJ_waZlJU8g',
                          '5_xFdhfUnvQ']

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