from moneyed import Money
from pcpartpicker.parts import Bytes, ClockSpeed, NetworkSpeed, RPM, Decibels, CFM, Resolution, FrequencyResponse
from pcpartpicker.parts import CPU, CPUCooler, Motherboard, Memory, StorageDrive, GPU, PSU, \
    Case, Fan, FanController, ThermalPaste, OpticalDrive, SoundCard, EthernetCard, WirelessCard, \
    Monitor, ExternalHDD, Headphones, Keyboard, Mouse, Speakers, UPS
from sqlalchemy import Table, Column, Integer, Boolean, String, ForeignKey, TypeDecorator, Numeric
from sqlalchemy import create_engine
from sqlalchemy.orm import registry, relationship
from sqlalchemy.orm import sessionmaker, Session


class Database:

    def __init__(self, database: str):
        self._engine = create_engine(database, echo=True)
        self._session_creator = sessionmaker(bind=self._engine)

    def create_session(self) -> Session:
        return self._session_creator()


class ByteType(TypeDecorator):
    impl = Integer

    def process_bind_param(self, value: Bytes, dialect) -> int:
        return value.total

    def process_result_value(self, value: int, dialect) -> Bytes:
        return Bytes(value)


class ClockSpeedType(TypeDecorator):
    impl = Integer

    def process_bind_param(self, value: ClockSpeed, dialect) -> int:
        return value.cycles

    def process_result_value(self, value: int, dialect) -> ClockSpeed:
        return ClockSpeed(value)


class NetworkSpeedType(TypeDecorator):
    impl = Integer

    def process_bind_param(self, value: NetworkSpeed, dialect) -> int:
        return value.bits_per_second

    def process_result_value(self, value: int, dialect) -> NetworkSpeed:
        return NetworkSpeed(value)


mapper_registry = registry()

money_table = Table(
    'price',
    mapper_registry.metadata,
    Column('id', Integer, primary_key=True),
    Column('amount', Numeric),
    Column('currency', String)
)

rpm_table = Table(
    'rpm',
    mapper_registry.metadata,
    Column('id', Integer, primary_key=True),
    Column('min', Numeric),
    Column('max', Numeric),
    Column('default', Numeric)
)

decibel_table = Table(
    'decibel',
    mapper_registry.metadata,
    Column('id', Integer, primary_key=True),
    Column('min', Numeric),
    Column('max', Numeric),
    Column('default', Numeric)
)

cfm_table = Table(
    'cfm',
    mapper_registry.metadata,
    Column('id', Integer, primary_key=True),
    Column('min', Numeric),
    Column('max', Numeric),
    Column('default', Numeric)
)

resolution_table = Table(
    'resolution',
    mapper_registry.metadata,
    Column('id', Integer, primary_key=True),
    Column('width', Integer),
    Column('height', Integer)
)

frequency_response = Table(
    'frequency_response',
    mapper_registry.metadata,
    Column('id', Integer, primary_key=True),
    Column('min', Numeric),
    Column('max', Numeric),
    Column('default', Numeric)
)

cpu_table = Table(
    'cpu',
    mapper_registry.metadata,
    Column('brand', String),
    Column('model', String),
    Column('cores', Integer),
    Column('base_clock', ClockSpeedType),
    Column('boost_clock', ClockSpeedType),
    Column('tdp', Integer),
    Column('integrated_graphics', String),
    Column('multithreading', Boolean),
    Column('price_id', ForeignKey('price.id'))
)

cpu_cooler_table = Table(
    'cpu_cooler',
    mapper_registry.metadata,
    Column('brand', String),
    Column('model', String),
    Column('fan_rpm_id', ForeignKey('rpm.id')),
    Column('decibels_id', ForeignKey('decibel.id')),
    Column('color', String),
    Column('radiator_size', Integer),
    Column('price_id', ForeignKey('price.id'))
)

motherboard_table = Table(
    'motherboard',
    mapper_registry.metadata,
    Column('brand', String),
    Column('model', String),
    Column('socket', String),
    Column('form_factor', String),
    Column('ram_slots', Integer),
    Column('max_ram', ByteType),
    Column('color', String),
    Column('price_id', ForeignKey('price.id'))
)

memory_table = Table(
    'memory',
    mapper_registry.metadata,
    Column('brand', String),
    Column('model', String),
    Column('module_type', String),
    Column('speed', ClockSpeedType),
    Column('number_of_modules', Integer),
    Column('module_size', ByteType),
    Column('price_per_gb_id', ForeignKey('price.id')),
    Column('color', String),
    Column('first_word_latency', Numeric),
    Column('cas_timing', Integer),
    Column('error_correction', String),
    Column('price_id', ForeignKey('price.id'))
)

