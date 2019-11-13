# IMU_servo_speed_control

# Prior requirements:
AngleMeterAlpha.py: This script is responsible for reading the gyroscope and accelerometer data from the MPU from their respective addresses

kalman.py: This script takes the readings from the previous file and filters the data to produce reasonable results to work with

# Main.py

The aim of this project is to control the speed of the servo motor using the data from the MPU. This is done through a PWM signal which is controlled through the the readings from the MPU. As the pitch angle increases, the PWM singal has a wider pulse. This is the case for all angles except when the roll angle has a value bigger than 45 degrees.

# Considerations

