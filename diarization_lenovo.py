from voiceid_ilp.sr import Voiceid
from voiceid_ilp.db import GMMVoiceDB

def diarize(filename,voices):
	new_speakers = False
    ## Database address. You can have trained models here in case of voice recognition.
    db = GMMVoiceDB('.')
    v = Voiceid(db, filename)
    ## Diarization
    v.extract_speakers(new_speakers = new_speakers)
    ## Get start, end time of each segment. To get the diarization plot.

    for c in v.get_clusters():
        cluster = v.get_cluster(c)
        cluster, start, end =  cluster.print_segments()
        print cluster, start, end
