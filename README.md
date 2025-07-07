# Enterprise CI/CD Platform (Sample)

This project demonstrates a scalable CI/CD pipeline using GitHub Actions, AWS ECR, EKS (Kubernetes), Docker, and SonarQube.

## Features
- Automated testing (pytest)
- Code quality & security scanning (SonarQube)
- Docker build & push to AWS ECR
- Kubernetes deployment to AWS EKS
- Triggered on every commit to `main`

## Directory Structure
```
.
├── app/                  # Flask app source code
│   ├── main.py
│   ├── requirements.txt
│   └── tests/
├── Dockerfile            # Docker build file
├── k8s/                  # Kubernetes manifests
│   ├── deployment.yaml
│   └── service.yaml
├── sonar-project.properties # SonarQube config
├── .github/workflows/ci-cd.yml # GitHub Actions workflow
└── README.md
```

## Prerequisites
- AWS account with ECR and EKS set up
- GitHub repository with the following secrets:
  - `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION`
  - `ECR_REPOSITORY` (name of your ECR repo)
  - `EKS_CLUSTER_NAME` (name of your EKS cluster)
  - `SONAR_TOKEN`, `SONAR_HOST_URL` (for SonarQube)

## How it Works
1. **On push to `main`:**
   - Runs tests and SonarQube scan
   - Builds and pushes Docker image to ECR
   - Updates Kubernetes deployment in EKS

## Setup Steps
1. **Clone this repo and push to your GitHub repository.**
2. **Set up the required GitHub secrets** (see above).
3. **Ensure your EKS cluster and ECR repo exist.**
4. **Push a commit to `main` to trigger the pipeline.**

## Customization
- Edit `app/main.py` for your app logic.
- Update `k8s/deployment.yaml` and `k8s/service.yaml` for your deployment needs.
- Adjust the workflow in `.github/workflows/ci-cd.yml` as needed.

## Notes
- The workflow uses `sed` to inject the Docker image URI into the deployment manifest before applying it.
- SonarQube scan requires a running SonarQube server and a valid token.

---

For questions or improvements, open an issue or PR! 