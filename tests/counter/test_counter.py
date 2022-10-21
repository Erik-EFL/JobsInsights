from src.counter import count_ocurrences


def test_counter():
    path = "src/jobs.csv"
    word = ["python", "PYTHON", "javascript", "JAVAscript"]
    expected_results = [1639, 1639, 122, 122]

    for index in range(len(word)):
        count = count_ocurrences(path, word[index])
        assert count == expected_results[index]
