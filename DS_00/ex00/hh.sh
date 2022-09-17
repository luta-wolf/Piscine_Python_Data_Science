#!/bin/sh

# -H запись
curl -k -H 'User-Agent: api-test-agent' 'https://api.hh.ru/vacancies?text='"${1// /+}"'&per_page=20' | jq '.' > hh.json