storage_table = Table(
    'storage',
    mapper_registry.metadata,
    Column('brand', String),
    Column('model', String),
    Column('capacity', ByteType),
    Column('price_per_gb_id', ForeignKey('price.id')),
    Column('storage_type', String),
    Column('platter_rpm', Integer),
    Column('cache_amount', ByteType),
    Column('form_factor', String),
    Column('interface', String),
    Column('price_id', ForeignKey('price.id'))
)

gpu_table = Table(
    'gpu',
    mapper_registry.metadata,
    Column('brand', String),
    Column('model', String),
    Column('chipset', String),
    Column('vram', ByteType),
    Column('core_clock', ClockSpeedType),
    Column('boost_clock', ClockSpeedType),
    Column('color', String),
    Column('length', Numeric),
    Column('price_id', ForeignKey('price.id'))
)

psu_table = Table(
    'psu',
    mapper_registry.metadata,
    Column('brand', String),
    Column('model', String),
    Column('form_factor', String),
    Column('efficiency_rating', String),
    Column('wattage', Integer),
    Column('modular', String),
    Column('color', String),
    Column('price_id', ForeignKey('price.id'))
)

case_table = Table(
    'case',
    mapper_registry.metadata,
    Column('brand', String),
    Column('model', String),
    Column('form_factor', String),
    Column('color', String),
    Column('psu_wattage', Integer),
    Column('side_panel', Boolean),
    Column('external_bays', Integer),
    Column('internal_bays', Integer),
    Column('price_id', ForeignKey('price.id'))
)

fan_table = Table(
    'fan',
    mapper_registry.metadata,
    Column('brand', String),
    Column('model', String),
    Column('size', Integer),
    Column('color', String),
    Column('rpm_id', ForeignKey('rpm.id')),
    Column('airflow_id', ForeignKey('cfm.id')),
    Column('decibels_id', ForeignKey('decibel.id')),
    Column('pwm', Boolean),
    Column('price_id', ForeignKey('price.id'))
)

fan_controller_table = Table(
    'fan_controller',
    mapper_registry.metadata,
    Column('brand', String),
    Column('model', String),
    Column('channels', Integer),
    Column('channel_wattage', Integer),
    Column('pwm', Boolean),
    Column('form_factor', String),
    Column('color', String),
    Column('price_id', ForeignKey('price.id'))
)

thermal_paste_table = Table(
    'thermal_paste',
    mapper_registry.metadata,
    Column('brand', String),
    Column('model', String),
    Column('amount', Numeric),
    Column('price_id', ForeignKey('price.id'))
)

optical_drive_table = Table(
    'optical_drive',
    mapper_registry.metadata,
    Column('brand', String),
    Column('model', String),
    Column('bluray_read_speed', Integer),
    Column('dvd_read_speed', Integer),
    Column('cd_read_speed', Integer),
    Column('bluray_write_speed', Integer),
    Column('dvd_write_speed', Integer),
    Column('cd_write_speed', Integer),
    Column('price_id', ForeignKey('price.id'))
)

soundcard_table = Table(
    'soundcard',
    mapper_registry.metadata,
    Column('brand', String),
    Column('model', String),
    Column('channels', Numeric),
    Column('bitrate', Integer),
    Column('snr', Integer),
    Column('sample_rate', Numeric),
    Column('chipset', String),
    Column('interface', String),
    Column('price_id', ForeignKey('price.id'))
)

ethernet_card_table = Table(
    'ethernet_card',
    mapper_registry.metadata,
    Column('brand', String),
    Column('model', String),
    Column('interface', String),
    Column('port_speed', NetworkSpeedType),
    Column('port_number', Integer),
    Column('color', String),
    Column('price_id', ForeignKey('price.id'))
)

wireless_card_table = Table(
    'wireless_card',
    mapper_registry.metadata,
    Column('brand', String),
    Column('model', String),
    Column('supported_protocols', String),
    Column('interface', String),
    Column('color', String),
    Column('price_id', ForeignKey('price.id'))
)

monitor_table = Table(
    'monitor',
    mapper_registry.metadata,
    Column('brand', String),
    Column('model', String),
    Column('size', Numeric),
    Column('resolution_id', ForeignKey('resolution.id')),
    Column('refresh_rate', Integer),
    Column('response_time', Numeric),
    Column('panel_type', String),
    Column('aspect_ratio', String),
    Column('price_id', ForeignKey('price.id'))
)

external_hdd_table = Table(
    'external_hdd',
    mapper_registry.metadata,
    Column('brand', String),
    Column('model', String),
    Column('type', String),
    Column('interface', String),
    Column('capacity', ByteType),
    Column('price_per_gb_id', ForeignKey('price.id')),
    Column('color', String),
    Column('price_id', ForeignKey('price.id'))
)

