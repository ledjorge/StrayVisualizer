import numpy as np
import open3d as o3d

# Ensure previous_pose and T_WC are numpy arrays with correct shape
previous_pose = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
T_WC = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

try:
    # Print shapes and types for debugging
    print(f"previous_pose shape: {previous_pose.shape}, type: {type(previous_pose)}")
    print(f"T_WC shape: {T_WC.shape}, type: {type(T_WC)}")

    # Extract translation components
    previous_pose_translation = np.array([ 0.01807438,  0.01682918, -0.00030578])  #previous_pose[:3, 3]
    T_WC_translation = np.array([ 0.01877652,  0.01688515, -0.00099689])   #T_WC[:3, 3]

    # Combine into a 2D numpy array
    points_array = np.vstack([previous_pose_translation, T_WC_translation])

    # Create the Vector3dVector
    points = o3d.utility.Vector3dVector(points_array)

    print("Points created successfully:")
    print(np.asarray(points))

    # Ensure indices are in a numpy array with int32 type
    line_indices = np.array([[0, 1]], dtype=np.int32)

    # Create the Vector2iVector
    lines = o3d.utility.Vector2iVector(line_indices)

    print("Lines created successfully:")
    print(np.asarray(lines))
except Exception as e:
    print(f"An error occurred: {e}")
