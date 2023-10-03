This algorithm allows you to compare identical images, even if they have
minor changes (can be used to identify duplicates on the server).

Algorithm steps:

1.  Reducing the dimension to 8x8 pixels using the PIL library

> ![](./image1.jpeg){width="1.9833333333333334in"
> height="1.9767574365704288in"}![](./image2.png){width="1.9833333333333334in"
> height="1.9651367016622923in"}

2.  Converting an image to grayscale

![](./image3.png){width="2.029844706911636in"
height="2.0045767716535434in"}

3.  Binarization by average

> ![](./image4.png){width="2.0in" height="1.9794870953630797in"}

4.  Comparison of images by superimposing the resulting binarized
    matrices. The greater the discrepancy (Hamming distance), the more
    the images differ from each other.
