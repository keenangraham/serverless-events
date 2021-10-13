import json
import requests


BASE_URL = 'https://data-service.demo.regulomedb.org/rnaget/expressions/bytes'

HEADERS_TO_DROP = [
    'Content-Encoding',
    'Content-Length',
    'Transfer-Encoding',
    'Connection'
]


def make_query_string_from_grouped_params(grouped_params):
    key_values = (
        f'{param_key}={param_value}'
        for param_key, param_values in grouped_params.items()
        for param_value in param_values
    )
    return '&'.join(key_values)


def make_query_string_from_event(event):
    grouped_params =  event.get('multiValueQueryStringParameters') or {}
    return make_query_string_from_grouped_params(grouped_params)


def maybe_add_query_string(base_url, query_string):
    url = base_url
    if query_string:
        url += f'?{query_string}'
    return url


def safe_headers(headers):
    return {
        k: v
        for k, v in headers.items()
        if k not in HEADERS_TO_DROP
    }


def handler(event, context):
    query_string = make_query_string_from_event(event)
    url = maybe_add_query_string(BASE_URL, query_string)
    r = requests.get(url)
    return {
        'statusCode': r.status_code,
        'headers': safe_headers(r.headers),
        'body': r.content.decode('utf-8'),
    }
