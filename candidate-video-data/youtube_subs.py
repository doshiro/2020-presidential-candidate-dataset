from youtube_transcript_api import YouTubeTranscriptApi

def flattenTranscript(transcript):
    text = ''
    i = 0
    for obj in transcript:
        text += obj['text'] + " "
        i += 1
        if (i % 12 == 0):
           text += "\n"
    return text

def filterPete(pete):
    pete_split = pete.split()
    filtered = []
    start = False
    i = 0
    for word in pete_split:
        if (word == 'BUTTIGIEG:'):
            start = True
            continue
        if (start):
            if (word != 'PETE:' and word != 'AUDIENCE:' and word != '[applause]'):
                filtered.append(word)
                i += 1
                if (i % 70 == 0):
                    filtered.append('\n')
    return ' '.join(filtered)

def yt_link(vid_id):
    return 'https://www.youtube.com/watch?v=' + vid_id

#pete_file = open("pete_vids.txt", 'a+')
#pete_file.write(filterPete(flattenTranscript(YouTubeTranscriptApi.get_transcript('UFEqpwADCCs'))))
#pete_file.close()

# make file that just has the video links / candidate
# open each as a file
# flatten
# save

def make_files(vids, filename):
    f = open(filename + ".txt", "w+", encoding='utf-8')
    g = open(filename + "_links.txt", 'w+')
    for vid in vids:
        f.write(flattenTranscript(YouTubeTranscriptApi.get_transcript(vid)) + '\n')
        g.write(yt_link(vid) + '\n')
    f.close()
    g.close()

# list of videos / candidate
bennet_vids = ['LVdR-DKVJas', 'LVdR-DKVJas', 'Vyj5wJsMjvI', 'k2gFtk-TtoI', 'DSah2IGqZVw']
#make_files(bennet_vids, "bennet_vids")
biden_vids = ['Ku7uZ0Gok2g', 'U9E6GTOYlzI', 'Eo8QyK86gDM']
#make_files(biden_vids, "biden_vids")
booker_vids = ['amFehKjjteo', 'zhePX3n6CH0', 'AKHqjXIzdJA', 'mfkRcqbnZuc', 'G46MrmDIpH8']
#make_files(booker_vids, "booker_vids")
buttigieg_vids = ['j1_E2qOW3JQ', 'DDt4pCU9YSU', 'jit7J_vRHeI', 'qtAHTlogN-4', 'pE-r_4x9DFQ', 'VOak0ZMxbDM', '5tsSdf5B6wY', '-lMLLr9z0wg']
#make_files(buttigieg_vids, "buttigieg_vids")
castro_vids = ['O8xw1eoPTJ8', 'L6YUeBMTojI', 'Irva1VcgSr4', 'GSvEOEB7UW0', 'rCy4WoTrMmc', '1Gbwz7pygE4', 'mND9Px6UhD0']
#make_files(castro_vids, "castro_vids")
delaney_vids = ['DCCzeFu-7Wg', 'P4TqwKsbxrA', '-h-TWbpQSPI', 'PHLTp79hiyc', '6mj2Rxn6xiM']
#make_files(delaney_vids, "delaney_vids")
harris_vids = ['m4ecapNBaXU', 'MlYjv-otHKA', 'BdjXZq7HqdE', 'S7j1hYXD0uk', 'rx_q82wAzVs', 'jVyAXa-2rGA']
#make_files(harris_vids, "harris_vids")
klobuchar_vids = ['bX8rwqsdOCA', 'trOjFCisjfU', 'e_sELx4frj8', 'i-U9AgTVdPI', '3wnpLd4Ruus']
#make_files(klobuchar_vids, "klobuchar_vids")
sanders_vids = ['3ecPxjX-IrM', 's7DRwz0cAt0', 'qEaE1l3-9Xc', 'rBs1Kb8aroA', 'x3C8F9yUB2Q']
#make_files(sanders_vids, "sanders_vids")
trump_vids = ['YvRmQz525PA', 'sC0J1PGauqY', 'a-mfhjaPvsM', 'pMgjwBgCZIw', 'amz9yEk-3WU', '55-FciP-PTA']
#make_files(trump_vids, "trump_vids")
warren_vids = ['z17U8Gxvu8o', 'XSaHEfPBSrQ', 'oGoBDh1O5ng', 'ckrQaXwVUX8', 'QJ0rDnoi8A4']
#make_files(warren_vids, "warren_vids")
yang_vids = ['R9OBK3ss5W4', 'ydAf17x32Vg', 'qkH0xGUgR0c', 'i6B11k4H8z0', 'GhArPPmHjCs']
make_files(yang_vids, "yang_vids")