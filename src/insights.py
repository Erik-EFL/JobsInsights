from src.jobs import read

def get_unique_job_types(path):
    get_all_jobs = read(path)
    job_types = set()

    for job in get_all_jobs:
        if job["job_type"] is not None:
            job_types.add(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    filter_jobs = []

    for job in jobs:
        if job["job_type"] == job_type:
            filter_jobs.append(job)
    return filter_jobs

def get_unique_industries(path):
    get_all_jobs = read(path)
    get_industrie = set()

    for job in get_all_jobs:
        if job["industry"] != '':
            get_industrie.add(job["industry"])
    return get_industrie


def filter_by_industry(jobs, industry):
    filter_jobs = []

    for job in jobs:
        if job["industry"] == industry:
            filter_jobs.append(job)
    return filter_jobs


def get_max_salary(path):
    get_all_jobs = read(path)
    max_salary = []
    for job in get_all_jobs:
        if job["max_salary"].isdigit():
            max_salary.append(int(job["max_salary"]))
    return max(max_salary)


def get_min_salary(path):
    get_all_jobs = read(path)
    min_salary = []
    for job in get_all_jobs:
        if job["min_salary"].isdigit():
            min_salary.append(int(job["min_salary"]))
    return min(min_salary)


def matches_salary_range(job, salary):
    if (
        job.get("min_salary") is None
        or job.get("max_salary") is None
        or type(job.get("min_salary")) is not int
        or type(job.get("max_salary")) is not int
        or type(salary) is not int
        or job["min_salary"] > job["max_salary"]
    ):
        raise ValueError

    return job["min_salary"] <= salary <= job["max_salary"]

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    filter_jobs = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filter_jobs.append(job)
        except ValueError:
            print("ERROR: incorrect value type or data checked")
    return filter_jobs
