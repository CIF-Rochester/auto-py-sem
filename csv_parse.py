import csv


def read_csv(filename):
    data = []
    with open(filename, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            time, x, y = float(row[0]), float(row[1]), float(row[2])
            data.append((time, x, y))
    return data


def find_max_y(data):
    max_y = 0.0
    for time, x, y in data:
        if y > max_y:
            max_y = y
    return max_y



#csv_filename = 'rocket_trajectory.csv'

#traj_data = read_csv(csv_filename)
#max_y = find_max_y(traj_data)

#print(f'Maximum Y position of the rocket: {max_y} meters')
