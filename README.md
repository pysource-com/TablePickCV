# TablePickCV

**Vision-guided tabletop pick-and-place using open-source computer vision and robotics.**

TablePickCV is a community-driven, educational open-source project that builds a modular pipeline to:

- detect objects on a table
- segment them
- estimate a 3D pick pose (position + orientation)
- send the pick command to a robot (via ROS2 or simulation)

## 🎯 Goals

- Provide a **clean reference architecture** for real-world vision + robotics projects
- Learn how to structure a **modular CV/robotics system**
- Learn **collaborative development** with GitHub (issues, PRs, reviews)
- Produce something that actually works in **simulation and/or real hardware**

## 📂 Project Structure

```
TablePickCV/
├── src/                    # Source code
│   ├── input/             # Camera, video, image sources
│   ├── detection/         # Object detection (YOLO, etc.)
│   ├── segmentation/      # Instance segmentation (SAM, etc.)
│   ├── depth/             # RGB-D processing
│   ├── pose_estimation/   # Pick pose calculation
│   ├── export/            # JSON export, visualization
│   ├── robot/             # ROS2/simulation interfaces
│   ├── pipeline/          # Main orchestrator
│   └── utils/             # Shared utilities
├── tests/                  # Unit tests
├── configs/               # YAML configuration files
├── data/                  # Sample data (gitignored)
├── docs/                  # Documentation
│   ├── learnings/         # Contributor learning notes
│   └── setup/             # Installation guides
└── scripts/               # Helper scripts
```

## 🧱 Planned V1 Features

- Input from camera / video / image folder
- Object detection (YOLO)
- Object segmentation (SAM)
- Depth integration (RGB-D)
- Pick pose estimation (X, Y, Z + yaw)
- JSON export + visualization
- Simple robot execution:
  - ROS2 + MoveIt OR
  - Simulation (PyBullet)

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/YOUR_ORG/TablePickCV.git
cd TablePickCV

```

## 📦 Project Status

🚧 **Early development** — project skeleton and first modules are being set up.

## 🤝 How to Contribute

We welcome contributors of all experience levels! Here's how to get started:

1. **Check the [Issues](../../issues) tab** — we have beginner, intermediate, and advanced tasks
2. **Comment on an issue** to let others know you're working on it
3. **Fork the repo** and create a branch for your work
4. **Open a PR** when ready
5. **Add a learning note** in `docs/learnings/` to share what you learned

📖 **Full guide:** [docs/contributing.md](docs/contributing.md)

📐 **Architecture:** [docs/architecture.md](docs/architecture.md)

🛠️ **Installation:** [docs/setup/installation.md](docs/setup/installation.md)


## 🪪 License

MIT License — see [LICENSE](LICENSE)

---

Built by the members of the **AI Vision Academy** community:  
https://www.skool.com/ai-vision-academy

