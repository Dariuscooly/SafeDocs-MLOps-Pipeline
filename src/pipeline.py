from sagemaker.estimator import Estimator
from sagemaker.workflow.steps import TrainingStep, ProcessingStep
from sagemaker.workflow.pipeline import Pipeline
from sagemaker.workflow.pipeline_context import PipelineSession
from sagemaker.sklearn.processing import SKLearnProcessor
import sagemaker

# Create a pipeline session
pipeline_session = PipelineSession()

# Define the IAM role for SageMaker
role = 'YourSageMakerRole'  # Replace with your IAM role ARN

# Define the Estimator
estimator = Estimator(
    image_uri='your-image-uri',  # Replace with the appropriate Docker image URI
    role=role,
    instance_count=1,
    instance_type='ml.m5.xlarge',
    entry_point='train.py',      # The entry point script for training
    source_dir='src/',           # Directory containing your training script
    output_path='s3://your-bucket/path/to/output',  # S3 location for model artifacts
    hyperparameters={
        'learning_rate': 0.001,
        'batch_size': 32
    }
)

# Define the processing step (if needed)
sklearn_processor = SKLearnProcessor(
    framework_version='0.23-1',
    role=role,
    instance_type='ml.m5.xlarge',
    instance_count=1
)

processing_step = ProcessingStep(
    name='DataProcessing',
    processor=sklearn_processor,
    inputs=[...],  # Replace with actual inputs
    outputs=[...]  # Replace with actual outputs
)

# Define the TrainingStep
training_step = TrainingStep(
    name='ModelTraining',
    estimator=estimator,
    inputs={
        'train': 's3://your-bucket/path/to/training/data',
        'validation': 's3://your-bucket/path/to/validation/data'
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
