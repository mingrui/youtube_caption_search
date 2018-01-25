from webvtt import WebVTT
import caption_utility
import glob

def process_webvtt(webvtt_file, video_id, output_file):
    text_file = open(output_file, 'w')
    for caption in WebVTT().read(webvtt_file):
        text_file.writelines(caption.text)
        text_file.writelines('\n')
        text_file.writelines(caption.start)
        text_file.writelines('\n')
        text_file.writelines(
            caption_utility.youtube_watch_url + video_id + '#t='
            + caption.start[0:2] + 'h'
            + caption.start[3:5] + 'm'
            + caption.start[6:8] + 's')
        text_file.writelines('\n')
        text_file.writelines('\n')
    text_file.close()

if __name__=='__main__':
    for video_id in caption_utility.fast_ai_video_id_array:
        webvtt_file = glob.glob('*' + video_id + '.en.vtt')[0]
        output_file = webvtt_file.split('.')[0] + '.txt'
        process_webvtt(webvtt_file, video_id, output_file)