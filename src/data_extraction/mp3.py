import ffmpeg

input_file = 'C:/Users/NHI360/Desktop/ml-youtube-search/src/data_extraction/audio_files/StatQuest： Random Forests Part 1 - Building, Using and Evaluating.webm'
output_file = 'C:/Users/NHI360/Desktop/ml-youtube-search/src/data_extraction/audio_files/StatQuest： Random Forests Part 1 - Building, Using and Evaluating.mp3'

audio = ffmpeg.input(input_file)
audio = ffmpeg.output(audio, output_file)
ffmpeg.run(audio, cmd=r'C:/Users/NHI360/Downloads/ffmpeg-2023-03-20-git-57afccc0ef-full_build/ffmpeg-2023-03-20-git-57afccc0ef-full_build/bin/ffmpeg')




