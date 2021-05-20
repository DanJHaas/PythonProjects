import sys
import time
import openvr

openvr.init(openvr.VRApplication_Scene)

poses = []  # Let waitGetPoses populate the poses structure the first time

# Print out headset transform five times a second for 20 seconds
for i in range(100):
    poses, game_poses = openvr.VRCompositor().waitGetPoses(poses, None)
    hmd_pose = poses[openvr.k_EButton_IndexController_A]
    print(hmd_pose.mDeviceToAbsoluteTracking[0][0:])
    sys.stdout.flush()
    time.sleep(0.2)

openvr.shutdown()