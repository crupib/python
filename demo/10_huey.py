from huey import RedisHuey, crontab

huey = RedisHuey("my-app", host="localhost")


@huey.task()
def add_numbers(a, b):
    return a + b


@huey.task(retries=2, retry_delay=60)
def flaky_task(url):
    return this_might_fail(url)


@huey.periodic_task(crontab(minute="0", hour="3"))
def nightly_backup():
    sync_all_data()


flaky_task("www.gaggle.com")
