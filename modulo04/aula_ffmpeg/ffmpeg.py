"""
https://ffmpeg.org/

Sintaxe:
ffmpeg -i 'arquivo_entrada' -i 'arquivo_legenda'
  -c:v libx264 -crf 23 -preset ultrafast -c:a aac -b:a 320k
  -c:s srt -map v:0 -map a 1:0 -ss 00:00:00 -to 00:00:10 'arquivo_saida'
"""

import os
import fnmatch
import sys

if sys.platform == 'linux':
    cmd_bin = 'ffmpeg'
else:
    cmd_bin = r'..\..\ffmpeg.exe'

codec_video = '-c:v libx264'
codec_audio = '-c:a aac'
crf = '-crf 23'  # 18 melhor qualidade e 28 pior
preset = '-preset ultrafast'
bitrate_audio = '-b:a 320k'
debug = '-ss 00:00:00 -to 00:00:10'  # executar todo video deixar debug = ''


path_source = '/home/guilhermedasilva/Videos'
path_output = '/home/guilhermedasilva/Videos/ffmpeg_py'

for root, dir, files in os.walk(path_source):
    for file in files:
        if not fnmatch.fnmatch(file, '*.mkv'):
            continue

        path = os.path.join(root, file)
        path_name, ext = os.path.splitext(path)
        path_sub = path_name + '.srt'

        if os.path.isfile(path_sub):
            input_sub = f'-i "{path_sub}"'
            map_sub = '-c:s srt -map v:0 -map a -map 1:0'
        else:
            input_sub = ''
            map_sub = ''

        name = os.path.splitext(file)[0]
        output = f'{path_output}/{name}_copy{ext}'

        cmd = f'{cmd_bin} -i "{path}" {input_sub} ' \
              f'{codec_video} {crf} {preset} {codec_audio} ' \
              f'{bitrate_audio} {debug} {map_sub} {output}'

        # print(cmd)
        os.system(cmd)
