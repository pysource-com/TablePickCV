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


## 🧱 Planned V1 Features

- Input from camera / video / image folder
- Object detection
- Object segmentation
- Depth integration (RGB-D)
- Pick pose estimation (X, Y, Z + yaw)
- JSON export + visualization
- Simple robot execution:
  - ROS2 + MoveIt OR
  - Simulation (e.g. PyBullet)

## 📦 Project Status

🚧 **Early development** — project skeleton and first modules are being set up.

## 🤝 How to participate

- Check the issues tab
- Pick a task
- Open a PR
- Add a short learning note in `docs/learnings/`

See: `docs/contributing.md`

## 🪪 License

MIT License — see `LICENSE`

---

Built by the members of the **AI Vision Academy** community:  
https://www.skool.com/ai-vision-academy
