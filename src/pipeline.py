from sagemaker.workflow.pipeline import Pipeline
from sagemaker.workflow.steps import ProcessingStep, TrainingStep
from sagemaker.workflow.pipeline_context import PipelineSession
from sagemaker.sklearn.processing import SKLearnProcessor

pipeline_session = PipelineSession()

sklearn_processor = SKLearnProcessor(
    framework_version='0.23-1',
    role='AmazonSageMaker-ExecutionRole-20240727T164373',
    instance_type='ml.m5.xlarge',
    instance_count=1
)

processing_step = ProcessingStep(
    name='DataProcessing',
    processor=sklearn_processor,
    inputs=[...],
    outputs=[...]
)

training_step = TrainingStep(
    name='ModelTraining',
    estimator=...,
    inputs=...
)

pipeline = Pipeline(
    name='SafeDocsPipeline',
    steps=[processing_step, training_step, ...]
)

if __name__ == "__main__":
    pipeline.upsert(role_arn='AmazonSageMaker-ExecutionRole-20240727T164373')
