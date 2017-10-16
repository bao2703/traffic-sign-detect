# traffic sign detect

```
opencv_createsamples -img dataset/left.png -bg dataset/negatives/negatives.txt -info samples/annotations.lst -maxxangle 0.1 -maxyangle 0.1 -maxzangle 0.1 -w 24 -h 24 -num 1115
```