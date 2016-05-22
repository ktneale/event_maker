# event_maker.py
Tool to script animations in Python and capture jpeg output (for user with mjpeg-streamer).

### 1) Notes

This script requires 'Python' and 'PyGame' to be available on the host system.


### 2) Usage

`$python ./event_maker <event_name> e.g. /event_maker "motion test 1b"`

### 3) To use output with mjpeg-streamer

`$export LD_LIBRARY_PATH="$(pwd)"`

`$./mjpg_streamer -i "input_file.so -f <path_to_output from event_maker> -e -d 1" -o "output_http.so -w www -p 8080" &`

