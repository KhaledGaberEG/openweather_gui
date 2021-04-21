#!/usr/bin/python3
import json
import tkinter as tk
import sys
import subprocess
import pkg_resources
import argparse


country =  ''
city = ''
appid = ""

parser = argparse.ArgumentParser(description='openweathermap api frontend',
                                usage="weather.py --id <API Key>")
parser.add_argument('--id', type=str,
                    help='openweathermap API key SignUP to openweather and pass \
                    key as a command line argument visit \n \
                    https://openweathermap.org/' ,
                    dest="appid", required=True)
args = parser.parse_args()
appid = args.appid
# check if requests is installed

try:
    import requests
except ImportError:
    print("requests is not installed")
    install = input("do you want to install requests[y/n] :")
    if install == 'y':
        python = sys.executable
        subprocess.check_call([python, '-m', 'pip', 'install', "requests"], stdout=subprocess.DEVNULL)
        print("installing requests*******Complete")
    else:
        print("[+] exiting")
        sys.exit()


def get_res():
    url = "https://api.openweathermap.org/data/2.5/weather?appid=" + appid + "&units=metric&q=" + city+',' + country
    print("sending:", url)
    try:
        response = requests.get(url)
        response = json.loads(response.text)
        res.delete(0, tk.END)
        res.insert(index=0, string=str(response["main"]["temp"])+" c°")
        print("successfully retrieved temperature")
    except Exception:
        res.delete(0, tk.END)
        res.insert(index=0, string="Didn't Find your City or Error occured")


def get_input():
    global city
    global country
    country = entry.get()
    city = entry2.get()
    get_res()


mainwindow = tk.Tk()
mainwindow.geometry("624x245")
mainwindow.title("Weather Api")

mainwindow.rowconfigure(0, weight=2)
mainwindow.rowconfigure(1, weight=2)
mainwindow.rowconfigure(2, weight=2)

mainwindow.columnconfigure(0, weight=1)
mainwindow.columnconfigure(1, weight=1)
mainwindow.columnconfigure(2, weight=1)

label = tk.Label( mainwindow, text="Enter Name of country :")
label.grid(row=0, column=0, sticky="wn", pady=0)

label2 = tk.Label(mainwindow, text="Enter Name of the city :")
label2.grid(row=0, column=1, sticky="wn", pady=0)


entry = tk.Entry(mainwindow)
entry.grid(row=0, column=0, sticky="sw")
entry2 = tk.Entry(mainwindow)
entry2.grid(row=0, column=1, sticky="sw")

result_label = tk.Label(text="Temperature")
result_label.grid(row=1, column=1, sticky='w')

res = tk.Entry(mainwindow)
res.grid(row=1, column=1, sticky="sw")

btn = tk.Button(text="Submit", command=get_input)
btn.grid(row=0, column=2, sticky="ws")
mainwindow.mainloop()
