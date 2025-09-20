
import argparse
from picamera2 import Picamera2
import cv2
import threading
import time

# -----------------------
# Parse CLI arguments
# -----------------------
parser = argparse.ArgumentParser(description="Pi Camera Video Capture")
parser.add_argument("--framerate", type=float, default=20.0,
                    help="Frames per second")
parser.add_argument("--width", type=int, default=640, help="Video width")
parser.add_argument("--height", type=int, default=480, help="Video height")
parser.add_argument("--output", type=str, default="output.mp4", help="Output filename")
parser.add_argument("--duration", type=int, default=10,
                    help="Recording duration in seconds")
args = parser.parse_args()

# Global flag for threading
recording_complete = threading.Event()

# Timer thread function
def timer_thread(duration):
    start_time = time.time()
    while time.time() - start_time < duration:
        time.sleep(60) # doesn't need to be that frequent, once a minute is fine
    recording_complete.set()
    print("\nRecording complete")

# init picamera
picam2 = Picamera2()
preview_config = picam2.create_preview_configuration(
    main={"format": "RGB888", "size": (args.width, args.height)},
    controls={"FrameRate": args.framerate}
)
picam2.configure(preview_config)
picam2.start()

# cv2 video writer
fourcc = cv2.VideoWriter_fourcc(*'avc1')  # H.264 for MP4
out = cv2.VideoWriter(args.output, fourcc, args.framerate, (args.width, args.height))

# start thread timer
timer = threading.Thread(target=timer_thread, args=(args.duration,))
timer.start()

# main loop
try:
    while not recording_complete.is_set():
        frame = picam2.capture_array()
        out.write(frame)

finally:
    # Wait for timer thread to complete
    timer.join()
    picam2.stop()
    out.release()