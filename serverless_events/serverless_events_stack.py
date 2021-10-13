from aws_cdk import aws_lambda
from aws_cdk import aws_apigateway
from aws_cdk import core as cdk

from aws_solutions_constructs import aws_apigateway_lambda

from aws_cdk.aws_lambda_python import PythonFunction


class ServerlessEventsStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        pyf = PythonFunction(
            self,
            "ApiGatewayToLambdaLambdaFunction",
            entry="serverless_events/lambda/", # required
            index="test.py", # optional, defaults to 'index.py'
            runtime=aws_lambda.Runtime.PYTHON_3_8
        )

        aws_apigateway_lambda.ApiGatewayToLambda(
            self,
            'ApiGatewayToLambda',
            existing_lambda_obj=pyf,
            api_gateway_props=aws_apigateway.RestApiProps(
                default_method_options=aws_apigateway.MethodOptions(
                    authorization_type=aws_apigateway.AuthorizationType.NONE,
                )
            )
        )
