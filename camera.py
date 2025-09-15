import argparse
from picamera2 import Picamera2
import cv2

# -----------------------
# Parse CLI arguments
# -----------------------
parser = argparse.ArgumentParser(description="Pi Camera Video Capture")
parser.add_argument("--framerate", type=float, default=20.0,
                    help="Frames per second")
parser.add_argument("--width", type=int, default=640, help="Video width")
parser.add_argument("--height", type=int, default=480, help="Video height")
parser.add_argument("--output", type=str, default="output.mp4", help="Output filename")
args = parser.parse_args()

# -----------------------
# Initialize Picamera2
# -----------------------
picam2 = Picamera2()
preview_config = picam2.create_preview_configuration(
    main={"format": "RGB888", "size": (args.width, args.height)},
    controls = {"FrameRate": args.framerate}
)
picam2.configure(preview_config)
picam2.start()

# -----------------------
# OpenCV VideoWriter
# -----------------------
fourcc = cv2.VideoWriter_fourcc(*'avc1')  # H.264 for MP4
out = cv2.VideoWriter(args.output, fourcc, args.framerate, (args.width, args.height))

# -----------------------
# Main capture loop
# -----------------------
try:
    while True:
        frame = picam2.capture_array()
        cv2.imshow("Camera Preview", frame)
        out.write(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    picam2.stop()
    out.release()
    cv2.destroyAllWindows()
