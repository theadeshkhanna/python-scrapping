from retrying import retry

@retry(wait_fixed=2000, stop_max_attempt_number=3)
def retry_request(func, *args, **kwargs):
    return func(*args, **kwargs)

