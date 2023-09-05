"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor, Keyboard

# create the Robot instance.
robot = Robot()
MAX_SPEED = 1.0
# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())
keyboard=Keyboard()
keyboard.enable(timestep)
# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
left_motor = robot.getDevice('left_motor')
right_motor = robot.getDevice('right_motor')

left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

left_motor.setVelocity(MAX_SPEED)
right_motor.setVelocity(MAX_SPEED)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    key=keyboard.getKey()
    print(key)
    if (key == 68):
        left_motor.setVelocity(MAX_SPEED)
        right_motor.setVelocity(-MAX_SPEED)       
    elif (key == 65):
        left_motor.setVelocity(-MAX_SPEED)
        right_motor.setVelocity(MAX_SPEED)  
    elif (key == 87):
        left_motor.setVelocity(MAX_SPEED)
        right_motor.setVelocity(MAX_SPEED)   
    elif (key == 83):
        left_motor.setVelocity(-MAX_SPEED)
        right_motor.setVelocity(-MAX_SPEED)         
    elif (key == 32):
        left_motor.setVelocity(0.)
        right_motor.setVelocity(0.)         
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()
    # print ("GO")
    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
