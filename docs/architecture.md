# TablePickCV Architecture

## Overview

TablePickCV is a modular pipeline for vision-guided robotic pick-and-place operations. The system processes visual input through several stages to generate pick commands for a robot.

## Pipeline Flow

```
┌─────────┐    ┌───────────┐    ┌─────────────┐    ┌───────┐
│  Input  │───▶│ Detection │───▶│ Segmentation│───▶│ Depth │
└─────────┘    └───────────┘    └─────────────┘    └───────┘
                                                        │
                                                        ▼
┌─────────┐    ┌────────┐    ┌─────────────────┐
│  Robot  │◀───│ Export │◀───│ Pose Estimation │
└─────────┘    └────────┘    └─────────────────┘
```

## Modules

### 1. Input (`src/input/`)
Handles all input sources:
- **ImageLoader**: Load images from a folder
- **VideoSource**: Read from video files or webcam
- **RGBDCamera**: Interface with depth cameras (RealSense, etc.)

### 2. Detection (`src/detection/`)
Object detection using deep learning:
- **YOLODetector**: Fast object detection with YOLO
- Returns bounding boxes with class labels and confidence

### 3. Segmentation (`src/segmentation/`)
Instance segmentation for precise object boundaries:
- **SAMSegmenter**: Segment Anything Model integration
- Takes bounding boxes, outputs pixel-precise masks

### 4. Depth (`src/depth/`)
3D information processing:
- **RGBDProcessor**: Align depth to RGB, extract 3D points
- **PointCloudGenerator**: Create point clouds from depth maps

### 5. Pose Estimation (`src/pose_estimation/`)
Calculate grasp poses:
- **PickPoseCalculator**: Compute X, Y, Z + orientation
- Uses mask centroid + depth for 3D position
- PCA or other methods for orientation

### 6. Export (`src/export/`)
Output and visualization:
- **JSONExporter**: Save results to structured JSON
- **Visualizer**: Draw boxes, masks, and poses on images

### 7. Robot (`src/robot/`)
Robot interfaces:
- **ROS2Interface**: Publish commands via ROS2
- **PyBulletSim**: Simulation environment for testing

### 8. Pipeline (`src/pipeline/`)
Main orchestrator:
- **Orchestrator**: Wire all modules together
- Handles configuration and execution flow

## Data Flow

Each module communicates through well-defined data structures:

```python
# Detection output
@dataclass
class Detection:
    bbox: tuple[int, int, int, int]  # x1, y1, x2, y2
    class_id: int
    class_name: str
    confidence: float

# Segmentation output
@dataclass
class SegmentedObject:
    detection: Detection
    mask: np.ndarray  # Binary mask

# Pose output
@dataclass
class PickPose:
    position: tuple[float, float, float]  # X, Y, Z in meters
    orientation: float  # Yaw angle in radians
    object_id: int
```

## Configuration

All settings are managed through YAML files in `configs/`:
- `pipeline_config.yaml`: Main pipeline settings
- Module-specific configs as needed

## Extending the System

To add a new detector:
1. Create a new file in `src/detection/`
2. Implement the detector interface
3. Register in `detection/__init__.py`
4. Add config options to `pipeline_config.yaml`
