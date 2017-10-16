# traffic sign detect

	opencv_createsamples -maxxangle 0.3 -maxyangle 0.3 -maxzangle 0.1 -w 20 -h 20 -info train/stop/samples/info.lst -img logo.png -bg bg.txt -num 1532

	opencv_createsamples -vec train/stop/samples.vec -info train/stop/samples/info.lst -maxxangle 0.3 -maxyangle 0.3 -maxzangle 0.1 -w 20 -h 20 -num 1532

	opencv_traincascade -vec train/stop/samples.vec -bg bg.txt -w 20 -h 20 -data train/stop/casade -numPos 1400 -numNeg 1500 -numStages 20 -precalcValBufSize 3000 -precalcIdxBufSize 3000 -numThreads 8