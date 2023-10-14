import subprocess

# List of required modules
required_modules = ['argparse', 'googleapiclient', 'pytube']

# Function to install modules
def install_required_modules():
    for module in required_modules:
        try:
            subprocess.check_call(['pip', 'install', module])
            print(f'Successfully installed {module}')
            
        except subprocess.CalledProcessError:
            print(f'Failed to install {module}')

if __name__ == "__main__":
    install_required_modules()