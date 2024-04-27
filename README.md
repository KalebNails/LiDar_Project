# LiDar_Project
### By: James Brophy (Jim) & Kaleb Nails
This started as a personal project in 2023, that I took a year long haitus on. Then my friend, James Brophy, wanted to do it as his instrumentation project. So we worked on it together.

# Files:

## Combined.py

## Aurduinoreader.py

## TF-luna distance


## References
Encoder Datasheet: https://www.cuidevices.com/product/resource/amt20.pdf

Lidar TF-Luna datasheet: https://s3-us-west-2.amazonaws.com/files.seeedstudio.com/products/101990656/res/SJ-PM-TF-Luna+A01+Product+Manual.pdf

TF-Luna Code Inspiration & tutorials: https://makersportal.com/shop/tf-luna-lidar-module

AMT 203 Code: https://github.com/HodgsonOrtho/AMT203

## TF-Luna Lidar:
This is a picture of the lidar I used, it is about $20 and has a range of 8m.

![image](https://github.com/KalebNails/LiDar_Project/assets/102830532/5be4f64d-e12d-4bdb-bc99-2ff9e22e8de1)

## AMT20 Encoder:
This is a picture of the absolute encoder I used for this project. We ran it using an arduino. 

![image](https://github.com/KalebNails/LiDar_Project/assets/102830532/cfba53ad-3e34-411f-948e-659eff0f1bb9)

## General Details:
We ran the lidar using a raspberry pi 4, and then used an arduino as a middleman for the encoder. I did this previously on my own with an incremental encoder but found accuracy issues, so I wanted to bumb it up to an absolute encoder. The process can be started using the command below:

```bash bokeh serve --show combined.py```
