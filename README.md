# traffic sign detect

Put positive images in the ./positives folder and create a list of them:
```
find ./positives -iname "*.jpg" > positives.txt
```

Put negative images in the ./negatives folder and create a list of them:
```
find ./negatives -iname "*.jpg" > negatives.txt
```


```
opencv_createsamples -img dataset/left.png -bg dataset/negatives.txt -info samples/annotations.lst -maxxangle 0.1 -maxyangle 0.1 -maxzangle 0.1 -w 20 -h 20 -num 1115
```