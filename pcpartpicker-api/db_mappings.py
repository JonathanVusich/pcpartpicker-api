from sqlalchemy import Table, Column, Integer, Boolean, String, ForeignKey
from sqlalchemy.orm import registry
from sqlalchemy import func
from sqlalchemy.types import UserDefinedType

from pcpartpicker.parts import CPU, CPUCooler, Motherboard

mapper_registry = registry()


cpu_table = Table(
    'cpu',
    mapper_registry.metadata,
    Column('brand', String),
    Column('model', String),
    Column('cores', Integer),
    Column('base_clock', Integer),
    Column('boost_clock', Integer),
    Column('tdp', Integer),
    Column('integrated_graphics', String),
    Column('multithreading', Boolean),
    Column('price', ForeignKey('money.id'))
)

cpu_cooler_table = Table(
    'cpu_cooler',
    mapper_registry.metadata,
    Column('brand', String),
    Column('model', String),
    Column('fan_rpm', ForeignKey('rpm.id')),
    Column('decibels', ForeignKey('decibel.id')),
    Column('color', String),
    Column('radiator_size', Integer),
    Column('price', ForeignKey('money.id'))
)

motherboard_table = Table(
    'motherboard',
    mapper_registry.metadata,
    Column('brand', String),
    Column('model', String),
    Column('socket', String),
    Column('form_factor', String),
    Column('ram_slots', Integer),
    Column('max_ram', Integer),
    Column('color', String)
)

mapper_registry.map_imperatively(CPU, cpu_table)
mapper_registry.map_imperatively(CPUCooler, cpu_cooler_table)
