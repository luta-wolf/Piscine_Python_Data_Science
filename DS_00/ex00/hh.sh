#!/bin/sh
curl -s -G "https://api.hh.ru/vacancies?text=${1/ /+}&per_page=20" | jq > hh.json
