#!/usr/bin/env python3
# encoding: UTF-8

import pytest
from src import *
import pandas as pd

relation1 = Relation(pd.read_csv("ENROLL.csv"))
relation2 = Relation(pd.read_csv("STUDENT.csv"))

def test_join():
    assert relation1.join(relation2, "StudentId", "SId") == Relation(pd.read_csv("JOIN.csv"))

def test_sort():
    assert relation1.sort(["SName"]) == Relation(pd.read_csv("SORT.csv"))

