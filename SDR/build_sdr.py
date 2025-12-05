import os

def build_sdr():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    modules_dir = os.path.join(base_dir, 'modules')
    output_file = os.path.join(base_dir, 'SDR.md')

    if not os.path.exists(modules_dir):
        print(f"Error: Modules directory not found at {modules_dir}")
        return

    # Get all markdown files in the modules directory, sorted by name
    files = [f for f in os.listdir(modules_dir) if f.endswith('.md')]
    files.sort()

    print(f"Found {len(files)} modules to combine.")

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for i, filename in enumerate(files):
            filepath = os.path.join(modules_dir, filename)
            print(f"Processing {filename}...")
            
            with open(filepath, 'r', encoding='utf-8') as infile:
                content = infile.read()
                outfile.write(content)
                
                # Add a newline between modules if not already present at the end
                if not content.endswith('\n'):
                    outfile.write('\n')
                
                # Add an extra newline for separation between modules, except for the last one
                if i < len(files) - 1:
                    outfile.write('\n')

    print(f"Successfully created {output_file}")

if __name__ == "__main__":
    build_sdr()
