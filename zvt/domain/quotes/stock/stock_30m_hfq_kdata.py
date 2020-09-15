# -*- coding: utf-8 -*-
# this file is generated by gen_kdata_schema function, dont't change it
from sqlalchemy.ext.declarative import declarative_base

from zvt.contract.register import register_schema
from zvt.domain.quotes import StockKdataCommon
from zvt.contract.common import Region, Provider

KdataBase = declarative_base()


class Stock30mHfqKdata(KdataBase, StockKdataCommon):
    __tablename__ = 'stock_30m_hfq_kdata'


register_schema(regions=[Region.CHN, Region.US], 
                providers=[Provider.JoinQuant, Provider.Yahoo], 
                db_name='stock_30m_hfq_kdata', schema_base=KdataBase)

__all__ = ['Stock30mHfqKdata']
