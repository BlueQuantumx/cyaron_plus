import random

from cyaron import IO, Sequence, String, Graph, Edge, Vector, randint
from cyaron.utils import ati

from cyaron_plus import Batch, Problem

problem_arrange = Problem(name="arrange", data_path="./examples/arrange/", data_num=10)


@Batch(problem_arrange, 10)
def arrange_data1(testdata: IO):
    n = 10
    m = 100

    testdata.input_writeln(n, m)

    testdata.output_gen("/tmp/CodeTmp/Executable")


@Batch(problem_arrange, 20)
def arrange_data2(testdata: IO):
    n = 10
    m = 20000

    testdata.input_writeln(n, m)

    testdata.output_gen("/tmp/CodeTmp/Executable")


@Batch(problem_arrange, 70)
def arrange_data3(testdata: IO):
    n = 100
    m = 20000

    testdata.input_writeln(n, m)

    testdata.output_gen("/tmp/CodeTmp/Executable")
