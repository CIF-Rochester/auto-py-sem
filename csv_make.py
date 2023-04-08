import csv
import math


def rocket_trajectory(initial_velocity, launch_angle, time_step=0.1, gravity=9.81):
    traj_data = []
    time = 0.0
    angle_rad = math.radians(launch_angle)

    # Calculate horizontal and vertical components of initial velocity
    initial_velocity_x = initial_velocity * math.cos(angle_rad)
    initial_velocity_y = initial_velocity * math.sin(angle_rad)

    y = 0.0
    current_velocity_y = initial_velocity_y

    while y >= 0:
        # Calculate horizontal and vertical positions
        x = initial_velocity_x * time
        y = y + current_velocity_y * time_step - 0.5 * gravity * time_step**2

        # Update vertical velocity
        current_velocity_y = current_velocity_y - gravity * time_step

        traj_data.append((time, x, y))
        time += time_step

    return traj_data


def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Time (s)', 'X (m)', 'Y (m)'])
        for row in data:
            csv_writer.writerow(row)


#initial_velocity = 100.0
#launch_angle = 60.0
#time_step = 0.1

#traj_data = rocket_trajectory(initial_velocity, launch_angle, time_step)
#save_to_csv(traj_data, 'rocket_trajectory.csv')