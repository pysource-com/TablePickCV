# Installation Guide

## Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Git

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_ORG/TablePickCV.git
cd TablePickCV
```

### 2. Create Virtual Environment

**Windows:**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

**Linux/Mac:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Optional Components

### PyTorch (for GPU acceleration)

Visit https://pytorch.org/get-started/locally/ and select your configuration.

Example for CUDA 11.8:
```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

### Segment Anything (SAM)

```bash
pip install git+https://github.com/facebookresearch/segment-anything.git
```

Download model weights:
- [sam_vit_b](https://dl.fbaipublicfiles.com/segment_anything/sam_vit_b_01ec64.pth) (375 MB)
- [sam_vit_l](https://dl.fbaipublicfiles.com/segment_anything/sam_vit_l_0b3195.pth) (1.2 GB)
- [sam_vit_h](https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth) (2.4 GB)

### ROS2 (for robot integration)

Follow the official ROS2 installation guide:
https://docs.ros.org/en/humble/Installation.html

### PyBullet (for simulation)

```bash
pip install pybullet
```

### Intel RealSense (for depth cameras)

```bash
pip install pyrealsense2
```

## Verify Installation

```bash
# Run tests
pytest

# Check imports
python -c "from src.input import *; print('Input module OK')"
python -c "from src.detection import *; print('Detection module OK')"
```

## Troubleshooting

### CUDA not found
- Ensure NVIDIA drivers are installed
- Check CUDA version compatibility with PyTorch

### OpenCV import error
- Try: `pip install opencv-python-headless` for server environments

### Permission errors on Linux
- Camera access may require: `sudo usermod -a -G video $USER`
