# LiDar_Project
### By: James Brophy (Jim) & Kaleb Nails
This started as a personal project in 2023, that I (Kaleb) took a year long haitus on because of issues I had with an encoder. Then my friend, James (Jim) Brophy, wanted to do it as his Mechanical Engineering Instrumentation Project. So we worked on it together.

## General Details:
We ran the lidar using a raspberry pi 4, and then used an arduino as a middleman for the encoder. I did this previously on my own with an incremental encoder but found accuracy issues, so I wanted to bumb it up to an absolute encoder. The process can be started using the command below:

```python3 Main.py```

Below is an image of the sensors suite we put together. 
![image](https://github.com/KalebNails/LiDar_Project/assets/102830532/2632550e-1d67-49bb-8fd0-541499f696dc)

### Project Origins:
This started as a personal project to learn about Lidar and encoders. The original plan was to have an encoder with a mirror attached to it, and a lidar directly under it pointing up as seen in the images below. 
![image](https://github.com/KalebNails/LiDar_Project/assets/102830532/2aba7f3b-47d7-47e6-bd68-f936eacfff19)  ![image](https://github.com/KalebNails/LiDar_Project/assets/102830532/98db289d-f6c5-4b41-bd92-847847df9202)

I started by just setting up the incremental encoder using an hbridge, and below is a fun ossiliscope image that I preformed to show how the encoder works, if you want to see a whole GIF of the previous set up here is the link: Set up here is the link: [Incremental Encoders GIF](https://www.linkedin.com/posts/kaleb-nails_incremental-encoders-are-pretty-cool-i-did-activity-7112027969715400704-XGwe?utm_source=share&utm_medium=member_desktop)

![image](https://github.com/KalebNails/LiDar_Project/assets/102830532/a255080e-63fc-451f-b532-fb29e9b1de1b)

Once I had the encoder working, I set up the TF luna. Orignially I had the TF luna running on a raspberry pi that was connected to a desktop through eithernet and an arduino connected to the same desktop through serial. The I used UDP to transfer all the data in realtime to the computer tower. The issue I ran into was that the incremental encoder was not accurate enough and I would end up getting drift in my values. After I hit this wall, I found an absolute encoder, but summer was rapidly approaching and so were finals, so this project got put away.

## Results 
Below are some of the results we collected from our data collection, throughout the campus:
### Hallway ###
![image](https://github.com/KalebNails/LiDar_Project/assets/102830532/946880a8-3cf0-4811-9501-096f3d901716) 

### Center Junction ###
![image](https://github.com/KalebNails/LiDar_Project/assets/102830532/4bec32ac-76f4-4e4b-9657-694d9ab316b0)

### Classroom ###
![image](https://github.com/KalebNails/LiDar_Project/assets/102830532/6d26e2b1-3f2a-4678-951f-09996ace5a7c)

### Eleveator ###
![image](https://github.com/KalebNails/LiDar_Project/assets/102830532/735c5bc5-b500-43d2-a137-5db36fbdb0aa)


## 📝 File Structure 
```text
📦LiDar_Project
 ┣ 📂experimental
 ┃ ┣ 📄ArduinoReader.py
 ┃ ┗ 📄combined.py
 ┣ 📄AMT203.py
 ┣ 📄Main.py
 ┣ 📄README.md
 ┣ 📄TFLunaRangeOutput.py
 ┣ 📄anlge_test.py
 ┗ 📄plotter.py
```


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