headphones_table = Table(
    'headphones',
    mapper_registry.metadata,
    Column('brand', String),
    Column('model', String),
    Column('form_factor', String),
    Column('frequency_response_id', ForeignKey("frequency_response.id")),
    Column('has_microphone', Boolean),
    Column('is_wireless', Boolean),
    Column('type', String),
    Column('color', String),
    Column('price_id', ForeignKey('price.id'))
)

keyboard_table = Table(
    'keyboard',
    mapper_registry.metadata,
    Column('brand', String),
    Column('model', String),
    Column('style', String),
    Column('switches', String),
    Column('backlight', String),
    Column('tenkeyless', Boolean),
    Column('connection', String),
    Column('color', String),
    Column('price_id', ForeignKey('price.id'))
)

mouse_table = Table(
    'mouse',
    mapper_registry.metadata,
    Column('brand', String),
    Column('model', String),
    Column('tracking', String),
    Column('connection', String),
    Column('max_dpi', Integer),
    Column('hand_orientation', String),
    Column('color', String),
    Column('price_id', ForeignKey('price.id'))
)

speakers_table = Table(
    'speakers',
    mapper_registry.metadata,
    Column('brand', String),
    Column('model', String),
    Column('channel_configuration', Numeric),
    Column('wattage', Numeric),
    Column('frequency_response_id', ForeignKey('frequency_response.id')),
    Column('color', String),
    Column('price_id', ForeignKey('price.id'))
)

ups_table = Table(
    'ups',
    mapper_registry.metadata,
    Column('brand', String),
    Column('model', String),
    Column('watt_capacity', Integer),
    Column('va_capacity', Integer),
    Column('price_id', ForeignKey('price.id'))
)
mapper_registry.map_imperatively(Money, money_table)
mapper_registry.map_imperatively(RPM, rpm_table)
mapper_registry.map_imperatively(Decibels, decibel_table)
mapper_registry.map_imperatively(CFM, cfm_table)
mapper_registry.map_imperatively(Resolution, resolution_table)

mapper_registry.map_imperatively(FrequencyResponse, frequency_response)
mapper_registry.map_imperatively(CPU, cpu_table, properties={
    'price': relationship(Money)
})
mapper_registry.map_imperatively(CPUCooler, cpu_cooler_table, properties={
    'fan_rpm': relationship(RPM),
    'decibels': relationship(Decibels),
    'price': relationship(Money)
})
mapper_registry.map_imperatively(Motherboard, motherboard_table, properties={
    'price': relationship(Money),
})
mapper_registry.map_imperatively(Memory, memory_table, properties={
    'price_per_gb': relationship(Money),
    'price': relationship(Money)
})
mapper_registry.map_imperatively(StorageDrive, storage_table, properties={
    'price_per_gb': relationship(Money),
    'price': relationship(Money)
})
mapper_registry.map_imperatively(GPU, gpu_table, properties={
    'price': relationship(Money)
})
mapper_registry.map_imperatively(PSU, psu_table, properties={
    'price': relationship(Money)
})
mapper_registry.map_imperatively(Case, case_table, properties={
    'price': relationship(Money)
})
mapper_registry.map_imperatively(Fan, fan_table, properties={
    'rpm': relationship(RPM),
    'airflow': relationship(CFM),
    'decibels': relationship(Decibels),
    'price': relationship(Money)
})
mapper_registry.map_imperatively(FanController, fan_controller_table, properties={
    'price': relationship(Money)
})
mapper_registry.map_imperatively(ThermalPaste, thermal_paste_table, properties={
    'price': relationship(Money)
})
mapper_registry.map_imperatively(OpticalDrive, optical_drive_table, properties={
    'price': relationship(Money)
})
mapper_registry.map_imperatively(SoundCard, soundcard_table, properties={
    'price': relationship(Money)
})
mapper_registry.map_imperatively(EthernetCard, ethernet_card_table, properties={
    'price': relationship(Money)
})
mapper_registry.map_imperatively(WirelessCard, wireless_card_table, properties={
    'price': relationship(Money)
})
mapper_registry.map_imperatively(Monitor, monitor_table, properties={
    'resolution': relationship(Resolution),
    'price': relationship(Money)
})
mapper_registry.map_imperatively(ExternalHDD, external_hdd_table, properties={
    'price_per_gb': relationship(Money),
    'price': relationship(Money)
})
mapper_registry.map_imperatively(Headphones, headphones_table, properties={
    'frequency_response': relationship(FrequencyResponse),
    'price': relationship(Money)
})
mapper_registry.map_imperatively(Keyboard, keyboard_table, properties={
    'price': relationship(Money)
})
mapper_registry.map_imperatively(Mouse, mouse_table, properties={
    'price': relationship(Money)
})
mapper_registry.map_imperatively(Speakers, speakers_table, properties={
    'frequency_response': relationship(FrequencyResponse),
    'price': relationship(Money)
})

mapper_registry.map_imperatively(UPS, ups_table, properties={
    'price': relationship(Money)
})
