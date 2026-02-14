# Configuration Management Report

**Automated Micro Story Generator**  
**CISC 594 — Software Engineering**  
**Team:** Dhruv Sharma, Durga Sai Sandeep Rayapureddy, Isit Pokharel, Tan Nguyen

---

## 1. Version Control System

| Component | Details |
|-----------|---------|
| **System** | Git |
| **Hosting** | GitHub (or equivalent remote) |
| **Repository** | automated-micro-story-generator |

---

## 2. Branching Strategy

The project uses a **Git Flow–style** branching model:

```
main (production)
  └── develop (integration)
        └── feature/v1-template-engine
        └── feature/v2-ai-generation
```

| Branch | Purpose |
|--------|---------|
| `main` | Production-ready code; tagged releases (v1.0, v2.0) |
| `develop` | Integration branch for completed features |
| `feature/*` | Isolated development for V1, V2, or other features |

---

## 3. Change Control Process

### 3.1 Workflow

1. **Create feature branch** from `develop`:
   ```bash
   git checkout develop
   git checkout -b feature/v1-template-engine   # or feature/v2-ai-generation
   ```

2. **Develop and commit** on the feature branch:
   ```bash
   git add .
   git commit -m "feat: add genre-based templates"
   ```

3. **Merge to develop** when the feature is complete:
   ```bash
   git checkout develop
   git merge feature/v1-template-engine
   ```

4. **Run tests** on `develop`:
   ```bash
   pytest tests/ -v
   ```

5. **Merge to main** when all tests pass and the release is ready:
   ```bash
   git checkout main
   git merge develop
   ```

6. **Tag the release**:
   ```bash
   git tag -a v1.0 -m "Version 1.0: Template-based story generator"
   git push origin v1.0
   ```

### 3.2 Commit Conventions

- Use clear, descriptive messages
- Prefix with scope when helpful: `feat:`, `fix:`, `docs:`, `test:`
- Example: `feat: add AI mode with Claude API fallback`

---

## 4. Release Tagging

| Version | Tag | Description |
|---------|-----|-------------|
| V1 | `v1.0` | Template-based story generator (genres, multi-paragraph) |
| V2 | `v2.0` | AI-enhanced generation with Claude API and fallback |

### Creating and Pushing Tags

```bash
# Create annotated tag
git tag -a v1.0 -m "Version 1.0: Template-based story generator"

# Push tag to remote
git push origin v1.0
```

---

## 5. Repository State

### 5.1 Git Log

```
$ git log --oneline --graph -20
* 2b81f66 Initial commit from local folder
* 963c75c Initial commit
```

### 5.2 Branches

```
$ git branch -a
* main
  remotes/origin/HEAD -> origin/main
  remotes/origin/main
```

### 5.3 Tags

```
$ git tag -l
v1.0
v2.0
```

---

## 6. Recommendations

1. ~~**Create tags** for v1.0 and v2.0 if not already present.~~ *(Done.)*
2. **Create `develop` branch** and adopt the branching strategy for future work.
3. **Protect `main`** (e.g., via GitHub branch protection) if working in a team.

---

## 7. Commands Reference

| Section | Command | Purpose |
|---------|---------|---------|
| Git log | `git log --oneline --graph -20` | Show commit history and structure |
| Branches | `git branch -a` | Show local and remote branches |
| Tags | `git tag -l` | Show release tags |
| Merge history | `git log --oneline --merges` | Show merge commits |
