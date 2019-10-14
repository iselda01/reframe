#!/usr/bin/env python3
# encoding: UTF-8

import pytest
import pandas as pd
from reframe import Relation

relation1 = Relation(pd.read_csv("ENROLL.csv"))
relation2 = Relation(pd.read_csv("STUDENT.csv"))

def test_join():
    assert relation1.join(relation2, "StudentId = StudentId").equals(Relation(pd.read_csv("JOIN.csv")))

def test_join_no_columns():
    assert relation1.join(relation2).equals(Relation(pd.read_csv("JOIN.csv")))


def test_sort():
    assert relation2.sort(["SName"]).reset_index().drop(columns=["index"]).equals(Relation(pd.read_csv("SORT.csv")))

