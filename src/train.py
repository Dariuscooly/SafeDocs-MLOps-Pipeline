import sagemaker
from sagemaker.estimator import Estimator

# Define your estimator
estimator = Estimator(
    image_uri='...',
    role='AmazonSageMaker-ExecutionRole-20240727T164373',
    instance_count=1,
    instance_type='ml.m5.xlarge'
)

# Train the model
estimator.fit({'train': 's3://your-bucket/path/to/data'})
