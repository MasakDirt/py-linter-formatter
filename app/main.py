def format_linter_error(error: dict) -> dict:
    return {
        "column": error["column_number"], "line": error["line_number"],
        "message": error["text"], "name": error["code"], "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [
            {
                "line": error["line_number"],
                "column": error["column_number"],
                "message": error["text"],
                "name": error["code"],
                "source": "flake8"
            } for error in errors
        ],
        "path": file_path, "status": "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors": [] if len(linter_report[reports]) == 0 else [
                {
                    "line": error["line_number"],
                    "column": error["column_number"],
                    "message": error["text"],
                    "name": error["code"],
                    "source": "flake8"
                }
                for error in linter_report[reports]
            ],
            "path": reports,
            "status": "passed" if len(linter_report[reports]) == 0
            else "failed"
        }
        for reports in linter_report
    ]
