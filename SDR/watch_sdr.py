import time
import os
import sys
from build_sdr import build_sdr

def get_mtime(dir_path):
    """Returns a dictionary of filename: mtime for all markdown files in the directory."""
    mtimes = {}
    try:
        for filename in os.listdir(dir_path):
            if filename.endswith(".md"):
                filepath = os.path.join(dir_path, filename)
                mtimes[filepath] = os.path.getmtime(filepath)
    except FileNotFoundError:
        pass
    return mtimes

def watch():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    modules_dir = os.path.join(base_dir, 'modules')
    
    if not os.path.exists(modules_dir):
        print(f"Error: Modules directory not found at {modules_dir}")
        return

    print(f"👀 Watching {modules_dir} for changes...")
    print("Press Ctrl+C to stop.")
    
    last_mtimes = get_mtime(modules_dir)
    
    try:
        while True:
            time.sleep(1)
            current_mtimes = get_mtime(modules_dir)
            
            # Check if any file has changed or if files were added/removed
            if current_mtimes != last_mtimes:
                print("\n🔄 Change detected! Rebuilding SDR.md...")
                try:
                    build_sdr()
                    print("✅ Build complete. Waiting for changes...")
                except Exception as e:
                    print(f"❌ Error during build: {e}")
                
                last_mtimes = current_mtimes
                
    except KeyboardInterrupt:
        print("\n🛑 Stopping watcher.")

if __name__ == "__main__":
    watch()
