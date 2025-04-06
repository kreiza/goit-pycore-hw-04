def total_salary(path: str) -> tuple:
    """
    Analyze a text file with developer salaries and return total and average salary.

    :param path: The path to the text file containing developer salaries in the format "Surname,Salary".
    :return: A tuple (total_salary, average_salary) as integers.
    :raises FileNotFoundError: If the file specified by path does not exist.
    """
    total = 0
    count = 0
    try:
        with open(path, encoding="utf-8") as file:
            for line in file:
                if line.strip():
                    _, salary = line.strip().split(",")
                    total += int(salary)
                    count += 1
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found: {path}") from e
    average = total // count if count > 0 else 0
    return total, average


def get_cats_info(path: str) -> list:
    """
    Read a text file with cat information and return a list of dictionaries.

    :param path: The path to the text file containing cat data in the format "id,name,age" per line.
    :return: A list of dictionaries, each with keys "id", "name", and "age".
    :raises FileNotFoundError: If the file specified by path does not exist.
    """
    cats = []
    try:
        with open(path, encoding="utf-8") as file:
            for line in file:
                if line.strip():
                    cat_id, name, age = line.strip().split(",")
                    cats.append({"id": cat_id, "name": name, "age": age})
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found: {path}") from e
    return cats
