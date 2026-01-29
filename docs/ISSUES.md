# GitHub Issues for TablePickCV

This file contains 15 starter issues for contributors. Copy each issue to GitHub Issues.

---

## 🟢 BEGINNER ISSUES (1-5)

---

### Issue #1: 📁 Set up pytest and create first test

**Labels:** `good first issue`, `testing`, `beginner`

**Description:**
Set up pytest for the project and write the first basic test to ensure the testing infrastructure works.

**Tasks:**
- [ ] Verify pytest is in `requirements.txt` (already added)
- [ ] Create `tests/test_sample.py` with a simple passing test
- [ ] Create `pytest.ini` or add pytest config to `pyproject.toml`
- [ ] Add a test that imports the main `src` module
- [ ] Document how to run tests in the README or contributing guide

**Acceptance Criteria:**
- Running `pytest` from project root executes tests successfully
- At least one meaningful test exists

**Resources:**
- [pytest documentation](https://docs.pytest.org/)

---

### Issue #2: 🖼️ Implement ImageLoader class

**Labels:** `good first issue`, `input`, `beginner`

**Description:**
Create a simple class that loads images from a folder. This is the first input source for the pipeline.

**Tasks:**
- [ ] Create `src/input/image_loader.py`
- [ ] Implement `ImageLoader` class with methods:
  - `__init__(self, folder_path: str)`
  - `__iter__` to iterate through images
  - `__len__` to get total count
- [ ] Support common formats: `.jpg`, `.jpeg`, `.png`, `.bmp`
- [ ] Use OpenCV or Pillow to load images
- [ ] Add basic error handling for invalid paths

**Example Usage:**
```python
loader = ImageLoader("data/sample_images")
for image in loader:
    # image is a numpy array (H, W, C)
    process(image)
```

**Acceptance Criteria:**
- Can load images from a folder
- Returns images as numpy arrays
- Has a test in `tests/test_input.py`

---

### Issue #3: 📝 Create sample images for testing

**Labels:** `good first issue`, `data`, `beginner`

**Description:**
Create or collect a small set of sample images for testing the pipeline. These should show objects on a table.

**Tasks:**
- [ ] Create `data/sample_images/` folder (already exists, ignored by git)
- [ ] Add 5-10 sample images of objects on a table
- [ ] Create `scripts/download_sample_data.py` to download images
- [ ] Update `.gitignore` to ignore large files but keep the script
- [ ] Document sample data in `data/README.md`

**Notes:**
- Use freely licensed images or take your own photos
- Include variety: single object, multiple objects, different lighting

**Acceptance Criteria:**
- Script downloads or generates sample images
- README explains what the data contains

---

### Issue #4: 📊 Create data classes for pipeline objects

**Labels:** `good first issue`, `utils`, `beginner`

**Description:**
Define the core data structures that will be passed between pipeline modules.

**Tasks:**
- [ ] Create `src/utils/data_types.py`
- [ ] Define dataclasses:
  ```python
  @dataclass
  class BoundingBox:
      x1: int
      y1: int
      x2: int
      y2: int
  
  @dataclass
  class Detection:
      bbox: BoundingBox
      class_id: int
      class_name: str
      confidence: float
  
  @dataclass
  class SegmentedObject:
      detection: Detection
      mask: np.ndarray
  
  @dataclass
  class PickPose:
      x: float
      y: float
      z: float
      yaw: float
  ```
- [ ] Add helper methods (e.g., `bbox.area()`, `bbox.center()`)
- [ ] Export from `utils/__init__.py`

**Acceptance Criteria:**
- All dataclasses are defined with type hints
- Basic tests verify dataclass creation

---

### Issue #5: 📖 Write learning note template

**Labels:** `good first issue`, `documentation`, `beginner`

**Description:**
Create a template for contributors to document what they learned while working on the project.

**Tasks:**
- [ ] Create `docs/learnings/TEMPLATE.md`
- [ ] Include sections:
  - Contributor name
  - Date
  - Task/Issue worked on
  - Key learnings
  - Challenges faced
  - Resources that helped
- [ ] Add an example learning note
- [ ] Update `docs/contributing.md` to reference the template

**Acceptance Criteria:**
- Template is clear and easy to follow
- Encourages reflection on the learning process

---

## 🟡 INTERMEDIATE ISSUES (6-10)

---

### Issue #6: 📹 Implement VideoSource class

**Labels:** `enhancement`, `input`, `intermediate`

**Description:**
Create a class that reads frames from video files or webcam, complementing the ImageLoader.

**Tasks:**
- [ ] Create `src/input/video_source.py`
- [ ] Implement `VideoSource` class:
  - `__init__(self, source: str | int)` - path or camera ID
  - `read() -> tuple[bool, np.ndarray]`
  - `release()`
  - Context manager support (`__enter__`, `__exit__`)
- [ ] Handle video file playback with configurable FPS
- [ ] Support webcam capture
- [ ] Add frame skipping option for performance

**Example Usage:**
```python
with VideoSource(0) as cam:  # webcam
    while True:
        success, frame = cam.read()
        if not success:
            break
        process(frame)
```

**Acceptance Criteria:**
- Works with video files and webcam
- Proper resource cleanup
- Tests with a sample video

---

### Issue #7: 🎯 Integrate YOLO detector

**Labels:** `enhancement`, `detection`, `intermediate`

**Description:**
Implement object detection using YOLOv8 from the Ultralytics library.

**Tasks:**
- [ ] Create `src/detection/yolo_detector.py`
- [ ] Implement `YOLODetector` class:
  - `__init__(self, model_path: str, confidence: float = 0.5)`
  - `detect(image: np.ndarray) -> list[Detection]`
- [ ] Load model weights (download if needed)
- [ ] Convert YOLO output to our `Detection` dataclass
- [ ] Support filtering by class IDs
- [ ] Add configuration in `configs/`

**Dependencies:**
- `ultralytics` package (already in requirements.txt)

**Acceptance Criteria:**
- Detects objects and returns `Detection` objects
- Configurable confidence threshold
- Works with sample images

---

### Issue #8: 📊 Create JSON exporter

**Labels:** `enhancement`, `export`, `intermediate`

**Description:**
Implement a module to save detection and pose results to JSON files.

**Tasks:**
- [ ] Create `src/export/json_exporter.py`
- [ ] Implement `JSONExporter` class:
  - `__init__(self, output_dir: str)`
  - `export(results: dict, filename: str)`
  - `export_frame(detections, poses, frame_id)`
- [ ] Define JSON schema for output
- [ ] Support both single-frame and batch export
- [ ] Add timestamp and metadata

**Example Output:**
```json
{
  "timestamp": "2026-01-29T12:00:00",
  "frame_id": 1,
  "detections": [
    {
      "class": "cup",
      "confidence": 0.92,
      "bbox": [100, 150, 200, 300],
      "pick_pose": {"x": 0.15, "y": 0.22, "z": 0.05, "yaw": 0.0}
    }
  ]
}
```

**Acceptance Criteria:**
- Produces valid JSON output
- Handles all dataclass types
- Tests verify output structure

---

### Issue #9: 🖼️ Build visualization module

**Labels:** `enhancement`, `export`, `intermediate`

**Description:**
Create visualization tools to draw detections, masks, and poses on images.

**Tasks:**
- [ ] Create `src/export/visualizer.py`
- [ ] Implement `Visualizer` class:
  - `draw_detections(image, detections) -> image`
  - `draw_masks(image, segmented_objects) -> image`
  - `draw_poses(image, poses) -> image`
  - `draw_all(image, results) -> image`
- [ ] Use distinct colors for different classes
- [ ] Add labels with class name and confidence
- [ ] Optionally save visualized images

**Acceptance Criteria:**
- Clear, informative visualizations
- Doesn't modify original image (returns copy)
- Works with matplotlib and/or OpenCV

---

### Issue #10: ⚙️ Create configuration loader with validation

**Labels:** `enhancement`, `utils`, `intermediate`

**Description:**
Build a robust configuration system using YAML and Pydantic for validation.

**Tasks:**
- [ ] Create `src/utils/config.py`
- [ ] Define Pydantic models for each config section:
  - `InputConfig`
  - `DetectionConfig`
  - `SegmentationConfig`
  - `PoseConfig`
  - `ExportConfig`
  - `RobotConfig`
  - `PipelineConfig` (combines all)
- [ ] Load from YAML file
- [ ] Validate types and ranges
- [ ] Support environment variable overrides

**Example:**
```python
config = PipelineConfig.from_yaml("configs/pipeline_config.yaml")
print(config.detection.confidence_threshold)  # 0.5
```

**Acceptance Criteria:**
- Validates configuration on load
- Clear error messages for invalid config
- Tests cover validation logic

---

## 🔴 ADVANCED ISSUES (11-15)

---

### Issue #11: 📐 Implement RGB-D processor

**Labels:** `enhancement`, `depth`, `advanced`

**Description:**
Create a module to process RGB-D data, aligning depth to color and extracting 3D information.

**Tasks:**
- [ ] Create `src/depth/rgbd_processor.py`
- [ ] Implement `RGBDProcessor` class:
  - `__init__(self, intrinsics: CameraIntrinsics)`
  - `align_depth(color, depth) -> aligned_depth`
  - `pixel_to_3d(u, v, depth) -> tuple[x, y, z]`
  - `get_points_in_mask(depth, mask) -> np.ndarray`
- [ ] Define `CameraIntrinsics` dataclass (fx, fy, cx, cy)
- [ ] Handle depth scale conversion
- [ ] Filter invalid depth values

**Resources:**
- [Pinhole camera model](https://docs.opencv.org/4.x/d9/d0c/group__calib3d.html)
- Intel RealSense SDK examples

**Acceptance Criteria:**
- Correctly converts pixels to 3D coordinates
- Handles depth alignment for non-aligned sensors
- Unit tests with synthetic data

---

### Issue #12: 🤖 Implement pick pose calculator

**Labels:** `enhancement`, `pose_estimation`, `advanced`

**Description:**
Create the core algorithm to calculate grasp poses from segmentation masks and depth data.

**Tasks:**
- [ ] Create `src/pose_estimation/pick_pose_calculator.py`
- [ ] Implement `PickPoseCalculator` class:
  - `__init__(self, rgbd_processor: RGBDProcessor)`
  - `calculate_pose(mask, depth) -> PickPose`
- [ ] Calculate position:
  - Find mask centroid
  - Get depth at centroid (or median depth in mask)
  - Convert to 3D coordinates
- [ ] Calculate orientation (yaw):
  - Use PCA on mask points for major axis
  - Or use depth gradient
- [ ] Add approach offset (pre-grasp position)

**Acceptance Criteria:**
- Produces valid 3D pick poses
- Orientation aligns with object major axis
- Tests with synthetic mask/depth data

---

### Issue #13: 🧩 Integrate Segment Anything (SAM)

**Labels:** `enhancement`, `segmentation`, `advanced`

**Description:**
Integrate Meta's Segment Anything Model for high-quality instance segmentation.

**Tasks:**
- [ ] Create `src/segmentation/sam_segmenter.py`
- [ ] Implement `SAMSegmenter` class:
  - `__init__(self, model_type: str, checkpoint_path: str)`
  - `segment(image, bboxes) -> list[SegmentedObject]`
- [ ] Support prompt types:
  - Bounding box prompts (from detector)
  - Point prompts (optional)
- [ ] Handle model loading and GPU/CPU selection
- [ ] Add model download script

**Dependencies:**
- segment-anything (install from GitHub)
- PyTorch

**Acceptance Criteria:**
- Produces accurate masks from bounding boxes
- Works on CPU (slower) and GPU
- Documented installation steps

---

### Issue #14: 🎮 Create PyBullet simulation environment

**Labels:** `enhancement`, `robot`, `advanced`

**Description:**
Build a simulation environment using PyBullet to test pick-and-place without real hardware.

**Tasks:**
- [ ] Create `src/robot/pybullet_sim.py`
- [ ] Implement `PickPlaceSimulator` class:
  - `__init__(self, robot_urdf: str)`
  - `reset()`
  - `add_object(mesh_path, position, orientation)`
  - `execute_pick(pose: PickPose) -> bool`
  - `get_camera_image() -> tuple[rgb, depth]`
- [ ] Load a simple robot arm (e.g., Franka, UR5, or generic)
- [ ] Implement basic pick motion:
  - Move to pre-grasp
  - Approach
  - Close gripper
  - Lift
- [ ] Add table and random objects

**Resources:**
- [PyBullet quickstart](https://pybullet.org/wordpress/)
- Robot URDF files from GitHub

**Acceptance Criteria:**
- Simulated robot can execute pick commands
- Can render RGB and depth images
- Basic demo script works

---

### Issue #15: ⚙️ Create pipeline orchestrator

**Labels:** `enhancement`, `pipeline`, `advanced`

**Description:**
Build the main orchestrator that wires all modules together into a complete pipeline.

**Tasks:**
- [ ] Create `src/pipeline/orchestrator.py`
- [ ] Implement `Pipeline` class:
  - `__init__(self, config: PipelineConfig)`
  - `setup()` - initialize all modules
  - `process_frame(image, depth=None) -> PipelineResult`
  - `run()` - main loop for video/camera
- [ ] Handle optional modules (depth, segmentation, robot)
- [ ] Add logging and timing
- [ ] Create `PipelineResult` dataclass
- [ ] Create main entry point script

**Example:**
```python
pipeline = Pipeline.from_config("configs/pipeline_config.yaml")
pipeline.setup()

for result in pipeline.run():
    print(f"Detected {len(result.detections)} objects")
    print(f"Pick poses: {result.poses}")
```

**Acceptance Criteria:**
- Runs end-to-end with all implemented modules
- Handles errors gracefully
- Configuration controls which modules are active
- Demo script with sample images

---

## Issue Labels Reference

Create these labels in your GitHub repository:

| Label | Color | Description |
|-------|-------|-------------|
| `good first issue` | #7057ff | Good for newcomers |
| `beginner` | #c5def5 | Beginner-friendly task |
| `intermediate` | #fbca04 | Requires some experience |
| `advanced` | #d93f0b | Complex task |
| `input` | #0e8a16 | Input module |
| `detection` | #1d76db | Detection module |
| `segmentation` | #5319e7 | Segmentation module |
| `depth` | #006b75 | Depth module |
| `pose_estimation` | #b60205 | Pose estimation module |
| `export` | #f9d0c4 | Export module |
| `robot` | #e99695 | Robot module |
| `pipeline` | #c2e0c6 | Pipeline/orchestrator |
| `utils` | #bfdadc | Utilities |
| `testing` | #fef2c0 | Testing related |
| `documentation` | #0075ca | Documentation |
| `data` | #d4c5f9 | Data/samples |
| `enhancement` | #a2eeef | New feature |
