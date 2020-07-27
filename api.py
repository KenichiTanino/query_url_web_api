#!/usr/bin/env python

from fastapi import FastAPI, Query
from urllib.parse import urlencode

app = FastAPI()

inner_keyword = {
    'R': 'ラーメン',
    'G': '行政書士',
}

@app.get("/query/{key}")
async def queryurl(key: str, q: str = Query('', max_length=250)):
    """
    クエリURL 生成API:

    - **key**: 固定の内部キーワードを指定する
    - **q**: 任意のキーワードを指定する
    \f
    :param queryURL: キーワード検索URL.
    """
    search_keyword = inner_keyword.get(key, '') + " " + q
    path_keyword = urlencode({'q': search_keyword})
    query_url = f"https://www.google.com/search?{path_keyword}"
    return {"queryURL": query_url}