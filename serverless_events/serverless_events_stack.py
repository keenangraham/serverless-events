from aws_cdk import aws_lambda
from aws_cdk import aws_apigateway
from aws_cdk import core as cdk

from aws_solutions_constructs import aws_apigateway_lambda


class ServerlessEventsStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        aws_apigateway_lambda.ApiGatewayToLambda(
            self,
            'ApiGatewayToLambda',
            lambda_function_props=aws_lambda.FunctionProps(
                runtime=aws_lambda.Runtime.PYTHON_3_8,
                code=aws_lambda.Code.asset('serverless_events/lambda/'),
                handler='test.handler',
            ),
            api_gateway_props=aws_apigateway.RestApiProps(
                default_method_options=aws_apigateway.MethodOptions(
                    authorization_type=aws_apigateway.AuthorizationType.NONE,
                )
            )
        )
