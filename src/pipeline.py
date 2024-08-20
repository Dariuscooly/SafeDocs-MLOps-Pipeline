from sagemaker.estimator import Estimator
from sagemaker.workflow.steps import TrainingStep, ProcessingStep
from sagemaker.workflow.pipeline import Pipeline
from sagemaker.workflow.pipeline_context import PipelineSession
from sagemaker.sklearn.processing import SKLearnProcessor
import sagemaker

# Create a pipeline session
pipeline_session = PipelineSession()

# Define the IAM role for SageMaker
role = 'arn:aws:iam::905418298175:role/AmazonSageMaker-ExecutionRole-SafeDocs-MLOps-Pipeline'  # Replace with your actual role ARN

# Define your S3 bucket URIs
input_data_s3_uri = 's3://crfsafedocs/raw-data/'  # Replace with your input data S3 URI
output_data_s3_uri = 's3://crfsafedocs/processed-data/'  # Replace with your processed data S3 URI
model_artifacts_s3_uri = 's3://crfsafedocs/models/'  # Replace with your model artifacts S3 URI

# Define the Estimator
estimator = Estimator(
    image_uri='your-image-uri',  # Replace with the appropriate Docker image URI
    role=role,
    instance_count=1,
    instance_type='ml.m5.xlarge',
    entry_point='train.py',  # The entry point script for training
    source_dir='src/',  # Directory containing your training script
    output_path=model_artifacts_s3_uri,  # S3 location for model artifacts
    hyperparameters={
        'learning_rate': 0.001,
        'batch_size': 32
    }
)

# Define the SKLearnProcessor for data processing
sklearn_processor = SKLearnProcessor(
    framework_version='0.23-1',
    role=role,
    instance_type='ml.m5.xlarge',
    instance_count=1
)

# Define the ProcessingStep with a valid entry point
processing_step = ProcessingStep(
    name='DataProcessing',
    processor=sklearn_processor,
    inputs=[
        sagemaker.processing.ProcessingInput(
            source=input_data_s3_uri,  # Connect your input data from S3
            destination='/opt/ml/processing/input'
        )
    ],
    outputs=[
        sagemaker.processing.ProcessingOutput(
            source='/opt/ml/processing/output',
            destination=output_data_s3_uri  # Store processed data in the processed-data/ directory
        )
    ],
    code='src/process_data.py',  # Ensure you specify the script to run
    job_arguments=["--input-data", "/opt/ml/processing/input", "--output-data", "/opt/ml/processing/output"]
)

# Define the TrainingStep
training_step = TrainingStep(
    name='ModelTraining',
    estimator=estimator,
    inputs={
        'train': processing_step.properties.ProcessingOutputConfig.Outputs["output"].S3Output.S3Uri,  # Use processed data from S3
        'validation': 's3://crfsafedocs/training-data/validation.csv'  # Replace with your validation data S3 URI
    }
)

# Define the pipeline with the steps
pipeline = Pipeline(
    name='SafeDocsPipeline',
    steps=[processing_step, training_step]
)

# Execute the pipeline creation or update
if __name__ == "__main__":
    pipeline.upsert(role_arn=role)
    print(f"Pipeline '{pipeline.name}' successfully created or updated.")
