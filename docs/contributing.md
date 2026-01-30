# Contributing to TablePickCV

Welcome! We're excited to have you contribute to this community-driven project. This guide will help you get started.

## 🚀 Getting Started

### Step 1: Fork the Repository

Before you can contribute, you need to create your own copy of the repository:

1. Visit the repository at: **https://github.com/pysource-com/TablePickCV**
2. Click the **Fork** button in the top-right corner of the page
3. Select your GitHub account as the destination for the fork
4. Wait for GitHub to create your personal copy of the repository

This creates a complete copy of the project under your GitHub account where you can make changes without affecting the original repository.

### Step 2: Clone Your Fork

Once you've forked the repository, clone it to your local machine:

```bash
# Replace YOUR-USERNAME with your actual GitHub username
git clone https://github.com/YOUR-USERNAME/TablePickCV.git
cd TablePickCV
```

Alternatively, if you have SSH configured with GitHub:

```bash
git clone git@github.com:YOUR-USERNAME/TablePickCV.git
cd TablePickCV
```

### Step 3: Set Up Upstream Remote

Add the original repository as an upstream remote to keep your fork synchronized:

```bash
git remote add upstream https://github.com/pysource-com/TablePickCV.git
git remote -v  # Verify the remotes
```

### Step 4: Set Up Your Environment

```bash
# Create a virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 5: Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

## 📝 Workflow

1. **Pick an issue** from the Issues tab
2. **Comment** on the issue to let others know you're working on it
3. **Create a branch** for your work
4. **Make your changes** with clear, small commits
5. **Test your changes** - add tests if applicable
6. **Open a Pull Request** with a clear description

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
├── configs/               # Configuration files
├── data/                  # Sample data (gitignored)
├── docs/                  # Documentation
└── scripts/               # Helper scripts
```

## 🎯 Coding Guidelines
- Keep functions focused and small

### Example Function

```python
def detect_objects(image: np.ndarray, confidence: float = 0.5) -> list[Detection]:
    """
    Detect objects in an image using the configured model.

    Args:
        image: Input image as numpy array (H, W, C) in BGR format
        confidence: Minimum confidence threshold (0.0 to 1.0)

    Returns:
        List of Detection objects with bounding boxes and labels
    """
    # Implementation here
    pass
```

### Commits
- Write clear commit messages
- Use present tense: "Add feature" not "Added feature"
- Reference issues: "Fix #12: Handle empty image input"

## 🧪 Testing

```bash
# Run all tests
pytest

# Run tests for a specific module
pytest tests/test_input.py

# Run with coverage
pytest --cov=src
```

## 📖 Learning Notes

After completing your contribution, consider adding a short learning note in `docs/learnings/`:

```markdown
# Your Name - What I Learned

## Date: YYYY-MM-DD

## Task
Brief description of what you worked on.

## Key Learnings
- Point 1
- Point 2

## Challenges & Solutions
What was tricky and how you solved it.
```

## ❓ Questions?

- Open a Discussion on GitHub
- Ask in the AI Vision Academy community

Thank you for contributing! 🎉
