# 🚀 Machine Learning Model Deployment with FastAPI, Docker, and AWS  

This repository showcases my **first DevOps project**, where I successfully deployed a **Machine Learning model** as a production-ready web service using **FastAPI**, **Docker**, and **AWS**.  

In addition, I’ve also authored a **research paper** published in the **Journal of Civil and Environmental Engineering** titled:  
**"Leveraging Ensemble Models for Multimodal Harmful Speech Detection on Social Media"**.  

---

## 🌐 Project Overview  
The project demonstrates the **end-to-end process of deploying an ML model** into a scalable and secure environment. From building the FastAPI application to containerizing with Docker and deploying on AWS infrastructure, this project captures the complete lifecycle of modern ML deployment.  

---

## 🛠️ Key Features  

1. **Machine Learning Model Integration**  
   - Wrapped a trained ML model into a **FastAPI application**.  
   - Served predictions through clean REST APIs with automatic docs (`/docs`).  

2. **FastAPI Framework**  
   - High-performance, asynchronous Python framework.  
   - Automatic OpenAPI and Swagger documentation.  
   - Easy-to-scale architecture.  

3. **Docker Containerization**  
   - Containerized the application for portability and consistent deployments.  
   - Built Docker images for local testing and production readiness.  

4. **AWS ECR & EC2 Deployment**  
   - Stored Docker images in **Amazon Elastic Container Registry (ECR)**.  
   - Deployed the containerized app on **AWS EC2 instance**.  
   - Configured **networking & security groups** for secure external access.  

5. **Networking & Security Best Practices**  
   - Configured inbound rules for controlled API access.  
   - Hardened deployment environment with IAM roles and least-privilege policies.  

6. **Troubleshooting & Debugging**  
   - Documented challenges in Docker + AWS deployment.  
   - Shared solutions for common issues (port binding, ECR auth, EC2 security).  

---

## ⚙️ Tech Stack  
- **Backend:** FastAPI (Python)  
- **ML Model:** Pre-trained model (Ensemble-based for harmful speech detection reference)  
- **Containerization:** Docker  
- **Cloud:** AWS EC2, ECR  
- **Networking & Security:** AWS Security Groups, IAM roles  
- **Version Control:** Git + GitHub  

---

## 📊 Workflow  

1. Train or load ML model.  
2. Build **FastAPI app** to serve model predictions.  
3. Write `Dockerfile` and build image locally.  
4. Push Docker image to **AWS ECR**.  
5. Launch **EC2 instance** and pull image from ECR.  
6. Run container → expose API endpoints securely.  
7. Test deployment with external requests.  

---

## 📜 Research Publication  

I am also proud to share my research work:  

**Paper Title:** *Leveraging Ensemble Models for Multimodal Harmful Speech Detection on Social Media*  
**Journal:** *Journal of Civil and Environmental Engineering*  
**Publication Year:** 2025  
📄 [Read the Paper](https://ijcee.in/volume-12-issue-10-2024/)  

The research explores **ensemble learning approaches** for harmful speech detection on social media by leveraging **multimodal features (text, metadata, and context)**, advancing the field of **AI for social good**.  

---

## 🔮 Future Enhancements  
- Add **CI/CD pipeline** with GitHub Actions or AWS CodePipeline.  
- Integrate with **AWS Lambda + API Gateway** for serverless deployment.  
- Expand ML model deployment to support **batch inference + monitoring**.  
- Extend harmful speech detection system into a **real-time moderation tool**.  

---

## 🌟 Acknowledgments  
This project reflects my **first step as a DevOps Engineer** 🚀 and builds upon my academic foundation in **Machine Learning research**.  

---