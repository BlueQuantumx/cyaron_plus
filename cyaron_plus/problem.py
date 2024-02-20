class Problem:
    def __init__(self, name, data_path: str, data_num: int):
        self.name = name
        self.data_path = data_path
        self.data_num = data_num

        self.data_id_cnt = 0

    def __del__(self):
        if self.data_id_cnt != self.data_num:
            print(
                f"Warning: Problem '{self.name}': The number of data generated is not equal to the data_num."
            )
