import os
import subprocess
import json
import csv
import pygetwindow as gw

def get_access_token():
    with open("config.json") as config_file:
        config_data = json.load(config_file)
        return config_data["access_token"]

def get_save_path():
    with open("config.json") as config_file:
        config_data = json.load(config_file)
        if config_data["save_path"] == "":
            return os.path.expanduser(config_data["default_save_path"])
        else: return config_data["save_path"]

def set_save_path(users_save_path):
    with open("config.json", "r") as config_file:
        config_data = json.load(config_file)

    if users_save_path:
        config_data['save_path'] = users_save_path

        with open('config.json', 'w') as config_file:
            json.dump(config_data, config_file, indent=4)
    
    return print(f"Saved user's save location {users_save_path}")


def write_data_to_file(data_arr, last_month_arr):

    start_date, end_date = last_month_arr
    save_path = get_save_path()
    print(f"Here is a save path: {save_path}")
    output_directory = os.path.expanduser(save_path)
    
    file_path = os.path.join(output_directory, f'Assets Deployed - {start_date} - {end_date}.csv')

    with open(file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(data_arr)
    
    new_file_location = os.path.abspath(save_path)

    window = gw.getWindowsWithTitle(new_file_location)

    if window:
        window[0].activate()
    else:
        subprocess.run(["explorer", new_file_location], shell=True)
    
    return print(f'CSV file "{file_path}" created and data written.')