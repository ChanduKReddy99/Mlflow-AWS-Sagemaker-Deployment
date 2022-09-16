import mlflow.sagemaker as mfs

experiment_id= '1'
run_id= '555f63666d294dec9daaa9f39a009246'
region= 'us-east-1'
aws_id= '374664354934'
arn= 'arn:aws:iam::374664354934:role/mlflow-roles'
app_name= 'test-app'
model_uri= f'mlruns/{experiment_id}/{run_id}/artifacts/random-forest-model'
tag_id= '1.26.1'
image_url= aws_id + '.dkr.ecr.' +region + '.amazonaws.com/mlflow-pyfunc:'+ tag_id

mfs.deploy(app_name,
        model_uri= model_uri,
        region_name= region,
        mode= 'create',
        execution_role_arn= arn,
        image_url=image_url,
    )