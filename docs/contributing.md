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

### Step 5: Pick an Issue & Create a Branch

1. **Browse the Issues tab** at https://github.com/pysource-com/TablePickCV/issues
2. **Find an issue** that interests you (look for "good first issue" labels if you're new)
3. **Comment on the issue** to let maintainers and others know you're working on it
4. **Create a branch** for your work:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

### Step 6: Make Your Changes

- Write clear, focused code
- Make small, logical commits as you work
- Test your changes thoroughly
- Add tests if you're introducing new features

## 🔄 Submitting a Pull Request

### Step 1: Commit Your Changes

```bash
# Stage your changes
git add .

# Commit with a descriptive message
git commit -m "Add: table detection feature for YOLO model"
```

### Step 2: Keep Your Branch Updated

Before submitting, sync with the latest changes from the main repository:

```bash
# Fetch the latest changes from upstream
git fetch upstream

# Merge upstream changes into your branch
git merge upstream/main

# Resolve any conflicts if they occur
```

### Step 3: Push to Your Fork

```bash
git push origin feature/your-feature-name
```

### Step 4: Create the Pull Request

1. Go to your fork on GitHub: `https://github.com/YOUR-USERNAME/TablePickCV`
2. You'll see a banner saying "Compare & pull request" - click it
3. Alternatively, go to the **Pull Requests** tab and click **New Pull Request**
4. Ensure the base repository is `pysource-com/TablePickCV` and base branch is `main`
5. Ensure the head repository is your fork and compare branch is your feature branch

### Step 5: Fill Out the PR Description

Provide a clear description of your changes:

```markdown
## Description
Brief summary of what this PR does.

## Related Issue
Closes #123

## Changes Made
- Added table detection module
- Updated configuration schema
- Added unit tests for detection

## Testing
- [ ] Tested with sample images
- [ ] All tests pass locally
- [ ] Added new tests for new features

## Screenshots (if applicable)
Add screenshots or videos demonstrating the changes.
```

### Step 6: Submit and Respond to Feedback

1. Click **Create Pull Request**
2. Wait for maintainers to review your PR
3. Respond to any feedback or requested changes
4. Push additional commits to your branch if changes are needed (they'll automatically appear in the PR)

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
