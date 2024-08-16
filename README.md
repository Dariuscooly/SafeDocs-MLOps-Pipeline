# SafeDocs-MLOps-Pipeline
This repository hosts the SafeDocs: Technical Architecture V2 project, implementing an MLOps pipeline with AWS Textract, S3, Lambda, RDS, and API Gateway. The project automates the extraction, categorization, and analysis of handwritten notes, enabling real-time document processing and review via a scalable AWS-based solution.

## Project Overview
SafeDocs: Technical Architecture V2 is a project designed to develop an end-to-end MLOps pipeline utilizing various AWS services. The goal is to build an application that extracts handwritten notes from documents using AWS Textract, categorizes them, and processes the data through a scalable pipeline. The application also reviews documents, counts occurrences of specific meal terms ("breakfast," "lunch," "dinner"), and interprets symbols to repeat previous meals.

## Key Technologies
- **AWS Textract**: For extracting text and table data from handwritten documents.
- **AWS S3**: Storage for documents and processed data.
- **AWS Lambda**: Serverless compute for processing data and managing triggers.
- **Amazon RDS**: Relational database for storing processed data.
- **AWS API Gateway**: To expose the application through a RESTful API.
- **GitHub Actions**: For continuous integration and deployment of the MLOps pipeline.
- **Amazon SageMaker**: Manages the MLOps pipeline, including training, deploying, and monitoring machine learning models.

digraph G {
    node [shape=box];
    SafeDocs_MLOps_Pipeline -> src;
    SafeDocs_MLOps_Pipeline -> tests;
    SafeDocs_MLOps_Pipeline -> docs;
    SafeDocs_MLOps_Pipeline -> .github;
    SafeDocs_MLOps_Pipeline -> README.md;
    SafeDocs_MLOps_Pipeline -> .gitignore;
    SafeDocs_MLOps_Pipeline -> requirements.txt;
    
    src -> pipeline.py;
    src -> train.py;
    src -> process_data.py;
    
    tests -> test_pipeline.py;
    
    docs -> architecture.md;
    docs -> setup_instructions.md;
    
    .github -> workflows;
    workflows -> deploy.yml;
}

