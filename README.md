# traffic sign detect

	opencv_createsamples -maxxangle 0.3 -maxyangle 0.3 -maxzangle 0.1 -w 20 -h 20 -info samples/info.txt -img logo.png -bg bg.txt -num 1532

	opencv_createsamples -vec samples.vec -info samples/info.txt -maxxangle 0.3 -maxyangle 0.3 -maxzangle 0.1 -w 20 -h 20 -num 1532

	opencv_traincascade -vec samples.vec -bg bg.txt -w 20 -h 20 -data cascade -numPos 1300 -numNeg 1400 -numStages 20