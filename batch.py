from typing import Any, Callable, List, Tuple
import cyaron as cy

from .problem import Problem


class Batch:
    def __init__(self, problem: Problem, batch_size: int):
        self.problem = problem
        self.batch_size = batch_size

    def __call__(self, func: Callable[[cy.IO], None]) -> Callable:
        if self.problem.data_num * self.batch_size % 100 != 0:
            raise ValueError(
                "The percentage of data generated should be an integer."
                "Please adjust the batch size."
            )

        for _ in range(self.batch_size * self.problem.data_num // 100):
            self.problem.data_id_cnt += 1
            io = cy.IO(
                file_prefix=self.problem.data_path + self.problem.name,
                data_id=self.problem.data_id_cnt,
            )
            func(io)
            print(
                "Generated data for problem",
                self.problem.name,
                "with data_id",
                self.problem.data_id_cnt,
            )

        def wrapper(*args, **kwargs):
            print(
                "You should not call this function directly. Use the decorator `Batch` instead."
            )

        return wrapper
