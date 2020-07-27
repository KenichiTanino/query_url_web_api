name = "gunicorn"

accesslog = "/usr/local/queryurl/log/log_access.txt"
errorlog = "/usr/local/queryurl/log/log_error.txt"
access-logformat = "{'remote_ip':'%(h)s','request_id':'%({X-Request-Id}i)s','response_code':'%(s)s','request_method':'%(m)s','request_path':'%(U)s','request_querystring':'%(q)s','request_timetaken':'%(D)s','response_length':'%(B)s'}"

bind = "127.0.0.1:28168"

worker_class = "uvicorn.workers.UvicornWorker"
workers = multiprocessing.cpu_count() * 2 + 1
worker_connections = 1024
backlog = 2048
max_requests = 5120
timeout = 360
keepalive = 2

debug = os.environ.get("DEBUG", "false") == "true"
reload = debug
preload_app = False
daemon = False
