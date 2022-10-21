from src.sorting import sort_by
from src.jobs import read
from src.insights import get_max_salary, get_min_salary


def test_sort_by_criteria():
    path = "src/jobs.csv"
    get_all_jobs = read(path)

    sort_by(get_all_jobs, "min_salary")
    excepted = get_min_salary(path)
    result = get_all_jobs[0]["min_salary"]
    assert result == str(excepted)

    sort_by(get_all_jobs, "max_salary")
    excepted = get_max_salary(path)
    result = get_all_jobs[0]["max_salary"]
    assert result == str(excepted)
