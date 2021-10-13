import json


def make_query_string_from_grouped_params(grouped_params):
    key_values = (
        f'{param_key}={param_value}'
        for param_key, param_values in grouped_params.items()
        for param_value in param_values
    )
    return '&'.join(key_values)


def make_query_string_from_event(event):
    grouped_params =  event.get('multiValueQueryStringParameters', {})
    return make_query_string_from_grouped_params(grouped_params)


def handler(event, context):
    query_string = make_query_string_from_event(event)
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': f'?{query_string}'
    }
