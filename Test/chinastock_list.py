#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Test.TushareProApi
from Test.TushareProApi import GetdatlyfromCname
from Test.TushareProApi import Getconcept_detail
from Test.TushareProApi import Getdailyfromconcept
from Test.TushareProApi import moneyflowlist
import Test.QyptTableView
from Test.QyptTableView import Dataframdatashow
from Test.TushareProApi import trade_cal
from Test.TushareProApi import trade_cal_list
from Test.TushareProApi import hk_daily
from Test.TushareProApi import GetAlltscode
from Test.TushareProApi import Getdailyfromtscode
from Test.TushareProApi import hk_hold
from Test.TushareProApi import index_classify
from Test.TushareProApi import index_member
import pandas as pd

show = True
show_func = print if show else lambda a: a

index_classify_L1=index_classify('L1')
index_classify_L2=index_classify('L2')
index_classify_L3=index_classify('L3')
index_classify = pd.DataFrame()
# index_classify = pd.concat(index_classify_L1

show_func(index_classify_L3.head(),index_classify_L2.head(),index_classify_L1.head())

# show_func(index_classify.head())

