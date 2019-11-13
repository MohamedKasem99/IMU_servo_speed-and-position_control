# IMU_servo_speed_control
In this mini-project we implemented a DC motor bi-directional speed control based on MPU 6050 readings. The continuous servo motor will speed up as the pitch angle increases and vice versa while the roll angle is below 45 degree. Here's a video of the projcet in motion: 

https://drive.google.com/file/d/1e2IDNRZsvWtSsizygtWvzXyni6FBNiSW/view?usp=sharing

# Prior requirements:
AngleMeterAlpha.py: This script is responsible for reading the gyroscope and accelerometer data from the MPU from their respective addresses. Basically it includes a class with member functions responsible for initializing and interfacing the I2C bus and obtaining the values stored in the MPU 6050 registers which contain the values for orientation and acceleration in 3d space. 

kalman.py: This script takes the readings from the previous file and filters the data to produce reasonable results to work with

# Main.py

The aim of this project is to control the speed of the servo motor using the data from the MPU. This is done through a PWM signal which is controlled through the the readings from the MPU. As the pitch angle increases, the PWM singal has a wider pulse up to a certain adjustable point at which the servo starts going in the opposite direction. This is the case for all angles except when the roll angle has a value bigger than 45 degrees. 

# Hardware: 
- Raspberry pi 3 model B v1.2
- MPU 6050. Datasheet: 
- position control: 
S-91BB servo. Datasheet:

- speed control: 
FS5103R continuous servo. Datasheet: https://media.digikey.com/pdf/Data%20Sheets/Adafruit%20PDFs/154_Web.pdf


