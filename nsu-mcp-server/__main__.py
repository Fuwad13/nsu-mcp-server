from server import mcp
import sys, signal


def signal_handler(sig, frame):
    print("Shutting down server...")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

print("Starting server...")
sys.exit(mcp.run())
