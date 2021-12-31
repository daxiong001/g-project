# coding: utf-8
from sqlalchemy import Column, DECIMAL, Date, DateTime, Index, String, TIMESTAMP, Table, Text, Time, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, TIMESTAMP, TINYINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class BBaseAppVersion(Base):
    __tablename__ = 'b_base_app_version'
    __table_args__ = {'comment': 'app版本信息表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    version_type = Column(TINYINT(4), nullable=False, server_default=text("'0'"), comment='#版本类型#ENUM#0:历史版本,1:当前版本#')
    version_number = Column(String(10), nullable=False, comment='#版本号#')
    business_type = Column(TINYINT(4), comment='#业务类型#ENUM#0:crm:crmapp,1:CLIENT:客户端app,2:MERCHANT:商户端app#')
    operating_system = Column(TINYINT(4), nullable=False, comment='#操作系统#ENUM#0:android,1:ios#')
    upgrade_way = Column(TINYINT(4), nullable=False, server_default=text("'0'"), comment='#升级方式#ENUM#0:咨询升级,1:强制升级#')
    upgrade_time = Column(DateTime, nullable=False, comment='#升级时间#')
    upgrade_url = Column(String(500), comment='#升级地址#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    modifier = Column(String(25), server_default=text("''"), comment='修改人')
    update_time = Column(DateTime, comment='修改时间')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='逻辑删除#ENUM#0:正常,1:删除')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')


class BBaseArea(Base):
    __tablename__ = 'b_base_area'
    __table_args__ = {'comment': '区域表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    parent_id = Column(BIGINT(20), nullable=False, comment='#父级id#')
    parent_code = Column(String(50), comment='#父级编码#')
    code = Column(VARCHAR(50), nullable=False, comment='#编码#')
    name = Column(VARCHAR(100), nullable=False, comment='#名称#')
    level = Column(TINYINT(4), nullable=False, comment='#等级#ENUM#1:省,2:市,3:区#')
    city_code = Column(String(10), comment='#城市区号#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BBaseCodeManage(Base):
    __tablename__ = 'b_base_code_manage'
    __table_args__ = {'comment': '编码管理'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    status = Column(TINYINT(4), nullable=False, comment='#启用状态#ENUM#1:启动,2:未启用#')
    function_module = Column(String(50), nullable=False, comment='#功能模块#')
    field_name = Column(String(50), nullable=False, comment='#字段名称#')
    prefix_num = Column(String(50), nullable=False, comment='#前缀编号#')
    date_type = Column(TINYINT(4), nullable=False, comment='#日期类型#')
    date_str = Column(String(50), comment='#日期字符串#')
    suffix_delimiter = Column(String(50), comment='#后缀分隔符#')
    suffix_digit = Column(INTEGER(11), nullable=False, comment='#后缀位数#')
    start_value = Column(INTEGER(11), nullable=False, comment='#起始值#')
    current_value = Column(INTEGER(11), comment='#当前值#')
    example = Column(String(50), comment='#示例#')
    version = Column(INTEGER(11), server_default=text("'1'"), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BBaseCost(Base):
    __tablename__ = 'b_base_cost'
    __table_args__ = {'comment': '商户费用基础表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    name = Column(String(100), comment='#费用条目#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BBaseDict(Base):
    __tablename__ = 'b_base_dict'
    __table_args__ = {'comment': '字典表'}

    id = Column(INTEGER(11), primary_key=True, comment='#主键ID#')
    name = Column(String(100), comment='#字典名称#')
    code = Column(String(50), comment='#字典code#')
    bussiness_type = Column(String(255), comment='#字典业务类型#')
    parent_code = Column(String(50), comment='#父节点#')
    sort = Column(INTEGER(5), comment='#排序#')
    remark = Column(String(100), comment='#描述#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BBaseFile(Base):
    __tablename__ = 'b_base_file'
    __table_args__ = (
        Index('biz_index', 'biz_id', 'biz_module'),
        {'comment': '附件记录表'}
    )

    id = Column(String(32), primary_key=True, comment='#主键#')
    file_id = Column(BIGINT(22), comment='#文件id#')
    file_name = Column(String(45), comment='#文件名称#')
    biz_id = Column(String(32), comment='#业务表id#')
    biz_module = Column(String(45), comment='#业务模块#')


class BBaseProces(Base):
    __tablename__ = 'b_base_process'
    __table_args__ = {'comment': '工作流程表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    pre_process_id = Column(BIGINT(20), comment='#上一个流程步骤id#')
    next_process_id = Column(BIGINT(20), comment='#下一个流程步骤id#')
    type = Column(TINYINT(4), comment='#类型#ENUM#0:商机审核流程#')
    step_type = Column(TINYINT(4), comment='#流程步骤类型#ENUM#0:开始,1:条件分支,2:结束#')
    approver_role = Column(BIGINT(20), comment='#审核人角色#')
    condition_branch = Column(String(500), comment='#条件分支（json结构{"value1":"processID1","value2":"processID2","value3":"processID3"}）#')


class BBaseProcessHistory(Base):
    __tablename__ = 'b_base_process_history'
    __table_args__ = {'comment': '工作流程历史表（快照）'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    ref_business_id = Column(BIGINT(20), comment='#关联的业务id#')
    pre_process_id = Column(BIGINT(20), comment='#上一个流程步骤id#')
    next_process_id = Column(BIGINT(20), comment='#下一个流程步骤id#')
    type = Column(TINYINT(4), comment='#类型#ENUM#0:商机审核流程#')
    step_type = Column(TINYINT(4), comment='#流程步骤类型#ENUM#0:开始,1:条件分支,2:结束#')
    step_status = Column(TINYINT(4), comment='#流程步骤状态#ENUM#0:未完成,1:已完成#')
    approver_role = Column(BIGINT(20), comment='#审核人角色#')
    approver_id = Column(BIGINT(20), comment='#审核人id#')
    condition_branch = Column(String(500), comment='#条件分支（json结构{"value1":"processID1","value2":"processID2","value3":"processID3"}）#')


class BBaseSubjectInfo(Base):
    __tablename__ = 'b_base_subject_info'
    __table_args__ = {'comment': '平台主体信息表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    name = Column(String(100), comment='#主体名称#')
    address = Column(String(100), comment='#通讯地址#')
    legal_person = Column(String(50), comment='#法定代表人#')
    unified_social_credit_code = Column(String(100), comment='#统一社会信用代码#')
    contacts = Column(String(50), comment='#联系人#')
    phone = Column(String(50), comment='#联系电话#')
    bank_name = Column(String(100), comment='#开户行#')
    bank_account = Column(String(100), comment='#开户行账号#')
    tx_id_num = Column(String(100), comment='#纳税人识别号#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BBillAccountDetail(Base):
    __tablename__ = 'b_bill_account_detail'

    id = Column(BIGINT(20), primary_key=True, comment='#主键ID#')
    account_id = Column(BIGINT(20), comment='#账户ID#')
    type = Column(TINYINT(4), comment='#收付款类型#')
    target_type = Column(TINYINT(4), comment='#单位类型#')
    target_name = Column(String(100), comment='#客商名称#')
    serial_no = Column(String(20), comment='#收付款单号#')
    account_type = Column(TINYINT(4), comment='#账号类型#')
    account_name = Column(String(100), comment='#账户名称#')
    receive_money = Column(DECIMAL(12, 2), comment='#流入金额#')
    pay_money = Column(DECIMAL(12, 2), comment='#流出金额#')
    money = Column(DECIMAL(12, 2), comment='#余额#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BBillBankAccount(Base):
    __tablename__ = 'b_bill_bank_account'
    __table_args__ = {'comment': '资金账户表'}

    id = Column(BIGINT(20), primary_key=True, comment='#资金账户表ID#')
    account_type = Column(TINYINT(4), comment='#账户类型#')
    account_name = Column(String(100), comment='#账户名#')
    account_no = Column(String(50), comment='#账号#')
    bank_name = Column(String(100), comment='#发卡行#')
    company = Column(String(255), comment='#公司名称#')
    message = Column(String(255), comment='#备注#')
    sub_bank_name = Column(String(100), comment='#发卡子行#')
    money = Column(DECIMAL(10, 2), server_default=text("'0.00'"), comment='#账户余额#')
    status = Column(TINYINT(4), comment='#状态#')
    subject = Column(String(10), comment='#对应会计科目#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BBillItem(Base):
    __tablename__ = 'b_bill_item'
    __table_args__ = {'comment': '账单费用明细表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键ID#')
    bill_id = Column(BIGINT(20), comment='#账单ID#')
    item_name = Column(String(255), comment='#项名称#')
    num = Column(INTEGER(10), comment='#数量#')
    unit_price = Column(DECIMAL(10, 2), comment='#单价#')
    unit_code = Column(String(50), comment='#单位字典code#')
    unit_name = Column(String(50), comment='#单位字典name#')
    adjust_price = Column(DECIMAL(10, 2), comment='#调整价格#')
    message = Column(String(255), comment='#说明#')
    bill_type = Column(TINYINT(4), comment='#所属账单类型#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


t_b_bill_report_snap = Table(
    'b_bill_report_snap', metadata,
    Column('id', BIGINT(20), comment='#账单结算报工快照表ID#'),
    Column('bill_id', BIGINT(20), comment='#账单表ID#'),
    Column('bill_type', TINYINT(4), comment='#账单类型#'),
    Column('work_detail', Text, comment='#作业报工明细数据#'),
    Column('day_work_detail', Text, comment='#日报工明细数据#'),
    Column('version', INTEGER(11), comment='#数据版本#'),
    Column('creator_id', BIGINT(20), comment='#创建人id#'),
    Column('creator', String(25), server_default=text("''"), comment='#创建人#'),
    Column('create_time', DateTime, comment='#创建时间#'),
    Column('modifier_id', BIGINT(20), comment='#修改人id#'),
    Column('modifier', String(25), server_default=text("''"), comment='#修改人#'),
    Column('update_time', DateTime, comment='#修改时间#'),
    Column('delete_flag', TINYINT(4), server_default=text("'0'"), comment='逻辑删除#ENUM#0:正常,1:删除'),
    comment='账单结算报工快照表'
)


class BBuildDeviceParameter(Base):
    __tablename__ = 'b_build_device_parameter'
    __table_args__ = {'comment': '施工设备参数'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    build_device_id = Column(BIGINT(20), nullable=False, comment='#施工设备id#')
    device_category_id = Column(BIGINT(20), comment='#设备品类#')
    device_param_id = Column(BIGINT(20), comment='#设备规格参数id#')
    device_param_name = Column(String(50), comment='#设备规格参数名称#')
    device_param_value = Column(DECIMAL(18, 2), comment='#参数值#')
    unit_id = Column(BIGINT(20), comment='#计量单位id#')
    unit_name = Column(String(25), comment='#计量单位（冗余）#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BBuildDeviceTenantDispatchInfo(Base):
    __tablename__ = 'b_build_device_tenant_dispatch_info'
    __table_args__ = {'comment': '商户设备匹配调度表'}

    id = Column(BIGINT(22), primary_key=True, comment='#主键ID#')
    build_notice_id = Column(BIGINT(20), nullable=False, comment='#施工通知单ID#')
    build_notice_device_assign_id = Column(BIGINT(20), nullable=False, comment='#b_build_notice_device_assign.id#')
    device_category_id = Column(BIGINT(20), comment='#设备品类id#')
    tenant_order_id = Column(BIGINT(20), comment='#商户转租订单id#b_tenant_order.id#')
    tenant_order_code = Column(String(50), comment='#商户转租订单编号#b_tenant_order.code#')
    tenant_order_device_id = Column(BIGINT(20), comment='#商户转租订单设备id#tenant_order_device.id#')
    tenant_order_valuation_id = Column(BIGINT(20), comment='#商户转租订单设备计价方式##b_tenant_order_valuation.id#')
    tenant_id = Column(BIGINT(20), comment='#商户id#')
    tenant_name = Column(VARCHAR(200), comment='#商户名称#')
    customer_order_id = Column(BIGINT(20), comment='#b_customer_order.id#')
    customer_order_device_id = Column(BIGINT(20), comment='#b_customer_order_device.id#')
    customer_order_valuation_id = Column(BIGINT(20), comment='#b_customer_order_valuation.id#')
    customer_id = Column(BIGINT(20), comment='#客户id#')
    tenant_contract_id = Column(BIGINT(20), comment='#转租合同ID#')
    tenant_order_num = Column(INTEGER(11), server_default=text("'0'"), comment='#商户订单数量#')
    tenant_contract_code = Column(String(100), comment='#转租合同code#')
    dispatched_num = Column(INTEGER(11), server_default=text("'0'"), comment='#平台已调度数量#')
    num = Column(INTEGER(11), comment='#本次平台调度数量#')
    valuation_way = Column(TINYINT(4), comment='#计价方式#')
    dispatched_time = Column(DateTime, comment='#平台调度时间#')
    status = Column(TINYINT(4), server_default=text("'0'"), comment='#状态#ENUM#0:正常:NORMAL,1:商户拒绝调度:REFUSE#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(VARCHAR(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(VARCHAR(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BBuildNotice(Base):
    __tablename__ = 'b_build_notice'
    __table_args__ = {'comment': '施工通知单'}

    id = Column(BIGINT(22), primary_key=True, comment='#主键ID#')
    code = Column(String(50), comment='#通知单编号#')
    customer_id = Column(BIGINT(22), comment='#客户id#')
    customer_name = Column(String(50), comment='#客户编号#')
    customer_order_id = Column(BIGINT(22), comment='#租赁订单id#')
    customer_order_code = Column(String(50), comment='#租赁订单编号#')
    project_id = Column(BIGINT(20), comment='#工程id#')
    project_name = Column(String(100), comment='#工程名称#')
    contract_id = Column(BIGINT(20), nullable=False, comment='#合同id#')
    contract_code = Column(String(50), comment='#合同编号#')
    contract_name = Column(String(100), comment='#合同名称#')
    site_leader = Column(String(100), comment='#客户现场负责人#')
    site_leader_phone = Column(String(20), comment='#客户现场负责人电话#')
    province_code = Column(String(50), comment='#省份code#')
    province_name = Column(String(50), comment='#省份名称#')
    city_code = Column(String(50), comment='#城市code#')
    city_name = Column(String(50), comment='#城市名称#')
    district_code = Column(String(50), comment='#区域code#')
    district_name = Column(String(50), comment='#区域名称#')
    address = Column(String(1000), comment='#施工地址#')
    type = Column(TINYINT(4), comment='#类型Enum#1:NORMAL:普通,2:ADDED:追加，3:CHANGE_DEVICE:更换设备#')
    status = Column(TINYINT(4), comment='#订单状态Enum#1.WAITING:待调度,2.PART_WAITING:部分调度,3.FINISH:已完成,4.CLOSE:关闭#')
    customer_contract_type = Column(TINYINT(4), comment='#合同类型#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BBuildNoticeDevice(Base):
    __tablename__ = 'b_build_notice_device'
    __table_args__ = {'comment': '施工通知单设备信息'}

    id = Column(BIGINT(22), primary_key=True, comment='#主键ID#')
    build_notice_id = Column(BIGINT(22), nullable=False, comment='#施工通知单表id#b_build_notice.id#')
    customer_order_device_id = Column(BIGINT(22), comment='#租赁订单设备id#')
    device_category_id = Column(BIGINT(22), comment='#品类id#b_device_category.id')
    device_category_name = Column(VARCHAR(50), comment='#品类名称#')
    brand_id = Column(BIGINT(22), comment='#品牌id#b_device_brand.id')
    brand_name = Column(VARCHAR(50), comment='#品牌名称#')
    device_type = Column(VARCHAR(100), comment='#设备型号#')
    leasing_model = Column(TINYINT(4), comment='#租赁模式#')
    valuation_way = Column(TINYINT(4), comment='#结算模式#')
    rent_unit = Column(String(100), comment='#租金单位#')
    order_num = Column(INTEGER(11), server_default=text("'0'"), comment='#订单数量#')
    noticed_num = Column(INTEGER(11), comment='#该设备本次施工通知总量#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(VARCHAR(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(VARCHAR(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BBuildNoticeDeviceAssign(Base):
    __tablename__ = 'b_build_notice_device_assign'
    __table_args__ = {'comment': '施工通知单设备分配信息表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键ID#')
    build_notice_id = Column(BIGINT(20), nullable=False, comment='#施工通知单ID#')
    notice_device_id = Column(BIGINT(20), nullable=False, comment='#施工通知的设备ID#')
    enter_time = Column(DateTime, comment='#进场时间#')
    num = Column(INTEGER(11), server_default=text("'0'"), comment='#本次施工通知数量#')
    dispatch_num = Column(INTEGER(11), server_default=text("'0'"), comment='#平台已调度数量#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(VARCHAR(50), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(VARCHAR(50), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), comment='#逻辑删除#ENUM#0:正常,1:删除#')
    version = Column(INTEGER(11), comment='#数据版本#')


class BBuildNumBu(Base):
    __tablename__ = 'b_build_num_bus'
    __table_args__ = {'comment': '施工调度数量总线表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键#')
    build_notice_id = Column(BIGINT(20), comment='#施工单ID#')
    contract_id = Column(BIGINT(20), comment='#合同ID#')
    contract_type = Column(BIGINT(20), comment='#合同类型#')
    device_id = Column(BIGINT(20), comment='#合同设备ID#')
    target_num = Column(INTEGER(10), server_default=text("'0'"), comment='#目标履约数量#')
    actual_num = Column(INTEGER(10), server_default=text("'0'"), comment='#实际履约数量#')
    build_notice_status = Column(TINYINT(4), comment='#施工单状态#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BBusinessCost(Base):
    __tablename__ = 'b_business_cost'
    __table_args__ = {'comment': '商机费用条目'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    business_id = Column(BIGINT(20), comment='#商机id#')
    cost_id = Column(BIGINT(20), comment='#费用id#')
    cost_name = Column(String(100), comment='#费用名目(冗余)#')
    undertake_object = Column(TINYINT(4), comment='#承担对象#ENUM#0:甲方:PARTY_A,1:乙方:PARTY_B#')
    money = Column(DECIMAL(18, 2), comment='#金额（元）#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


t_b_business_defeat_cause = Table(
    'b_business_defeat_cause', metadata,
    Column('id', BIGINT(20), comment='#主键id#'),
    Column('business_id', BIGINT(20), comment='#商机id#'),
    Column('type', TINYINT(4), comment='#原因类型#'),
    Column('content', String(1000), comment='#内容#'),
    Column('version', INTEGER(11), comment='#数据版本#'),
    Column('creator_id', BIGINT(20), comment='#创建人id#'),
    Column('creator', String(25), server_default=text("''"), comment='#创建人#'),
    Column('create_time', DateTime, comment='#创建时间#'),
    Column('modifier_id', BIGINT(20), comment='#修改人id#'),
    Column('modifier', String(25), server_default=text("''"), comment='#修改人#'),
    Column('update_time', DateTime, comment='#修改时间#'),
    Column('delete_flag', TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#'),
    comment='商机战败原因表'
)


class BBusinessDevice(Base):
    __tablename__ = 'b_business_device'
    __table_args__ = {'comment': '商业设备表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    business_id = Column(BIGINT(20), comment='#商机id#')
    device_category_id = Column(BIGINT(20), comment='#设备品类id#')
    device_category_name = Column(String(50), comment='#设备品类名称#')
    brand_id = Column(BIGINT(20), comment='#品牌id#')
    brand_name = Column(String(50), comment='#品牌名称#')
    model = Column(String(100), comment='#型号#')
    num = Column(INTEGER(11), comment='#台数#')
    leasing_model = Column(TINYINT(4), comment='#租赁模式#ENUM#0:干租:DRY_LEASE,1:湿租:WET_LEASE#')
    valuation_way = Column(TINYINT(4), comment='计价方式#ENUM#0:包月:MONTH,1:台班:MACHINE_TEAM,2:按日:DAY,3:按小时:HOUR')
    invoice_type = Column(TINYINT(4), comment='#开票类型#ENUM#0:不开票:NO_INVOICING,1:普票:ORDINARY_INVOICE,2:专票:SPECIAL_INVOICE#')
    tax_rate = Column(DECIMAL(18, 2), comment='#租金税率#')
    unit_price = Column(DECIMAL(18, 2), comment='#不含税单价#')
    tax_unit_price = Column(DECIMAL(18, 2), comment='#含税单价#')
    first_entry_num = Column(INTEGER(11), comment='#首次进场台数#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BBusinessDeviceParameter(Base):
    __tablename__ = 'b_business_device_parameter'
    __table_args__ = {'comment': '商机设备参数'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    business_id = Column(BIGINT(20), comment='#商机id#')
    business_device_id = Column(BIGINT(20), comment='#商机设备id#')
    device_category_id = Column(BIGINT(20), comment='#设备品类#')
    device_param_id = Column(BIGINT(20), comment='#设备规格参数id#')
    device_param_name = Column(String(50), comment='#设备规格参数名称#')
    device_param_value = Column(DECIMAL(18, 2), comment='#参数值#')
    unit_id = Column(BIGINT(20), comment='#计量单位id#')
    unit_name = Column(String(25), comment='#计量单位（冗余）#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BBusinessEstimate(Base):
    __tablename__ = 'b_business_estimate'
    __table_args__ = {'comment': '商机项目测算表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    business_id = Column(BIGINT(20), comment='#商机id#')
    customer_id = Column(BIGINT(20), comment='#客户id#')
    customer_name = Column(String(50), comment='#客户名称#')
    sales_bd_id = Column(BIGINT(20), comment='#销售BD id#')
    sales_bd_name = Column(String(25), comment='#销售BD名称#')
    leasing_days = Column(INTEGER(11), comment='#预计租赁时长#')
    client_rental_income = Column(DECIMAL(18, 2), comment='#客端-租金收入#')
    client_logistics_tax_rate = Column(DECIMAL(18, 2), comment='#客端-物流税率(%)#')
    client_logistics_income = Column(DECIMAL(18, 2), comment='#客端-物流收入#')
    client_total_income = Column(DECIMAL(18, 2), comment='#客端-收入合计#')
    output_tax = Column(DECIMAL(18, 2), comment='#客端-销项税#')
    tenant_rental_expend = Column(DECIMAL(18, 2), comment='#商端-租金支出#')
    tenant_logistics_tax_rate = Column(DECIMAL(18, 2), comment='#商端-物流税率(%)#')
    tenant_logistics_expend = Column(DECIMAL(18, 2), comment='#商端-物流支出#')
    tenant_total_expend = Column(DECIMAL(18, 2), comment='#商端-支出合计#')
    input_tax = Column(DECIMAL(18, 2), comment='#商端-进项税#')
    value_added_tax = Column(DECIMAL(18, 2), comment='#增值税赋(元)#')
    gross_profit = Column(DECIMAL(18, 2), comment='#毛利（元）#')
    gross_profit_rate = Column(DECIMAL(18, 2), comment='#毛利率(%)#')
    client_payment_months = Column(INTEGER(11), comment='#对客账期（月）#')
    financing_apr = Column(DECIMAL(18, 2), comment='#融资年利率(%)#')
    cost_funds = Column(DECIMAL(18, 2), comment='#资金成本（元）#')
    reduced_income = Column(DECIMAL(18, 2), comment='#减免抵减收入（元）#')
    freight_reduction_ratio = Column(DECIMAL(18, 2), comment='#运费减免比例#')
    client_commission = Column(DECIMAL(18, 2), comment='#客端佣金（元）#')
    tenant_commission = Column(DECIMAL(18, 2), comment='#商端佣金（元）#')
    city_manager_commission = Column(DECIMAL(18, 2), comment='#城市经理佣金(元)#')
    totail_commission = Column(DECIMAL(18, 2), comment='#佣金合计(元)#')
    fund_cost = Column(DECIMAL(18, 2), comment='#资金成本(元)#')
    profit = Column(DECIMAL(18, 2), comment='#项目利润#')
    remark = Column(String(1000), comment='#备注#')
    data_type = Column(TINYINT(4), comment='#数据类型#ENUM#0:最新:NEWEST,1:历史:HISTORY#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BBusinessEstimateApproveRecord(Base):
    __tablename__ = 'b_business_estimate_approve_record'
    __table_args__ = {'comment': '商机项目审核记录表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    business_estimate_id = Column(BIGINT(20), comment='#商机测算id#')
    current_step = Column(INTEGER(11), comment='#当前流程步骤#')
    approver_id = Column(BIGINT(20), comment='#审批人id#')
    approver_name = Column(String(25), comment='#审批人名称#')
    remark = Column(String(1000), comment='#备注#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BBusinessEstimateCustomerDevice(Base):
    __tablename__ = 'b_business_estimate_customer_device'
    __table_args__ = {'comment': '商机利润测算租赁订单表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    business_id = Column(BIGINT(20), comment='#商机id#')
    estimate_id = Column(BIGINT(20), comment='#利润测算id#')
    customer_id = Column(BIGINT(20), comment='#客户id#')
    customer_name = Column(String(50), comment='#客户名称#')
    device_category_id = Column(BIGINT(20), comment='#设备品类id#')
    device_category_name = Column(String(50), comment='#设备品类名称#')
    unit_price = Column(DECIMAL(18, 2), comment='#不含税单价#')
    tax_rate = Column(DECIMAL(18, 2), comment='#税率#')
    tax_unit_price = Column(DECIMAL(18, 2), comment='#含税单价#')
    num = Column(INTEGER(11), comment='#台数#')
    leasing_model = Column(TINYINT(4), comment='#租赁模式#ENUM#0:干租:DRY_LEASE,1:湿租:WET_LEASE#')
    valuation_way = Column(TINYINT(4), comment='计价方式#ENUM#0:包月:MONTH,1:台班:MACHINE_TEAM,2:按日:DAY,3:按小时:HOUR')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BBusinessEstimateTenantDevice(Base):
    __tablename__ = 'b_business_estimate_tenant_device'
    __table_args__ = {'comment': '商机利润测算转租订单表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    business_sub_id = Column(BIGINT(20), comment='#子商机id#')
    estimate_id = Column(BIGINT(20), comment='#利润测算id#')
    tenant_id = Column(BIGINT(20), comment='#商户id#')
    tenant_name = Column(String(100), comment='#商户名称#')
    device_category_id = Column(BIGINT(20), comment='#设备品类id#')
    device_category_name = Column(String(50), comment='#设备品类名称#')
    unit_price = Column(DECIMAL(18, 2), comment='#不含税单价#')
    tax_rate = Column(DECIMAL(18, 2), comment='#税率#')
    tax_unit_price = Column(DECIMAL(18, 2), comment='#含税单价#')
    num = Column(INTEGER(11), comment='#台数#')
    leasing_model = Column(TINYINT(4), comment='#租赁模式#ENUM#0:干租:DRY_LEASE,1:湿租:WET_LEASE#')
    valuation_way = Column(TINYINT(4), comment='计价方式#ENUM#0:包月:MONTH,1:台班:MACHINE_TEAM,2:按日:DAY,3:按小时:HOUR')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BBusinessInfo(Base):
    __tablename__ = 'b_business_info'
    __table_args__ = {'comment': '商机信息表'}

    id = Column(BIGINT(1), primary_key=True, comment='#主键id#')
    code = Column(String(100), comment='#客户商机编号#')
    customer_id = Column(BIGINT(20), comment='#客户id#')
    customer_name = Column(String(50), comment='#客户名称#')
    project_id = Column(BIGINT(20), comment='#工程id#')
    customer_contacts = Column(String(50), comment='#客户联系人#')
    customer_contacts_phone = Column(String(25), comment='#客户联系电话#')
    customer_site_leader = Column(String(25), comment='#客户现场负责人#')
    customer_site_leader_phone = Column(String(25), comment='#客户现场负责人电话#')
    last_defeat_status = Column(TINYINT(4), comment='#商机设为"战败"之前的状态#')
    status = Column(TINYINT(4), comment='#商机状态#')
    defeat_cause_type = Column(TINYINT(4), comment='#战败类型#')
    defeat_cause_desc = Column(String(500), comment='#战败原因类型描述#')
    profit_estimate = Column(TINYINT(1), server_default=text("'0'"), comment='#是否做过利润测算#')
    project_name = Column(String(100), comment='#工程名称#')
    province_code = Column(String(50), comment='#省份编号#')
    province_name = Column(String(50), comment='#省份名称#')
    city_code = Column(String(50), comment='#城市编号#')
    city_name = Column(String(50), comment='#城市名称#')
    district_code = Column(String(50), comment='#区域编号#')
    district_name = Column(String(50), comment='#区域名称#')
    address = Column(String(200), comment='#施工地点#')
    construction_type = Column(TINYINT(4), comment='#施工类型#')
    demand_month = Column(String(25), comment='#需求月份#')
    entry_date = Column(Date, comment='#进场日期#')
    departure_date = Column(Date, comment='#离场日期#')
    payment_terms = Column(TINYINT(4), comment='#支付条款, RENT_PREPAID: 租金先付, RENT_DEFERRED: 租金后付#')
    entry_fee = Column(DECIMAL(18, 2), comment='#进场费用#')
    delivery_method = Column(TINYINT(4), comment='#设备交付方式#ENUM#0:出租方负责运输:LESSOR,1:承租方负责运输:LESSEE#')
    project_content = Column(String(1000), comment='#施工内容#')
    sales_bd_id = Column(BIGINT(20), comment='#销售id#')
    sales_bd_name = Column(String(25), comment='#销售名称#')
    raw_score = Column(DECIMAL(18, 2), comment='#初评分数#')
    review_score = Column(DECIMAL(18, 2), comment='#复核分数#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BBusinessProjectFile(Base):
    __tablename__ = 'b_business_project_file'
    __table_args__ = {'comment': '商机工程资料'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    business_id = Column(BIGINT(20), comment='#商机id#')
    file_id = Column(BIGINT(20), comment='#文件id#')
    file_name = Column(String(500), comment='#文件名称#')
    url = Column(String(1024), comment='#文件url#')
    extension = Column(String(25), comment='#拓展名#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BBusinessSubCost(Base):
    __tablename__ = 'b_business_sub_cost'
    __table_args__ = {'comment': '子商机费用条目'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    business_sub_id = Column(BIGINT(20), comment='#子商机id#')
    cost_id = Column(BIGINT(20), comment='#费用id#')
    cost_name = Column(String(100), comment='#费用名目(冗余)#')
    undertake_object = Column(TINYINT(4), comment='#承担对象#ENUM#0:甲方:PARTY_A,1:乙方:PARTY_B#')
    money = Column(DECIMAL(18, 2), comment='#金额（元）#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


t_b_business_sub_defeat_cause = Table(
    'b_business_sub_defeat_cause', metadata,
    Column('id', BIGINT(20), comment='#主键id#'),
    Column('business_sub_id', BIGINT(20), comment='#子商机id#'),
    Column('type', TINYINT(4), comment='#原因类型#'),
    Column('content', String(1000), comment='#内容#'),
    Column('version', INTEGER(11), comment='#数据版本#'),
    Column('creator_id', BIGINT(20), comment='#创建人id#'),
    Column('creator', String(25), server_default=text("''"), comment='#创建人#'),
    Column('create_time', DateTime, comment='#创建时间#'),
    Column('modifier_id', BIGINT(20), comment='#修改人id#'),
    Column('modifier', String(25), server_default=text("''"), comment='#修改人#'),
    Column('update_time', DateTime, comment='#修改时间#'),
    Column('delete_flag', TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#'),
    comment='商机战败原因表'
)


class BBusinessSubDevice(Base):
    __tablename__ = 'b_business_sub_device'
    __table_args__ = {'comment': '子商业设备表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    business_sub_id = Column(BIGINT(20), comment='#子商机id#')
    tenant_id = Column(BIGINT(20), comment='#商户id#')
    tenant_name = Column(String(50), comment='#商户名称#')
    device_category_id = Column(BIGINT(20), comment='#设备品类#')
    device_category_name = Column(String(50), comment='#设备品类名称#')
    brand_id = Column(BIGINT(20), comment='#品牌id#')
    brand_name = Column(String(50), comment='#品牌名称#')
    model = Column(String(100), comment='#型号#')
    num = Column(INTEGER(11), comment='#台数#')
    leasing_model = Column(TINYINT(4), comment='#租赁模式#ENUM#0:干租:DRY_LEASE,1:湿租:WET_LEASE#')
    valuation_way = Column(TINYINT(4), comment='计价方式#ENUM#0:包月:MONTH,1:台班:MACHINE_TEAM,2:按日:DAY,3:按小时:HOUR')
    invoice_type = Column(TINYINT(4), comment='#开票类型#')
    tax_rate = Column(DECIMAL(18, 2), comment='#租金税率#')
    unit_price = Column(DECIMAL(18, 2), comment='#不含税单价#')
    tax_unit_price = Column(DECIMAL(18, 2), comment='#含税单价#')
    first_entry_num = Column(INTEGER(11), comment='#首次进场台数#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BBusinessSubDeviceParameter(Base):
    __tablename__ = 'b_business_sub_device_parameter'
    __table_args__ = {'comment': '子商机设备参数'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    business_sub_id = Column(BIGINT(20), comment='#子商机id#')
    business_device_id = Column(BIGINT(20), comment='#商机设备id#')
    device_category_id = Column(BIGINT(20), comment='#设备品类#')
    device_param_id = Column(BIGINT(20), comment='#设备规格参数id#')
    device_param_name = Column(String(50), comment='#设备规格参数名称#')
    device_param_value = Column(DECIMAL(18, 2), comment='#参数值#')
    unit_id = Column(BIGINT(20), comment='#计量单位id#')
    unit_name = Column(String(25), comment='#计量单位（冗余）#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BBusinessSubInfo(Base):
    __tablename__ = 'b_business_sub_info'
    __table_args__ = {'comment': '子商机信息表'}

    id = Column(BIGINT(1), primary_key=True, comment='#主键id#')
    code = Column(String(100), comment='#商户子商机编号#')
    business_id = Column(BIGINT(20), comment='#商机id#')
    tenant_id = Column(BIGINT(20), comment='#商户id#')
    tenant_name = Column(String(50), comment='#商户名称#')
    project_id = Column(BIGINT(20), comment='#工程id#')
    project_name = Column(String(100), comment='#工程名称#')
    status = Column(TINYINT(4), comment='#商机状态#')
    defeat_cause_type = Column(TINYINT(4), comment='#战败原因类型#')
    defeat_cause_desc = Column(String(500), comment='#战败原因类型描述#')
    address = Column(String(200), comment='#施工地点#')
    construction_type = Column(TINYINT(4), comment='#施工类型#')
    demand_month = Column(String(25), comment='#需求月份#')
    entry_date = Column(Date, comment='#进场日期#')
    departure_date = Column(Date, comment='#离场日期#')
    payment_terms = Column(TINYINT(4), comment='#支付条款, RENT_PREPAID: 租金先付, RENT_DEFERRED: 租金后付#')
    entry_fee = Column(DECIMAL(18, 2), comment='#进场费用#')
    delivery_method = Column(TINYINT(4), comment='#设备交付方式#ENUM#0:出租方负责运输:LESSOR,1:承租方负责运输:LESSEE#')
    project_content = Column(String(1000), comment='#施工内容#')
    merchants_bd_id = Column(BIGINT(20), comment='#招商BD的id#')
    merchants_bd_name = Column(String(25), comment='#招商BD的名称#')
    raw_score = Column(DECIMAL(18, 2), comment='#初评分数#')
    review_score = Column(DECIMAL(18, 2), comment='#复核分数#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BBusinessSubProjectFile(Base):
    __tablename__ = 'b_business_sub_project_file'
    __table_args__ = {'comment': '子商机工程资料'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    business_sub_id = Column(BIGINT(20), comment='#子商机id#')
    file_id = Column(BIGINT(20), comment='#文件id#')
    file_name = Column(String(500), comment='#文件名称#')
    url = Column(String(1000), comment='#文件url#')
    extension = Column(String(25), comment='#拓展名#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BBusinessSubValuation(Base):
    __tablename__ = 'b_business_sub_valuation'
    __table_args__ = {'comment': '子商机计价信息表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    business_sub_id = Column(BIGINT(20), comment='#子商户id#')
    month_days = Column(DECIMAL(18, 2), comment='#按月-包月天数#')
    month_hours = Column(DECIMAL(18, 2), comment='#按月-包月时限#')
    month_overtime_fee = Column(DECIMAL(18, 2), comment='#按月-超时费用#')
    month_entry_rule_time_before = Column(Time, comment='#按月-进场规则-时间-前#')
    month_entry_rule_time_before_days = Column(DECIMAL(18, 2), comment='#按月-进场规则-时间-前-天数#')
    month_entry_rule_middle_days = Column(DECIMAL(18, 2), comment='#按月-进场规则-中间进场-天数#')
    month_entry_rule_time_after = Column(Time, comment='#按月-进场规则-时间-后#')
    month_entry_rule_time_after_days = Column(DECIMAL(18, 2), comment='#按月-进场规则-时间-后-天数#')
    month_exit_rule_time_before = Column(Time, comment='#按月-退场规则-时间-前#')
    month_exit_rule_time_before_days = Column(DECIMAL(18, 2), comment='#按月-退场规则-时间-前-天数#')
    month_exit_rule_middle_days = Column(DECIMAL(18, 2), comment='#按月-退场规则-中间进场-天数#')
    month_exit_rule_time_after = Column(Time, comment='#按月-退场规则-时间-后#')
    month_exit_rule_time_after_days = Column(DECIMAL(18, 2), comment='#按月-退场规则-时间-后-天数#')
    machine_team_hours = Column(DECIMAL(18, 2), comment='#台班-时限#')
    machine_team_unit_device_num = Column(INTEGER(11), comment='#台班-单位设备台数#')
    machine_team_unit_operator_num = Column(INTEGER(11), comment='#台班-单位设备操作员数#')
    machine_team_work_rule_match_num = Column(DECIMAL(18, 2), comment='#台班-报工规则-匹配规则台班数#')
    machine_team_work_rule_not_match_num = Column(DECIMAL(18, 2), comment='#台班-报工规则-不匹配规则台班数#')
    machine_team_food_bed_type = Column(TINYINT(4), comment='#台班-住宿伙食#ENUM#0:包食宿:CONTAIN_ALL,1:包住宿，不包伙食:BED,2:包伙食，不包住宿:FOOD,3:不包食宿:NOT_CONTAIN#')
    day_hours = Column(DECIMAL(18, 2), comment='#按日-时限#')
    day_entry_rule_time_before = Column(Time, comment='#按日-进场规则-时间-前#')
    day_entry_rule_time_before_days = Column(DECIMAL(18, 2), comment='#按日-进场规则-时间-前-天数#')
    day_entry_rule_middle_days = Column(DECIMAL(18, 2), comment='#按日-进场规则-中间进场-天数#')
    day_entry_rule_time_after = Column(Time, comment='#按日-进场规则-时间-后#')
    day_entry_rule_time_after_days = Column(DECIMAL(18, 2), comment='#按日-进场规则-时间-后-天数#')
    day_exit_rule_time_before = Column(Time, comment='#按日-退场规则-时间-前#')
    day_exit_rule_time_before_days = Column(DECIMAL(18, 2), comment='#按日-退场规则-时间-前-天数#')
    day_exit_rule_middle_days = Column(DECIMAL(18, 2), comment='#按日-退场规则-中间进场-天数#')
    day_exit_rule_time_after = Column(Time, comment='#按日-退场规则-时间-后#')
    day_exit_rule_time_after_days = Column(DECIMAL(18, 2), comment='#按日-退场规则-时间-后-天数#')
    day_work_rule_match_num = Column(DECIMAL(18, 2), comment='#按日-报工规则-匹配规则天数#')
    day_work_rule_not_match = Column(DECIMAL(18, 2), comment='#按日-报工规则-不匹配规则天数#')
    hour_fee = Column(DECIMAL(18, 2), comment='#按小时-保底金额#')
    hour_duration = Column(DECIMAL(18, 2), comment='#按小时-保底时长#')
    hour_overtime_fee = Column(DECIMAL(18, 2), comment='#按小时-超时费用#')
    hour_work_rule_match_num = Column(DECIMAL(18, 2), comment='#按小时-报工规则-匹配规则小时数#')
    hour_work_rule_not_match = Column(DECIMAL(18, 2), comment='#按小时-报工规则-不匹配规则小时数')
    other_valuation_remark = Column(String(1000), comment='#其他计价方式#')
    prepayment = Column(DECIMAL(18, 2), comment='#预付费用#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')
    machineTeamUnitDeviceNum = Column(INTEGER(11), comment='#台班-单位设备台数#')
    machineTeamUnitOperatorNum = Column(INTEGER(11), comment='#台班-单位设备操作员数#')


class BBusinessValuation(Base):
    __tablename__ = 'b_business_valuation'
    __table_args__ = {'comment': '商机计价信息表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    business_id = Column(BIGINT(20), comment='#商户id#')
    month_days = Column(DECIMAL(18, 2), comment='#按月-包月天数#')
    month_hours = Column(DECIMAL(18, 2), comment='#按月-包月时限#')
    month_overtime_fee = Column(DECIMAL(18, 2), comment='#按月-超时费用#')
    month_entry_rule_time_before = Column(Time, comment='#按月-进场规则-时间-前#')
    month_entry_rule_time_before_days = Column(DECIMAL(18, 2), comment='#按月-进场规则-时间-前-天数#')
    month_entry_rule_middle_days = Column(DECIMAL(18, 2), comment='#按月-进场规则-中间进场-天数#')
    month_entry_rule_time_after = Column(Time, comment='#按月-进场规则-时间-后#')
    month_entry_rule_time_after_days = Column(DECIMAL(18, 2), comment='#按月-进场规则-时间-后-天数#')
    month_exit_rule_time_before = Column(Time, comment='#按月-退场规则-时间-前#')
    month_exit_rule_time_before_days = Column(DECIMAL(18, 2), comment='#按月-退场规则-时间-前-天数#')
    month_exit_rule_middle_days = Column(DECIMAL(18, 2), comment='#按月-退场规则-中间进场-天数#')
    month_exit_rule_time_after = Column(Time, comment='#按月-退场规则-时间-后#')
    month_exit_rule_time_after_days = Column(DECIMAL(18, 2), comment='#按月-退场规则-时间-后-天数#')
    machine_team_hours = Column(DECIMAL(18, 2), comment='#台班-时限#')
    machine_team_unit_device_num = Column(INTEGER(11), comment='#台班-单位设备台数#')
    machine_team_unit_operator_num = Column(INTEGER(11), comment='#台班-单位设备操作员数#')
    machine_team_work_rule_match_num = Column(DECIMAL(18, 2), comment='#台班-报工规则-匹配规则台班数#')
    machine_team_work_rule_not_match_num = Column(DECIMAL(18, 2), comment='#台班-报工规则-不匹配规则台班数#')
    machine_team_food_bed_type = Column(TINYINT(4), comment='#台班-住宿伙食#ENUM#0:包食宿:CONTAIN_ALL,1:包住宿，不包伙食:BED,2:包伙食，不包住宿:FOOD,3:不包食宿:NOT_CONTAIN#')
    day_hours = Column(DECIMAL(18, 2), comment='#按日-时限#')
    day_entry_rule_time_before = Column(Time, comment='#按日-进场规则-时间-前#')
    day_entry_rule_time_before_days = Column(DECIMAL(18, 2), comment='#按日-进场规则-时间-前-天数#')
    day_entry_rule_middle_days = Column(DECIMAL(18, 2), comment='#按日-进场规则-中间进场-天数#')
    day_entry_rule_time_after = Column(Time, comment='#按日-进场规则-时间-后#')
    day_entry_rule_time_after_days = Column(DECIMAL(18, 2), comment='#按日-进场规则-时间-后-天数#')
    day_exit_rule_time_before = Column(Time, comment='#按日-退场规则-时间-前#')
    day_exit_rule_time_before_days = Column(DECIMAL(18, 2), comment='#按日-退场规则-时间-前-天数#')
    day_exit_rule_middle_days = Column(DECIMAL(18, 2), comment='#按日-退场规则-中间进场-天数#')
    day_exit_rule_time_after = Column(Time, comment='#按日-退场规则-时间-后#')
    day_exit_rule_time_after_days = Column(DECIMAL(18, 2), comment='#按日-退场规则-时间-后-天数#')
    day_work_rule_match_num = Column(DECIMAL(18, 2), comment='#按日-报工规则-匹配规则天数#')
    day_work_rule_not_match = Column(DECIMAL(18, 2), comment='#按日-报工规则-不匹配规则天数#')
    hour_fee = Column(DECIMAL(18, 2), comment='#按小时-保底金额#')
    hour_duration = Column(DECIMAL(18, 2), comment='#按小时-保底时长#')
    hour_overtime_fee = Column(DECIMAL(18, 2), comment='#按小时-超时费用#')
    hour_work_rule_match_num = Column(DECIMAL(18, 2), comment='#按小时-报工规则-匹配规则小时数#')
    hour_work_rule_not_match = Column(DECIMAL(18, 2), comment='#按小时-报工规则-不匹配规则小时数')
    other_valuation_remark = Column(String(1000), comment='#其他计价方式#')
    prepayment = Column(DECIMAL(18, 2), comment='#预付费用#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BClassifyInfo(Base):
    __tablename__ = 'b_classify_info'
    __table_args__ = {'comment': '分类信息表'}

    id = Column(BIGINT(22), primary_key=True, comment='#主键ID#')
    name = Column(String(255))
    icon = Column(String(255), comment='#分类图标#')
    show_flag = Column(TINYINT(1), comment='#是否显示#1:是，0:否#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BClueDeviceCategory(Base):
    __tablename__ = 'b_clue_device_category'
    __table_args__ = {'comment': '线索设备需求表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    clue_id = Column(BIGINT(20), nullable=False, comment='#线索id#')
    device_category_first_id = Column(BIGINT(20), nullable=False, comment='#设备品类一级id#')
    device_category_second_id = Column(BIGINT(20), comment='#设备品类二级id#')
    device_category_third_id = Column(BIGINT(20), comment='#设备品类三级id#')
    device_amount = Column(INTEGER(11), comment='#设备数量#')
    version = Column(INTEGER(11), server_default=text("'1'"), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BClueInfo(Base):
    __tablename__ = 'b_clue_info'
    __table_args__ = {'comment': '线索信息表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    customer_id = Column(BIGINT(20), nullable=False, comment='#客户id#')
    customer_name = Column(String(255), comment='#客户名称#')
    customer_contacts = Column(String(50), nullable=False, comment='#客户联系人#')
    customer_phone = Column(String(50), nullable=False, comment='#联系人电话#')
    clue_level = Column(TINYINT(4), comment='#线索级别#ENUM#1:S,2:A,3:B,4:C#')
    expiration = Column(Date, nullable=False, comment='#过期时间#')
    province_id = Column(BIGINT(20), comment='#省id#REF#b_base_area.id#')
    province_code = Column(String(50), comment='#省code#REF#b_base_area.code#')
    province_name = Column(String(50), comment='#省名称#REF#b_base_area.name#')
    city_id = Column(BIGINT(20), comment='#市id#REF#b_base_area.id#')
    city_code = Column(String(50), comment='#市code#REF#b_base_area.code#')
    city_name = Column(String(50), comment='#市名称#REF#b_base_area.name#')
    district_id = Column(BIGINT(20), comment='#区id#REF#b_base_area.id#')
    district_code = Column(String(50), comment='#区code#REF#b_base_area.code#')
    district_name = Column(String(50), comment='#区名称#REF#b_base_area.name#')
    address = Column(String(100), comment='#详细地址#')
    address_description = Column(String(255), comment='#地址说明#')
    address_title = Column(String(255), comment='#地址标题#')
    address_lat = Column(String(50), comment='#详细地址纬度#')
    address_lng = Column(String(50), comment='#详细地址经度#')
    construction_type = Column(TINYINT(4), comment='#施工类型#ENUM#1:土建,2:钢构,3:消防,4:水电安装,5:通风安装,6:设备安装,7:油漆涂料,8:幕墙施工,9:装饰装修,10:市政维保类,11:其他#')
    converted = Column(TINYINT(1), server_default=text("'0'"), comment='#是否已转化商机#')
    sales_bd_id = Column(BIGINT(20), comment='#销售BDid#')
    version = Column(INTEGER(11), server_default=text("'1'"), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BCustomerContract(Base):
    __tablename__ = 'b_customer_contract'
    __table_args__ = {'comment': '客户合同表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    customer_id = Column(BIGINT(20), comment='#客户id#')
    customer_name = Column(String(50), comment='#客户名称#')
    type = Column(TINYINT(4), comment='#合同类型#')
    sign_date = Column(Date, comment='#签署日期#')
    code = Column(String(50), comment='#合同编号#')
    name = Column(String(100), comment='#合同名称#')
    external_code = Column(String(50), comment='#外部合同编号#')
    external_name = Column(String(100), comment='#外部合同编号#')
    status = Column(TINYINT(4), comment='#合同状态#')
    sales_bd_id = Column(BIGINT(20), comment='#销售BD id#')
    sales_bd_name = Column(String(50), comment='#销售BD 名称#')
    sign_sales_id = Column(BIGINT(20), comment='#签约销售id#')
    sign_sales_name = Column(String(50), comment='#签约销售名称#')
    region_name = Column(String(50), comment='#大区门店#')
    party_a_id = Column(BIGINT(20), comment='#甲方主体id#')
    party_a_name = Column(String(50), comment='#甲方（出租方）名称#')
    party_a_unified_social_credit_code = Column(String(50), comment='#甲方统一社会信用代码/身份证#')
    party_a_address = Column(String(500), comment='#甲方通讯地址#')
    party_a_legal_person = Column(String(25), comment='#甲方法定代表人#')
    party_a_contacts = Column(String(25), comment='#甲方联系人#')
    party_a_phone = Column(String(25), comment='#甲方联系方式#')
    party_b_name = Column(String(50), comment='#乙方（出租方）名称#')
    party_b_unified_social_credit_code = Column(String(50), comment='#乙方统一社会信用代码/身份证#')
    party_b_address = Column(String(500), comment='#乙方通讯地址#')
    party_b_legal_person = Column(String(25), comment='#乙方法定代表人#')
    party_b_contacts = Column(String(25), comment='#乙方联系人#')
    party_b_phone = Column(String(25), comment='#乙方联系方式#')
    party_a_account_name = Column(String(100), comment='#甲方账号名#')
    party_a_bank_account = Column(String(100), comment='#甲方账号#')
    party_a_bank_name = Column(String(100), comment='#甲方开户行#')
    party_b_invoice_name = Column(String(100), comment='#乙方名称#')
    party_b_invoice_tx_id_num = Column(String(50), comment='#乙方纳税人识别号#')
    party_b_invoice_address = Column(String(500), comment='#乙方地址#')
    party_b_invoice_tel = Column(String(50), comment='#乙方电话#')
    party_b_invoice_bank_name = Column(String(100), comment='#乙方开户行#')
    party_b_invoice_bank_account = Column(String(100), comment='#乙方账号#')
    start_date = Column(Date, comment='#合同起始日期#')
    end_date = Column(Date, comment='#合同结束日期#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BCustomerContractFile(Base):
    __tablename__ = 'b_customer_contract_file'
    __table_args__ = {'comment': '客户合同附件表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    customer_contract_id = Column(BIGINT(20), comment='#客户合同表id#')
    attachment_file_id = Column(BIGINT(20), comment='#附件id#')
    attachment_url = Column(String(1024), comment='#附件url#')
    attachment_name = Column(String(100), comment='#附件名称#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BCustomerContractZero(Base):
    __tablename__ = 'b_customer_contract_zero'
    __table_args__ = {'comment': '零租合同表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    contract_id = Column(BIGINT(20), comment='#租凭合同id#')
    contract_code = Column(String(50), comment='#租凭合同编号#')
    business_id = Column(BIGINT(200), comment='#商机id#')
    project_id = Column(BIGINT(20), comment='#工程id#')
    project_name = Column(String(100), comment='#工程名称#')
    delivery_place = Column(String(200), comment='#施工/设备交付地点#')
    entry_date = Column(DateTime, comment='#进场时间#')
    departure_date = Column(DateTime, comment='#离场时间#')
    delivery_method = Column(TINYINT(4), comment='#设备交付方式#ENUM#0:出租方负责运输:LESSOR,1:承租方负责运输:LESSEE#')
    construction_content = Column(TINYINT(4), comment='#施工内容#')
    construction_content_other_desc = Column(String(1024), comment='#施工内容其他补充说明#')
    invoice_type = Column(TINYINT(4), comment='#开票类型#')
    prepaid_amount = Column(DECIMAL(18, 2), comment='#预付金额#')
    lease_amount = Column(INTEGER(11), server_default=text("'0'"), comment='#租赁台数#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BCustomerContractZeroCost(Base):
    __tablename__ = 'b_customer_contract_zero_cost'
    __table_args__ = {'comment': '零租合同费用分担表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    customer_contract_id = Column(BIGINT(20), nullable=False, comment='#租赁合同id#')
    cost_id = Column(BIGINT(20), comment='#费用id#')
    cost_name = Column(String(100), comment='#费用名目(冗余)#')
    money = Column(DECIMAL(18, 2), comment='#金额（元）#')
    sort = Column(INTEGER(11), comment='#排序#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BCustomerContractZeroDevice(Base):
    __tablename__ = 'b_customer_contract_zero_device'
    __table_args__ = {'comment': '零租合同设备表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    customer_contract_id = Column(BIGINT(20), comment='#租赁合同id#')
    device_category_id = Column(BIGINT(20), comment='#设备品类id#')
    device_category_name = Column(String(20), comment='#设备品类#')
    brand_id = Column(BIGINT(20), comment='#品牌id#')
    brand_name = Column(String(50), comment='#品牌名称#')
    model = Column(String(100), comment='#型号#')
    num = Column(INTEGER(11), comment='#台数#')
    leasing_model = Column(TINYINT(4), comment='#租赁模式#')
    unit_price = Column(DECIMAL(18, 2), comment='#不含税单价#')
    rent_unit = Column(String(50), comment='#租金单位#')
    tax_unit_price = Column(DECIMAL(18, 2), comment='#含税单价#')
    tax_rent_subtotal = Column(DECIMAL(18, 2), comment='#含税租金小计#')
    rent_subtotal = Column(DECIMAL(18, 2), comment='#不含税租金小计#')
    sort = Column(INTEGER(11), comment='#排序#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BCustomerContractZeroDeviceParameter(Base):
    __tablename__ = 'b_customer_contract_zero_device_parameter'
    __table_args__ = {'comment': '零租合同设备参数'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    customer_contract_id = Column(BIGINT(20), comment='#租赁合同id#')
    customer_contract_zero_device_id = Column(BIGINT(20), comment='#零租合同设备id#')
    device_category_id = Column(BIGINT(20), comment='#设备品类id#')
    device_category_name = Column(String(50), comment='#设备品类名称#')
    device_param_id = Column(BIGINT(20), comment='#设备规格参数id#')
    device_param_name = Column(String(50), comment='#设备规格参数名称#')
    device_param_value = Column(DECIMAL(18, 2), comment='#参数值#')
    unit_id = Column(BIGINT(20), comment='#计量单位id#')
    unit_name = Column(String(25), comment='#计量单位（冗余）#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BCustomerInfo(Base):
    __tablename__ = 'b_customer_info'
    __table_args__ = {'comment': '客户信息表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    parent_id = Column(BIGINT(20), comment='#归属企业id，当客户性质为企业员工时用于关联企业#')
    tenant_id = Column(BIGINT(20), comment='#商户id, 用于关联商户创建客户#')
    nature = Column(TINYINT(4), nullable=False, comment='#客户性质#ENUM#1:企业:ENTERPRISE,2:企业员工:ENTERPRISE_EMPLOYEE,3:个人:PERSONAL#')
    code = Column(String(50), nullable=False, comment='#客户编号#')
    name = Column(String(100), nullable=False, comment='#客户名称#')
    name_pinyin = Column(String(200), comment='#客户名称拼音#')
    sales_bd_name = Column(String(50), comment='#销售BD名称#')
    sales_bd_id = Column(BIGINT(20), comment='#销售BD id#')
    province_code = Column(String(50), comment='#省code#REF#b_base_area.code#')
    province_name = Column(String(50), comment='#省名称#REF#b_base_area.name#')
    city_code = Column(String(50), comment='#市code#REF#b_base_area.code#')
    city_name = Column(String(50), comment='#市名称#REF#b_base_area.name#')
    district_code = Column(String(50), comment='#区code#REF#b_base_area.code#')
    district_name = Column(String(50), comment='#区名称#REF#b_base_area.name#')
    address = Column(String(500), comment='#详细地址#')
    contacts = Column(String(50), comment='#联系人#')
    phone = Column(String(50), comment='#联系手机#')
    front_desk_tel = Column(String(50), comment='#前台电话#')
    customer_source = Column(TINYINT(4), comment='#客户来源#ENUM#1:线上推广:ONLINE_PROMOTION,2:属地工程陌拜:LOCAL_PROJECT_COLD_CALL,3:属地企业陌拜:LOCAL_ENTERPRISE_COLD_CALL,4:老客户转介绍:OLD_CUSTOMER_REFERRAL,5:公司客户池资源:CUSTOMER_POOL#')
    enterprise_type = Column(TINYINT(4), comment='#企业类型#ENUM#1:央企:CENTRAL_ENTERPRISE,2:国企:STATE_ENTERPRISE,3:民营企业:PRIVATE_ENTERPRISE,4:外资企业:FOREIGN_ENTERPRISE#')
    personnel_size = Column(TINYINT(4), comment='#人员规模#ENUM#1:1000人以上:GE_1000,2:500-999人:BT_500_999,3:100-499人:BT_100_TO_499,4:99人及以下:LE_99#')
    customer_type = Column(TINYINT(4), comment='#客户类型#ENUM#1:总承包:GENERAL_CONTRACTING,2:专业分包:PROFESSIONAL_SUBCONTRACTING,3:劳务分包:LABOR_SUBCONTRACTING,4:劳务班组:LABOR_TEAMS,5:个人:INDIVIDUALS,6:其他:OTHER#')
    customer_level = Column(TINYINT(4), comment='#客户等级#ENUM#1:战略客户:STRATEGIC,2:核心客户:CORE,3:潜力客户:POTENTIAL,4:一般客户:GENERAL,5:意向客户:INTENDED,6:潜在客户:LATENT,7:黑名单客户:BLACKLIST#')
    cooperation_status = Column(TINYINT(4), comment='#合作状态#ENUM#1:未合作:NO_COOPERATION,2:商机客户:BUSINESS_CUSTOMER,3:已合作:ALREADY_COOPERATION#')
    special_invoice = Column(TINYINT(1), server_default=text("'0'"), comment='#开票类型-专票#')
    ordinary_invoice = Column(TINYINT(1), server_default=text("'0'"), comment='#开票类型-普票#')
    no_invoice = Column(TINYINT(1), server_default=text("'0'"), comment='#开票类型-不开票#')
    business_domains = Column(String(50), comment='#业务领域, 多个用逗号隔开#')
    construction_types = Column(String(50), comment='#施工类型，多个用逗号隔开#')
    device_types = Column(String(50), comment='#常用设备类型，多个用逗号隔开#')
    business_coverage = Column(TINYINT(4), comment='#业务覆盖范围#ENUM#1:全国:NATIONAL,2:大区级:REGIONAL,3:省级:PROVINCIAL,4:市级:MUNICIPAL#')
    payment_method = Column(TINYINT(4), comment='#常用付款方式#')
    has_master = Column(TINYINT(1), comment='#是否有机手#')
    key_decision_maker = Column(String(50), comment='#关键决策人#')
    decision_maker_tel = Column(String(50), comment='#决策人电话#')
    decision_maker_age = Column(TINYINT(4), comment='#决策人年龄#')
    decision_maker_position = Column(String(50), comment='#决策人职位#')
    unified_social_credit_code = Column(String(50), comment='#统一社会信用代码#')
    legal_person = Column(String(50), comment='#法人#')
    business_license_file_id = Column(BIGINT(20), comment='#营业执照文件id#')
    business_license_file_name = Column(String(100), comment='#营业执照文件名称#')
    business_license_url = Column(String(1024), comment='#营业执照图片地址#')
    id_card_num = Column(String(20), comment='#身份证号#')
    id_card_front = Column(String(1024), comment='#身份证正面图片地址#')
    id_card_front_url = Column(String(1024), comment='#身份证正面图片url#')
    id_card_front_file_id = Column(BIGINT(20), comment='#身份证正面图片文件id#')
    id_card_front_file_name = Column(String(100), comment='#身份证下面图片文件名称#')
    id_card_back = Column(String(1024), comment='#身份证反面图片地址#')
    id_card_back_url = Column(String(1024), comment='#身份证反面图片url#')
    id_card_back_file_id = Column(BIGINT(20), comment='#身份证反面图片文件id#')
    id_card_back_file_name = Column(String(100), comment='#身份证反面图片文件名称#')
    registered_capital = Column(TINYINT(4), comment='#注册资本#ENUM#1:5亿以上:GT_5_Y,2:1-5亿:BT_1_5_Y,3:5000-9999万:BT_5000_9999_W,4:2000-4999万:BT_2000_4999_W,5:1000-1999万:BT_1000_1999_W,6:1000万以下:LT_1000_W#')
    paid_in_capital = Column(DECIMAL(18, 4), comment='#实缴资本#')
    register_years = Column(INTEGER(11), comment='#已注册年限#')
    total_assets = Column(DECIMAL(18, 4), comment='#总资产#')
    asset_liability_ratio = Column(DECIMAL(18, 4), comment='#资产负债率#')
    version = Column(INTEGER(11), server_default=text("'1'"), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), index=True, server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BCustomerOrder(Base):
    __tablename__ = 'b_customer_order'
    __table_args__ = {'comment': '客端订单表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    status = Column(TINYINT(4), comment='#订单状态#')
    code = Column(String(50), comment='#订单编号#')
    customer_id = Column(BIGINT(20), comment='#客户id#')
    customer_name = Column(String(50), comment='#客户名称#')
    contract_id = Column(BIGINT(20), comment='#租凭合同id#')
    contract_code = Column(String(50), comment='#租凭合同编号#')
    business_id = Column(BIGINT(20), comment='#商机id#')
    sales_bd_id = Column(BIGINT(20), comment='#销售BD id#')
    sales_bd_name = Column(String(50), comment='#销售BD名称#')
    party_a_contacts = Column(String(25), comment='#甲方联系人#')
    party_a_phone = Column(String(25), comment='#甲方联系方式#')
    party_b_contacts = Column(String(25), comment='#乙方联系人#')
    party_b_phone = Column(String(25), comment='#乙方联系方式#')
    site_leader = Column(String(25), comment='#客户现场负责人#')
    site_leader_phone = Column(String(25), comment='#客户现场负责人电话#')
    project_id = Column(BIGINT(20), comment='#工程id#')
    project_name = Column(String(100), comment='#工程名称#')
    province_code = Column(String(50), comment='#省code#')
    province_name = Column(String(50), comment='#省份名称#')
    city_code = Column(String(50), comment='#市code#')
    city_name = Column(String(50), comment='#城市名称#')
    district_code = Column(String(50), comment='#区code#')
    district_name = Column(String(50), comment='#区域名称#')
    delivery_place = Column(String(200), comment='#施工/设备交付地点#')
    entry_date = Column(Date, comment='#进场日期#')
    departure_date = Column(Date, comment='#离场日期#')
    delivery_method = Column(TINYINT(4), comment='#设备交付方式#ENUM#0:出租方负责运输:LESSOR,1:承租方负责运输:LESSEE#')
    project_content = Column(String(1000), comment='#施工内容#')
    payment_terms = Column(TINYINT(4), comment='#支付条款#')
    other_valuation_way = Column(String(1024), comment='#其他计价方式#')
    rent_deferred_desc = Column(String(1024), comment='#租金后付条款补充说明#')
    entry_fee = Column(DECIMAL(18, 2), comment='#进场费用#')
    cause_type = Column(TINYINT(4), comment='#取消原因类型#')
    cancel_reason = Column(String(200), comment='#取消原因#')
    cancel_time = Column(DateTime, comment='#取消时间#')
    lease_amount = Column(INTEGER(11), server_default=text("'0'"), comment='#租赁台数#')
    sign_sales_id = Column(BIGINT(20), comment='#签约销售id#')
    sign_sales_name = Column(String(25), comment='#签约销售名称#')
    sign_date = Column(Date, comment='#签约日期#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BCustomerOrderCost(Base):
    __tablename__ = 'b_customer_order_cost'
    __table_args__ = {'comment': '客端订单费用分担表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    customer_order_id = Column(BIGINT(20), nullable=False, comment='#客端订单id#')
    cost_id = Column(BIGINT(20), comment='#费用id#')
    cost_name = Column(String(100), comment='#费用名目(冗余)#')
    undertake_object = Column(TINYINT(4), comment='#承担对象#ENUM#0:甲方:PARTY_A,1:乙方:PARTY_B#')
    money = Column(DECIMAL(18, 2), comment='#金额（元）#')
    sort = Column(INTEGER(11), comment='#排序#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BCustomerOrderDevice(Base):
    __tablename__ = 'b_customer_order_device'
    __table_args__ = {'comment': '客端订单设备表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    customer_order_id = Column(BIGINT(20), comment='#客端订单id#')
    device_category_id = Column(BIGINT(20), comment='#设备品类id#')
    device_category_name = Column(String(20), comment='#设备品类#')
    brand_id = Column(BIGINT(20), comment='#品牌id#')
    brand_name = Column(String(50), comment='#品牌名称#')
    model = Column(String(100), comment='#型号#')
    num = Column(INTEGER(11), comment='#台数#')
    leasing_model = Column(TINYINT(4), comment='#租赁模式#')
    valuation_way = Column(TINYINT(4), comment='#计价方式#')
    invoice_type = Column(TINYINT(4), comment='#开票类型#ENUM#0:不开票:NO_INVOICING,1:普票:ORDINARY_INVOICE,2:专票:SPECIAL_INVOICE#')
    tax_rate = Column(DECIMAL(10, 2), comment='#租金税率#')
    unit_price = Column(DECIMAL(18, 2), comment='#不含税单价#')
    tax_unit_price = Column(DECIMAL(18, 2), comment='#含税单价#')
    first_entry_num = Column(INTEGER(11), comment='#首次进场台数#')
    sort = Column(INTEGER(11), comment='#排序#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')
    dispatched_num = Column(INTEGER(11), server_default=text("'0'"), comment='#已调度设备数量#')


class BCustomerOrderDeviceParameter(Base):
    __tablename__ = 'b_customer_order_device_parameter'
    __table_args__ = {'comment': '客端订单设备参数'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    customer_order_id = Column(BIGINT(20), comment='#客端订单id#')
    customer_order_device_id = Column(BIGINT(20), comment='#客端订单设备id#')
    device_category_id = Column(BIGINT(20), comment='#设备品类id#')
    device_category_name = Column(String(50), comment='#设备品类名称#')
    device_param_id = Column(BIGINT(20), comment='#设备规格参数id#')
    device_param_name = Column(String(50), comment='#设备规格参数名称#')
    device_param_value = Column(DECIMAL(18, 2), comment='#参数值#')
    unit_id = Column(BIGINT(20), comment='#计量单位id#')
    unit_name = Column(String(25), comment='#计量单位（冗余）#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BCustomerOrderFile(Base):
    __tablename__ = 'b_customer_order_file'
    __table_args__ = {'comment': '客户合同订单附件表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    customer_order_id = Column(BIGINT(20), comment='#客户订单id#')
    attachment_file_id = Column(BIGINT(20), comment='#附件id#')
    attachment_url = Column(String(1024), comment='#附件url#')
    attachment_name = Column(String(100), comment='#附件名称#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BCustomerOrderValuation(Base):
    __tablename__ = 'b_customer_order_valuation'
    __table_args__ = {'comment': '客端订单计价方式约定表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    customer_order_id = Column(BIGINT(20), comment='#客端订单id#')
    order_device_id = Column(BIGINT(20), comment='#订单设备id#')
    valuation_way = Column(TINYINT(4), comment='#计价方式#')
    month_days = Column(DECIMAL(18, 2), comment='#按月-包月天数#')
    month_hours = Column(DECIMAL(18, 2), comment='#按月-包月时限#')
    month_overtime_fee = Column(DECIMAL(18, 2), comment='#按月-超时费用#')
    month_entry_rule_time_before = Column(Time, comment='#按月-进场规则-时间-前#')
    month_entry_rule_time_before_days = Column(DECIMAL(10, 2), comment='#按月-进场规则-时间-前-天数#')
    month_entry_rule_middle_days = Column(DECIMAL(10, 2), comment='#按月-进场规则-中间进场-天数#')
    month_entry_rule_time_after = Column(Time, comment='#按月-进场规则-时间-后#')
    month_entry_rule_time_after_days = Column(DECIMAL(10, 2), comment='#按月-进场规则-时间-后-天数#')
    month_exit_rule_time_before = Column(Time, comment='#按月-退场规则-时间-前#')
    month_exit_rule_time_before_days = Column(DECIMAL(10, 2), comment='#按月-退场规则-时间-前-天数#')
    month_exit_rule_middle_days = Column(DECIMAL(10, 2), comment='#按月-退场规则-中间进场-天数#')
    month_exit_rule_time_after = Column(Time, comment='#按月-退场规则-时间-后#')
    month_exit_rule_time_after_days = Column(DECIMAL(18, 2), comment='#按月-退场规则-时间-后-天数#')
    month_exchange_machine_hours = Column(DECIMAL(18, 2), comment='#按月-转台班时限#')
    month_exchange_machine_price = Column(DECIMAL(10, 2), comment='#按月-转台班单价#')
    month_exchange_machine_work_rule_match_num = Column(DECIMAL(18, 2), comment='#按月-转台班-报工规则-匹配规则台班数#')
    month_exchange_machine_work_rule_not_match = Column(DECIMAL(18, 2), comment='#按月-转台班-报工规则-不匹配规则台班数#')
    machine_team_hours = Column(DECIMAL(18, 2), comment='#台班-时限#')
    machine_team_work_rule_match_num = Column(DECIMAL(18, 2), comment='#台班-报工规则-匹配规则台班数#')
    machine_team_work_rule_not_match_num = Column(DECIMAL(18, 2), comment='#台班-报工规则-不匹配规则台班数#')
    machine_team_unit_device_num = Column(DECIMAL(18, 2), comment='#台班-单位设备台数#')
    machine_team_unit_operator_num = Column(DECIMAL(18, 2), comment='#台班-单位设备操作员数#')
    machine_team_food_bed_type = Column(TINYINT(4), comment='#台班-住宿伙食#ENUM#0:包食宿:CONTAIN_ALL,1:包住宿，不包伙食:BED,2:包伙食，不包住宿:FOOD,3:不包食宿:NOT_CONTAIN#')
    day_hours = Column(DECIMAL(18, 2), comment='#按日-时限#')
    day_entry_rule_time_before = Column(Time, comment='#按日-进场规则-时间-前#')
    day_entry_rule_time_before_days = Column(DECIMAL(18, 2), comment='#按日-进场规则-时间-前-天数#')
    day_entry_rule_middle_days = Column(DECIMAL(18, 2), comment='#按日-进场规则-中间进场-天数#')
    day_entry_rule_time_after = Column(Time, comment='#按日-进场规则-时间-后#')
    day_entry_rule_time_after_days = Column(DECIMAL(18, 2), comment='#按日-进场规则-时间-后-天数#')
    day_exit_rule_time_before = Column(Time, comment='#按日-退场规则-时间-前#')
    day_exit_rule_time_before_days = Column(DECIMAL(18, 2), comment='#按日-退场规则-时间-前-天数#')
    day_exit_rule_middle_days = Column(DECIMAL(18, 2), comment='#按日-退场规则-中间进场-天数#')
    day_exit_rule_time_after = Column(Time, comment='#按日-退场规则-时间-后#')
    day_exit_rule_time_after_days = Column(DECIMAL(18, 2), comment='#按日-退场规则-时间-后-天数#')
    day_work_rule_match_num = Column(DECIMAL(18, 2), comment='#按日-报工规则-匹配规则天数#')
    day_work_rule_not_match = Column(DECIMAL(18, 2), comment='#按日-报工规则-不匹配规则天数#')
    hour_fee = Column(DECIMAL(18, 0), comment='#按小时-保底金额#')
    hour_duration = Column(DECIMAL(18, 2), comment='#按小时-保底时长#')
    hour_overtime_fee = Column(DECIMAL(18, 2), comment='#按小时-超时费用#')
    hour_work_rule_match_num = Column(DECIMAL(18, 2), comment='#按小时-报工规则-匹配规则小时数#')
    hour_work_rule_not_match = Column(DECIMAL(18, 2), comment='#按小时-报工规则-不匹配规则小时数#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BDeviceBrand(Base):
    __tablename__ = 'b_device_brand'
    __table_args__ = {'comment': '设备品牌表'}

    id = Column(BIGINT(22), primary_key=True, comment='#主键ID#')
    name = Column(String(100), comment='#品牌名称#')
    code = Column(String(20), comment='#品牌code#')
    sort = Column(INTEGER(11), comment='#排序#')
    url = Column(String(1000), comment='#logo链接#')
    file_name = Column(String(255))
    ename = Column(String(100), comment='#英文名称#')
    file_id = Column(BIGINT(22), comment='#文件ID#')
    state = Column(TINYINT(4), comment='#枚举：启用，禁用#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BDeviceCategory(Base):
    __tablename__ = 'b_device_category'
    __table_args__ = {'comment': '设备品类级别表'}

    id = Column(BIGINT(22), primary_key=True, comment='#主键ID#')
    name = Column(String(100), comment='#类别名称#')
    parent_code = Column(String(50), comment='#父级code#')
    parent_id = Column(BIGINT(22), server_default=text("'0'"), comment='#父级id#')
    sort = Column(INTEGER(11), comment='#排序#')
    code = Column(String(50), unique=True, comment='#品类code#')
    version = Column(INTEGER(11), server_default=text("'0'"), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')
    status = Column(TINYINT(4), server_default=text("'0'"), comment='#启用状态#')
    introduce = Column(String(2000), comment='#介绍#')
    need_master = Column(TINYINT(4), server_default=text("'0'"), comment='是否需要机手')
    transport_type = Column(TINYINT(4), server_default=text("'0'"), comment='#运输方式#')


class BDeviceCategoryParam(Base):
    __tablename__ = 'b_device_category_param'
    __table_args__ = {'comment': '设备品类规格参数表'}

    id = Column(BIGINT(22), primary_key=True, comment='#主键ID#')
    category_id = Column(BIGINT(22), comment='#品类id#')
    name = Column(String(50), comment='#参数名称#')
    category_code = Column(String(100), comment='#品类code#')
    unit_id = Column(BIGINT(22), comment='#参数id#')
    unit = Column(String(100), comment='#中文单位#')
    en_unit = Column(String(64), comment='#英文单位#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BDeviceCategoryPicture(Base):
    __tablename__ = 'b_device_category_picture'
    __table_args__ = {'comment': '设备品类图片表'}

    id = Column(BIGINT(22), primary_key=True, comment='#设备明细图片表ID#')
    category_id = Column(BIGINT(22), comment='#设备品类ID#')
    main_graph = Column(TINYINT(1), server_default=text("'0'"), comment='#是否主图#')
    url = Column(String(1000), comment='#链接#')
    file_name = Column(String(255), comment='#文件名#')
    file_id = Column(BIGINT(22), comment='#文件ID#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BDeviceDetail(Base):
    __tablename__ = 'b_device_detail'
    __table_args__ = {'comment': '设备明细表'}

    id = Column(BIGINT(22), primary_key=True, comment='#主键ID#')
    tenant_id = Column(BIGINT(20), comment='#商户id#')
    device_id = Column(BIGINT(22), comment='#设备型号ID#')
    device_no = Column(String(50), comment='#设备序列号#')
    made_time = Column(Date, comment='#出厂日期#')
    work_hours = Column(DECIMAL(10, 0), comment='#工作小时数#')
    storage_name = Column(String(255), comment='#所在仓库#')
    storage_id = Column(BIGINT(22), comment='#仓库ID#')
    state = Column(INTEGER(3), server_default=text("'0'"), comment='#设备状态#1:出租中；0:待出租#')
    message = Column(String(255), comment='#补充说明#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='逻辑删除#ENUM#0:正常,1:删除')
    brand_id = Column(BIGINT(22), comment='#品牌id#')
    brand = Column(String(40), comment='#品牌#')
    device_type = Column(String(100), comment='#设备型号#')
    dispatch_status = Column(TINYINT(4), server_default=text("'0'"), comment='#设备调度状态#')


class BDeviceDetailPicture(Base):
    __tablename__ = 'b_device_detail_picture'
    __table_args__ = {'comment': '设备明细图片表'}

    id = Column(BIGINT(22), primary_key=True, comment='#设备明细图片表ID#')
    url = Column(String(1000), comment='#链接#')
    file_name = Column(String(255), comment='#文件名#')
    detail_id = Column(BIGINT(22), comment='#设备明细ID#')
    file_id = Column(BIGINT(22), comment='#文件ID#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BDeviceInfo(Base):
    __tablename__ = 'b_device_info'
    __table_args__ = {'comment': '设备信息表'}

    id = Column(BIGINT(22), primary_key=True, comment='#主键#')
    category_fir = Column(BIGINT(22), comment='#一级品类id#')
    category_sec = Column(BIGINT(22), comment='#二级品类id#')
    category_thi = Column(BIGINT(22), comment='#三级品类id#')
    category_id = Column(BIGINT(20), comment='#品类id(最后一级)#')
    category_name = Column(String(100), comment='#品类名称#')
    tenant_id = Column(BIGINT(22), comment='#商户ID#')
    tenant_name = Column(String(255), comment='#商户名称#')
    quote_text = Column(String(255), comment='#报价说明#')
    lease_mode = Column(TINYINT(4), comment='#租赁模式#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='逻辑删除#ENUM#0:正常,1:删除')
    provide_freight = Column(TINYINT(1), server_default=text("'0'"), comment='#是否提供运输物流#')
    freight_price = Column(DECIMAL(20, 2), comment='#运费单价#')


class BDeviceInfoReduction(Base):
    __tablename__ = 'b_device_info_reduction'
    __table_args__ = {'comment': '设备信息表-运费减免政策'}

    id = Column(BIGINT(22), primary_key=True, comment='#主键#')
    day_num = Column(INTEGER(22), nullable=False, comment='#天数#')
    reduction = Column(DECIMAL(20, 4), nullable=False, comment='#减免百分比#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')
    device_id = Column(BIGINT(22), comment='#设备id#')


class BDeviceParamUnit(Base):
    __tablename__ = 'b_device_param_unit'
    __table_args__ = {'comment': '设备规格参数单位表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    code = Column(String(25), comment='#编号#')
    name = Column(String(20), nullable=False, comment='#名称#')
    unit = Column(String(20), comment='#中文单位#')
    en_unit = Column(String(20), comment='#英文单位#')
    status = Column(TINYINT(2), comment='#状态#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='逻辑删除#ENUM#0:正常,1:删除')


class BDeviceParamValue(Base):
    __tablename__ = 'b_device_param_value'
    __table_args__ = {'comment': '设备规格参数值'}

    id = Column(BIGINT(22), primary_key=True, comment='#主键#')
    param_id = Column(BIGINT(22))
    device_id = Column(BIGINT(22), index=True, comment='#设备型号ID#b_device_info.id#')
    unit_id = Column(BIGINT(22), comment='#单位ID#')
    val = Column(DECIMAL(20, 2), comment='#数值#')
    param_name = Column(String(100), comment='#规格参数名称#')
    unit = Column(String(40), comment='#单位名称#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BDevicePrice(Base):
    __tablename__ = 'b_device_price'
    __table_args__ = {'comment': '设备租赁价格表'}

    id = Column(BIGINT(22), primary_key=True, comment='#主键ID#')
    lease_mode = Column(INTEGER(3), comment='#租赁模式#1:干租；0:湿租#')
    month_cost = Column(DECIMAL(10, 2), comment='#包月#')
    day_cost = Column(DECIMAL(10, 2), comment='#按日#')
    device_id = Column(BIGINT(22), index=True, comment='#设备型号ID#')
    moment_cost = Column(DECIMAL(10, 2), comment='#按台班#')
    hour_cost = Column(DECIMAL(10, 2), comment='#按小时#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='逻辑删除#ENUM#0:正常,1:删除')


class BDeviceStorage(Base):
    __tablename__ = 'b_device_storage'
    __table_args__ = {'comment': '设备仓库数量表'}

    id = Column(BIGINT(22), primary_key=True, comment='#主键ID #')
    tenant_id = Column(BIGINT(20), comment='#商户id#')
    device_id = Column(BIGINT(22), comment='#设备ID#')
    storage_id = Column(BIGINT(100), comment='#仓库ID#')
    count = Column(INTEGER(20), server_default=text("'0'"), comment='#数量#')
    storage_name = Column(String(100), comment='#仓库名称#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BDispatchTenantDevice(Base):
    __tablename__ = 'b_dispatch_tenant_device'
    __table_args__ = {'comment': '商户调度设备信息表'}

    id = Column(BIGINT(22), primary_key=True, comment='#主键ID#')
    dispatch_tenant_id = Column(BIGINT(22), nullable=False, comment='#调度表id#b_dispatch_tenant_info.id')
    build_device_dispatch_id = Column(BIGINT(20), comment='#商户设备匹配调度id#b_build_device_tenant_dispatch_info.id#')
    build_notice_device_assign_id = Column(BIGINT(20), nullable=False, comment='#设备拆分ID#')
    device_category_id = Column(BIGINT(22), comment='#设备品类id#')
    device_category_name = Column(String(50), comment='#设备品类名称#')
    brand_id = Column(BIGINT(22), comment='#品牌id#')
    brand_name = Column(String(50), comment='#品牌名称#')
    device_type = Column(String(50), comment='#设备型号#')
    tenant_id = Column(BIGINT(20), comment='#商户id#')
    tenant_order_id = Column(BIGINT(22), comment='#b_tenant_order.id#')
    tenant_order_device_id = Column(BIGINT(22), comment='#商户转租订单设备id#tenant_order_device.id#')
    tenant_order_valuation_id = Column(BIGINT(20), comment='#b_tenant_order_valuation.id#')
    customer_id = Column(BIGINT(20), comment='#客户id#')
    customer_order_id = Column(BIGINT(20), comment='#b_customer_order.id#')
    customer_order_device_id = Column(BIGINT(20), comment='#b_customer_order_device.id#')
    customer_order_valuation_id = Column(BIGINT(20), comment='#b_customer_order_valuation.id#')
    enter_time = Column(DateTime, comment='#进场时间#')
    leasing_model = Column(TINYINT(4), comment='#租赁方式#')
    valuation_way = Column(TINYINT(4), comment='#结算模式#')
    tenant_order_num = Column(INTEGER(11), server_default=text("'0'"), comment='#订单设备数量#')
    need_num = Column(INTEGER(11), server_default=text("'0'"), comment='#商户需调度数量#')
    dispatched_num = Column(INTEGER(11), comment='#商户已调度数量#')
    platform_dispatch_num = Column(INTEGER(11), server_default=text("'0'"), comment='#平台已调数量#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')
    build_notice_id = Column(BIGINT(20), comment='#施工单ID#')
    notice_type = Column(TINYINT(4), comment='#施工单类型#')
    rent_unit = Column(String(100), comment='#租金单位#')


class BDispatchTenantDeviceDetail(Base):
    __tablename__ = 'b_dispatch_tenant_device_detail'
    __table_args__ = {'comment': '商户调度设备明细表'}

    id = Column(BIGINT(22), primary_key=True, comment='#主键ID#')
    dispatch_tenant_device_id = Column(BIGINT(22), nullable=False, comment='#调度设备表id#b_dispatch_tenant_device.id')
    device_detail_id = Column(BIGINT(22), nullable=False, comment='#商户的设备明细表id#b_device_detail.id')
    device_no = Column(String(50), comment='#设备序列号#')
    enter_time = Column(DateTime, comment='#计划进场时间#')
    master_id = Column(BIGINT(22), comment='#机手id#')
    master_name = Column(String(255), comment='#机手名称#')
    master_phone = Column(String(20), comment='#机手手机号#')
    driver_id = Column(String(50), comment='#司机id#')
    driver_name = Column(String(50), comment='#司机姓名#')
    driver_phone = Column(String(50), comment='#司机手机#')
    status = Column(TINYINT(4), server_default=text("'0'"), comment='#记录状态#')
    enter_flag = Column(TINYINT(1), server_default=text("'0'"), comment='#是否已经产生进场单#true:是;false:否#')
    made_time = Column(DateTime, comment='#出厂日期#')
    driver_car_no = Column(String(50), comment='#司机车牌号#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BDispatchTenantDeviceDetailCache(Base):
    __tablename__ = 'b_dispatch_tenant_device_detail_cache'
    __table_args__ = {'comment': '商户调度设备明细表'}

    id = Column(BIGINT(22), primary_key=True, comment='#主键ID#')
    dispatch_tenant_device_id = Column(BIGINT(22), nullable=False, comment='#调度设备表id#b_dispatch_tenant_device.id')
    device_detail_id = Column(BIGINT(22), nullable=False, comment='#商户的设备明细表id#b_device_detail.id')
    device_no = Column(String(50), comment='#设备序列号#')
    enter_time = Column(DateTime, comment='#计划进场时间#')
    master_id = Column(BIGINT(22), comment='#机手id#')
    master_name = Column(String(255), comment='#机手名称#')
    master_phone = Column(String(20), comment='#机手手机号#')
    driver_id = Column(String(50), comment='#司机id#')
    driver_name = Column(String(50), comment='#司机姓名#')
    driver_phone = Column(String(50), comment='#司机手机#')
    status = Column(TINYINT(4), server_default=text("'0'"), comment='#记录状态#')
    enter_flag = Column(TINYINT(1), server_default=text("'0'"), comment='#是否已经产生进场单#true:是;false:否#')
    made_time = Column(DateTime, comment='#出厂日期#')
    driver_car_no = Column(String(50), comment='#司机车牌号#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BDispatchTenantDeviceParameter(Base):
    __tablename__ = 'b_dispatch_tenant_device_parameter'
    __table_args__ = {'comment': '商户调度设备参数'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    dispatch_tenant_device_id = Column(BIGINT(20), comment='#商户调度设备id#')
    device_category_id = Column(BIGINT(20), comment='#设备品类#')
    device_param_id = Column(BIGINT(20), comment='#设备规格参数id#')
    device_param_name = Column(String(50), comment='#设备规格参数名称#')
    device_param_value = Column(DECIMAL(18, 2), comment='#参数值#')
    unit_id = Column(BIGINT(20), comment='#计量单位id#')
    unit_name = Column(String(25), comment='#计量单位（冗余）#')
    unit_en_name = Column(String(25), comment='#英文计量单位（冗余）#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    modifier = Column(String(25), server_default=text("''"), comment='修改人')
    update_time = Column(DateTime, comment='修改时间')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='逻辑删除#ENUM#0:正常,1:删除')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')


class BDispatchTenantInfo(Base):
    __tablename__ = 'b_dispatch_tenant_info'
    __table_args__ = {'comment': '商户调度信息表'}

    id = Column(BIGINT(22), primary_key=True, comment='#主键ID#')
    build_device_tenant_dispatch_id = Column(BIGINT(20), nullable=False, comment='#平台调度id#b_build_device_tenant_dispatch_info.id#')
    build_notice_id = Column(BIGINT(22), nullable=False, comment='#通知单id#b_build_notice.id')
    build_notice_code = Column(String(22), comment='#通知单编号#')
    contract_id = Column(BIGINT(22), comment='#转租合同id#')
    customer_order_id = Column(BIGINT(20), comment='#租赁订单ID#')
    tenant_contract_code = Column(String(100), comment='#转租合同编号#')
    tenant_contract_id = Column(BIGINT(20), comment='#转租合同ID#')
    customer_order_code = Column(String(100), comment='#租赁订单编号#')
    tenant_id = Column(BIGINT(22), comment='#商户ID#')
    tenant_name = Column(String(100), comment='#转租方名称#')
    customer_id = Column(BIGINT(22), comment='#承租方id#')
    code = Column(String(50), comment='#商户调度单号#')
    project_id = Column(BIGINT(22), comment='#工程id#')
    project_name = Column(String(255), comment='#工程名称#')
    contract_name = Column(String(255), comment='#合同名称#')
    contract_code = Column(String(50), comment='#合同编号#')
    tenant_order_Id = Column(BIGINT(22), comment='#转租订单id#')
    tenant_order_code = Column(String(50), comment='#转租订单编号#')
    site_leader = Column(String(50), comment='#现场联系人#')
    site_leader_phone = Column(String(20), comment='#现场联系人手机#')
    refuse_msg = Column(String(1000), comment='#拒绝调度说明#')
    province_code = Column(String(50), comment='#省份code#')
    province_name = Column(String(50), comment='#省份名称#')
    city_code = Column(String(50), comment='#城市code#')
    city_name = Column(String(50), comment='#城市名称#')
    district_code = Column(String(50), comment='#区域code#')
    district_name = Column(String(50), comment='#区域名称#')
    address = Column(String(255), comment='#施工地址#')
    status = Column(TINYINT(4), comment='#状态#ENUM#1:待调度:WAITING,2:部分调度:PART_WAITING,3:已完成:FINISH,4:已关闭:REFUSE#')
    platform_dispatch_num = Column(INTEGER(11), server_default=text("'0'"), comment='#平台调度数量#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BEnterDeviceParameter(Base):
    __tablename__ = 'b_enter_device_parameter'
    __table_args__ = {'comment': '进场设备参数表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    enter_id = Column(BIGINT(20), comment='#进场单id#')
    device_category_id = Column(BIGINT(20), comment='#设备品类id#')
    device_category_name = Column(String(50), comment='#设备品类名称#')
    device_param_id = Column(BIGINT(20), comment='#设备规格参数id#')
    device_param_name = Column(String(50), comment='#设备规格参数名称#')
    device_param_value = Column(DECIMAL(18, 2), comment='#参数值#')
    unit_id = Column(BIGINT(20), comment='#计量单位id#')
    unit_name = Column(String(25), comment='#计量单位#')
    unit_en_name = Column(String(25), comment='#英文计量单位#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BEnterFile(Base):
    __tablename__ = 'b_enter_file'

    id = Column(BIGINT(20), primary_key=True, comment='#主键ID#')
    enter_id = Column(BIGINT(20), comment='#进场表id#b_enter_info.id')
    file_id = Column(BIGINT(20), comment='#文件ID#')
    file_name = Column(String(200), comment='#文件名#')
    file_url = Column(String(1000), comment='#文件URL#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BEnterInfo(Base):
    __tablename__ = 'b_enter_info'
    __table_args__ = {'comment': '进场确认单信息表'}

    id = Column(BIGINT(22), primary_key=True, comment='#主键ID#')
    status = Column(TINYINT(4), comment='#状态,1:待进场确认,2:进场完成,3:拒绝进场#')
    code = Column(String(50), comment='#进场单编号#')
    notice_id = Column(BIGINT(20), comment='#施工通知单id#')
    notice_code = Column(String(50), comment='#施工通知单编号#')
    dispatch_id = Column(BIGINT(22), comment='#调度单id#')
    dispatch_code = Column(String(50), comment='#调度单编号#')
    dispatch_device_detail_id = Column(BIGINT(20), comment='#调度设备明细表id#')
    customer_id = Column(BIGINT(20), comment='#客户id#')
    customer_name = Column(String(100), comment='#客户名称#')
    tenant_id = Column(BIGINT(22), comment='#商户id#')
    tenant_name = Column(String(100), comment='#商户名称#')
    customer_contract_id = Column(BIGINT(20), comment='#租赁合同id#')
    customer_contract_code = Column(String(50), comment='#租赁合同编号#')
    customer_contract_name = Column(String(50), comment='#租赁合同名称#')
    customer_contract_type = Column(BIGINT(20), comment='#租赁合同类型#')
    customer_order_id = Column(BIGINT(20), comment='#租赁订单id#')
    customer_order_code = Column(String(50), comment='#租赁订单编号#')
    customer_order_device_id = Column(BIGINT(20), comment='#租赁订单设备id#b_customer_order_device.id#')
    customer_order_valuation_id = Column(BIGINT(20), comment='#租赁订单计价方式id#b_customer_order_valuation.id#')
    tenant_contract_id = Column(BIGINT(20), comment='#转租合同id#')
    tenant_contract_code = Column(String(50), comment='#转租合同编号#')
    tenant_contract_name = Column(String(50), comment='#转租合同名称#')
    tenant_order_id = Column(BIGINT(20), comment='#转租订单id#')
    tenant_order_code = Column(String(50), comment='#转租订单编号#')
    tenant_order_device_id = Column(BIGINT(20), comment='#转租订单设备id#')
    tenant_order_valuation_id = Column(BIGINT(20), comment='#转租订单计价方式id#b_tenant_order_valuation.id##')
    device_no = Column(String(100), comment='#车牌号/序列号#')
    device_category_id = Column(BIGINT(20), comment='#设备品类id#')
    device_category_name = Column(String(50), comment='#设备品类名称#')
    brand_id = Column(BIGINT(20), comment='#品牌id#')
    brand_name = Column(String(100), comment='#品牌名称#')
    model = Column(String(50), comment='#型号#')
    leasing_model = Column(TINYINT(4), comment='#租赁模式#')
    valuation_way = Column(TINYINT(4), comment='#计价方式#')
    transport_car_no = Column(String(50), comment='#运输车牌号#')
    driver_name = Column(String(50), comment='#司机姓名#')
    driver_phone = Column(String(50), comment='#司机手机号#')
    master_id = Column(BIGINT(20), comment='#机手id#')
    master_phone = Column(String(50), comment='#机手手机号#')
    master_name = Column(String(50), comment='#机手名称#')
    project_id = Column(BIGINT(20), comment='#工程id#')
    project_name = Column(String(100), comment='#工程名称#')
    site_leader = Column(String(100), comment='#现场负责人#')
    site_leader_phone = Column(String(20), comment='#现场联系人电话#')
    province_code = Column(String(50), comment='#省份code#')
    province_name = Column(String(100), comment='#省份名称#')
    city_code = Column(String(50), comment='#城市code#')
    city_name = Column(String(100), comment='#城市名称#')
    district_code = Column(String(50), comment='#区域code#')
    district_name = Column(String(100), comment='#区域名称#')
    address = Column(String(100), comment='#施工地址#')
    detail_desc = Column(String(1000), comment='#详细说明#')
    plan_enter_time = Column(DateTime, comment='#计划进场时间#')
    confirm_time = Column(DateTime, comment='#确认时间#')
    acceptance_instructions = Column(String(1000), comment='#验收说明#')
    num = Column(INTEGER(11), comment='#数量#')
    captcha = Column(String(10), comment='#验证码#')
    refuse_reason = Column(String(500), comment='#拒绝进场原因#')
    customer_exit_flag = Column(TINYINT(1), server_default=text("'0'"), comment='#客户是否已退场#')
    tenant_exit_flag = Column(TINYINT(1), server_default=text("'0'"), comment='#商户是否已退场#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')
    device_detail_id = Column(BIGINT(20), comment='#设备明细id#')


class BExitDevice(Base):
    __tablename__ = 'b_exit_device'
    __table_args__ = {'comment': '退场设备表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    exit_id = Column(BIGINT(20), nullable=False, comment='#退场单表id#')
    device_category_id = Column(BIGINT(20), nullable=False, comment='#设备品类id#')
    device_category_name = Column(String(50), nullable=False, comment='#设备品类名称#')
    brand_id = Column(BIGINT(20), comment='#品牌id#')
    brand_name = Column(String(50), comment='#品牌名称#')
    model = Column(String(200), comment='#型号#')
    exit_num = Column(INTEGER(11), comment='#退场数量#')
    apply_exit_num = Column(INTEGER(11), comment='#申请退场数量#')
    actual_exit_num = Column(INTEGER(11), comment='#实际退场数量#')
    description = Column(String(500), comment='说明')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BExitDeviceDetail(Base):
    __tablename__ = 'b_exit_device_detail'
    __table_args__ = {'comment': '退场设备明细表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    exit_id = Column(BIGINT(20), nullable=False, comment='#退场表id#')
    exit_device_id = Column(BIGINT(20), nullable=False, comment='#退场设备表id#')
    enter_id = Column(BIGINT(20), nullable=False, comment='#进场单id#')
    num = Column(INTEGER(11), nullable=False, comment='#数量#')
    follow_machine_accessories = Column(String(1000), comment='#随机附件#')
    acceptance_instructions = Column(String(1000), comment='#验收情况#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BExitDeviceParameter(Base):
    __tablename__ = 'b_exit_device_parameter'
    __table_args__ = {'comment': '退场设备参数表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    exit_id = Column(BIGINT(20), comment='#退场单id#')
    exit_device_id = Column(BIGINT(20), comment='#退场设备id#')
    device_category_id = Column(BIGINT(20), comment='#设备品类id#')
    device_category_name = Column(String(50), comment='#设备品类名称#')
    device_param_id = Column(BIGINT(20), comment='#设备规格参数id#')
    device_param_name = Column(String(50), comment='#设备规格参数名称#')
    device_param_value = Column(DECIMAL(18, 2), comment='#参数值#')
    unit_id = Column(BIGINT(20), comment='#计量单位id#')
    unit_name = Column(String(25), comment='#计量单位#')
    unit_en_name = Column(String(25), comment='#英文计量单位#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BExitFile(Base):
    __tablename__ = 'b_exit_file'
    __table_args__ = {'comment': '退场单附件表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键ID#')
    exit_id = Column(BIGINT(20), comment='#退场表id#b_exit_info.id')
    type = Column(TINYINT(4), comment='#附件类型#ENUM#1:退场申请:EXIT_APPLY,2:退场签字单:EXIT_SIGNATURE#')
    file_id = Column(BIGINT(20), comment='#文件ID#')
    file_name = Column(String(200), comment='#文件名#')
    file_url = Column(String(1000), comment='#文件URL#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BExitInfo(Base):
    __tablename__ = 'b_exit_info'
    __table_args__ = {'comment': '客户退场单表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    code = Column(String(50), nullable=False, comment='#退场单编号#')
    status = Column(TINYINT(4), nullable=False, comment='#状态#ENUM#1:待平台审核:WAIT_PLATFORM_AUDIT,2:待退场交接:WAIT_EXIT_HANDOVER,3:待客户确认:WAIT_CUSTOMER_CONFIRM,4:完成:FINISH,5:审核不通过:AUDIT_FAILED,6:关闭:CLOSE#')
    customer_id = Column(BIGINT(20), nullable=False, comment='#客户id#')
    customer_name = Column(String(50), nullable=False, comment='#客户名称#')
    customer_contract_id = Column(BIGINT(20), nullable=False, comment='#租赁合同id#')
    customer_contract_code = Column(String(50), nullable=False, comment='#租赁合同编号#')
    customer_contract_name = Column(String(100), nullable=False, comment='#租赁合同名称#')
    customer_order_id = Column(BIGINT(20), comment='#租赁订单id#')
    customer_order_code = Column(String(50), comment='#租赁订单编号#')
    project_id = Column(BIGINT(20), nullable=False, comment='#工程id#')
    project_name = Column(String(100), nullable=False, comment='#工程名称#')
    site_leader = Column(String(50), nullable=False, comment='#现场负责人#')
    site_leader_phone = Column(String(50), nullable=False, comment='#现场负责人电话#')
    plan_exit_time = Column(DateTime, nullable=False, comment='#计划退场时间#')
    actual_exit_time = Column(DateTime, comment='#实际退场时间#')
    handover_id = Column(BIGINT(20), comment='#现场交接员id#')
    handover_name = Column(String(50), comment='#现场交接员名称#')
    handover_phone = Column(String(50), comment='#现场交接员电话#')
    customer_exit_code = Column(String(50), comment='#客户退场单号#')
    province_code = Column(String(50), comment='#省份code#')
    province_name = Column(String(100), comment='#省份名称#')
    city_code = Column(String(50), comment='#城市code#')
    city_name = Column(String(100), comment='#城市名称#')
    district_code = Column(String(50), comment='#区域code#')
    district_name = Column(String(100), comment='#区域名称#')
    address = Column(String(100), comment='#施工地址#')
    detail_desc = Column(String(500), comment='#详细说明#')
    num = Column(INTEGER(11), comment='#数量#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BExitNoticeDevice(Base):
    __tablename__ = 'b_exit_notice_device'
    __table_args__ = {'comment': '退场通知单设备表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    exit_notice_id = Column(BIGINT(20), nullable=False, comment='#退场通知单id#')
    device_category_id = Column(BIGINT(20), nullable=False, comment='#设备品类id#')
    device_category_name = Column(String(50), nullable=False, comment='#设备品类名称#')
    brand_id = Column(BIGINT(20), comment='#品牌id#')
    brand_name = Column(String(50), comment='#品牌名称#')
    model = Column(String(200), comment='#型号#')
    exit_num = Column(INTEGER(11), comment='#退场数量#')
    actual_exit_num = Column(INTEGER(11), comment='#实际退场数量#')
    description = Column(String(500), comment='说明')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')
    apply_exit_num = Column(INTEGER(11), comment='#申请退场数量#')


class BExitNoticeDeviceDetail(Base):
    __tablename__ = 'b_exit_notice_device_detail'
    __table_args__ = {'comment': '退场通知单设备明细表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    exit_notice_id = Column(BIGINT(20), nullable=False, comment='#退场通知单表id#')
    exit_notice_device_id = Column(BIGINT(20), nullable=False, comment='#退场通知单设备表id#')
    enter_id = Column(BIGINT(20), nullable=False, comment='#进场单id#')
    num = Column(INTEGER(11), nullable=False, comment='#数量#')
    follow_machine_accessories = Column(String(1000), comment='#随机附件#')
    acceptance_instructions = Column(String(1000), comment='#验收情况#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BExitNoticeDeviceParameter(Base):
    __tablename__ = 'b_exit_notice_device_parameter'
    __table_args__ = {'comment': '退场通知设备参数表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    exit_notice_id = Column(BIGINT(20), comment='#退场单通知单id#')
    exit_notice_device_id = Column(BIGINT(20), comment='#退场通知单设备id#')
    device_category_id = Column(BIGINT(20), comment='#设备品类id#')
    device_category_name = Column(String(50), comment='#设备品类名称#')
    device_param_id = Column(BIGINT(20), comment='#设备规格参数id#')
    device_param_name = Column(String(50), comment='#设备规格参数名称#')
    device_param_value = Column(DECIMAL(18, 2), comment='#参数值#')
    unit_id = Column(BIGINT(20), comment='#计量单位id#')
    unit_name = Column(String(25), comment='#计量单位#')
    unit_en_name = Column(String(25), comment='#英文计量单位#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BExitNoticeFile(Base):
    __tablename__ = 'b_exit_notice_file'
    __table_args__ = {'comment': '退场通知单附件表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键ID#')
    exit_notice_id = Column(BIGINT(20), comment='#退场通知单id#b_exit_notice_info.id')
    file_id = Column(BIGINT(20), comment='#文件ID#')
    file_name = Column(String(200), comment='#文件名#')
    file_url = Column(String(1000), comment='#文件URL#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BExitNoticeInfo(Base):
    __tablename__ = 'b_exit_notice_info'
    __table_args__ = {'comment': '退场通知单表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    status = Column(TINYINT(4), nullable=False, comment='#状态#ENUM#1:待退场:WAIT_EXIT,2:已退场:EXITED#')
    code = Column(String(50), nullable=False, comment='#退场通知单编号#')
    exit_id = Column(BIGINT(20), nullable=False, comment='#退场单id#')
    exit_code = Column(String(50), nullable=False, comment='#退场单编号#')
    customer_exit_code = Column(String(50), comment='#客户退场单号#')
    customer_id = Column(BIGINT(20), nullable=False, comment='#客户id#')
    customer_name = Column(String(50), nullable=False, comment='#客户名称#')
    tenant_id = Column(BIGINT(20), nullable=False, comment='#商户id#')
    tenant_name = Column(String(50), nullable=False, comment='#商户名称#')
    project_id = Column(BIGINT(20), nullable=False, comment='#工程id#')
    project_name = Column(String(100), nullable=False, comment='#工程名称#')
    request_exit_time = Column(DateTime, comment='#要求退场时间#')
    actual_exit_time = Column(DateTime, comment='#实际退场时间#')
    site_leader = Column(String(50), nullable=False, comment='#现场负责人#')
    site_leader_phone = Column(String(50), nullable=False, comment='#现场负责人电话#')
    handover_id = Column(BIGINT(20), comment='#现场交接员id#')
    handover_name = Column(String(50), comment='#现场交接员名称#')
    handover_phone = Column(String(50), comment='#现场交接员电话#')
    province_code = Column(String(50), comment='#省份code#')
    province_name = Column(String(100), comment='#省份名称#')
    city_code = Column(String(50), comment='#城市code#')
    city_name = Column(String(100), comment='#城市名称#')
    district_code = Column(String(50), comment='#区域code#')
    district_name = Column(String(100), comment='#区域名称#')
    address = Column(String(100), comment='#施工地址#')
    num = Column(INTEGER(11), comment='#数量#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BGradeTopic(Base):
    __tablename__ = 'b_grade_topic'
    __table_args__ = {'comment': '评分题目表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    name = Column(String(200), comment='#题目名称#')
    score = Column(DECIMAL(18, 2), comment='#分数#')
    parent_id = Column(BIGINT(20), comment='#父id#')
    level = Column(TINYINT(4), comment='#层级（大类/题目/选项）#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BGradeTopicTenantSnapshoot(Base):
    __tablename__ = 'b_grade_topic_tenant_snapshoot'
    __table_args__ = {'comment': '商户-评分题目快照表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    tenant_id = Column(BIGINT(20), comment='#商户id#')
    name = Column(String(200), comment='#题目名称#')
    score = Column(DECIMAL(18, 2), comment='#分数#')
    parent_id = Column(BIGINT(20), comment='#父id#')
    level = Column(TINYINT(4), comment='#层级（大类/题目/选项）#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BMasterBank(Base):
    __tablename__ = 'b_master_bank'
    __table_args__ = {'comment': '机手账户管理表'}

    id = Column(BIGINT(22), primary_key=True, comment='#主键id#')
    master_id = Column(BIGINT(22), comment='#机手ID#')
    bank_account = Column(String(50), comment='#银行账号#')
    bank_name = Column(String(100), comment='#开户行名称#')
    bank_user_name = Column(String(50), comment='#银行户名#')
    default_flag = Column(TINYINT(1), server_default=text("'0'"), comment='#是否默认#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BMasterDevice(Base):
    __tablename__ = 'b_master_device'
    __table_args__ = {'comment': '机手操作机型表'}

    id = Column(BIGINT(22), primary_key=True, comment='#主键ID#')
    master_id = Column(BIGINT(22), comment='#机手id#')
    category_id = Column(BIGINT(22), comment='#设备品类id#')
    category_name = Column(String(100), comment='#品类nameid#')
    brand_id = Column(BIGINT(22), comment='#品牌id#')
    device_type = Column(String(100), comment='#设备型号#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='逻辑删除#ENUM#0:正常,1:删除')
    brand_name = Column(String(100), comment='#品牌name#')


class BMasterDeviceParameter(Base):
    __tablename__ = 'b_master_device_parameter'
    __table_args__ = {'comment': '机手设备规格参数表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    master_id = Column(BIGINT(22), comment='#机手id#')
    master_device_id = Column(BIGINT(22), comment='#机手设备id#')
    device_param_id = Column(BIGINT(20), comment='#设备规格参数id#')
    device_param_name = Column(String(50), comment='#设备规格参数名称#')
    device_param_value = Column(DECIMAL(18, 2), comment='#参数值#')
    unit_id = Column(BIGINT(20), comment='#计量单位id#')
    unit_name = Column(String(25), comment='#计量单位（冗余）#')
    unit_en_name = Column(String(25), comment='#英文计量单位（冗余）#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    modifier = Column(String(25), server_default=text("''"), comment='修改人')
    update_time = Column(DateTime, comment='修改时间')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='逻辑删除#ENUM#0:正常,1:删除')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')


class BMasterEnterprise(Base):
    __tablename__ = 'b_master_enterprise'
    __table_args__ = {'comment': '机手企业管理表'}

    id = Column(BIGINT(22), primary_key=True, comment='#主键id#')
    master_id = Column(BIGINT(22), comment='#机手ID#')
    enterprise_id = Column(BIGINT(22), comment='#商户ID/客户ID#')
    enterprise_type = Column(TINYINT(4), server_default=text("'0'"), comment='#企业类型:商户/客户#')
    status = Column(TINYINT(4), server_default=text("'0'"), comment='#状态#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BMasterFile(Base):
    __tablename__ = 'b_master_file'
    __table_args__ = {'comment': '机手附件表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键ID#')
    master_id = Column(BIGINT(20), comment='#机手信息id#')
    type = Column(TINYINT(4), comment='#附件类型#ENUM#1:证书:CERTIFICATE')
    file_id = Column(BIGINT(20), comment='#文件ID#')
    file_name = Column(String(200), comment='#文件名#')
    file_url = Column(String(1000), comment='#文件URL#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BMasterInfo(Base):
    __tablename__ = 'b_master_info'
    __table_args__ = {'comment': '机手信息表'}

    id = Column(BIGINT(22), primary_key=True, comment='#主键ID#')
    head_image = Column(String(500), comment='#头像#')
    head_image_id = Column(BIGINT(22), comment='#头像ID#')
    name = Column(String(255), comment='#名称#')
    user_code = Column(String(20), comment='#用户ID#')
    phone = Column(String(20), comment='#手机号#')
    sex = Column(TINYINT(1), comment='#性别：1:男；0:女#')
    id_card = Column(String(50), comment='#身份证#')
    province_code = Column(String(20), comment='#省份code#')
    province_name = Column(String(100), comment='#省份名称#')
    city_code = Column(String(20), comment='#城市code#')
    city_name = Column(String(100), comment='#城市名称#')
    district_code = Column(String(20), comment='#地区code#')
    district_name = Column(String(100), comment='#区域名称#')
    tenant_id = Column(BIGINT(22), comment='#商户ID#')
    state = Column(String(20), server_default=text("'0'"), comment='#USE-启用，NO-USE-不启用')
    address = Column(String(255), comment='#地址#')
    black_flag = Column(TINYINT(1), server_default=text("'0'"), comment='#是否加入黑名单#')
    tech_msg = Column(String(255), comment='#技术说明#')
    card_front_file = Column(String(1000), comment='#身份证正面#')
    card_back_file = Column(String(1000), comment='#身份证背面#')
    card_front_file_id = Column(BIGINT(22), comment='#身份证正面文件id#')
    card_front_file_name = Column(String(200), comment='#身份证正面文件名#')
    card_back_file_id = Column(BIGINT(22), comment='#身份证背面文件id#')
    card_back_file_name = Column(String(200), comment='#身份证背面文件名#')
    certificate = Column(String(1000), comment='#证书#')
    certificate_file_id = Column(BIGINT(22), comment='#证书ID#')
    certificate_file_name = Column(String(255), comment='#证书文件名称#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')
    user_id = Column(BIGINT(22), comment='#用户表id#')
    drive_card = Column(String(100), comment='#驾驶证号#')
    perfect_data = Column(TINYINT(1), server_default=text("'0'"), comment='#是否完善资料#')


class BMasterWorkarea(Base):
    __tablename__ = 'b_master_workarea'

    id = Column(BIGINT(22), primary_key=True, comment='#主键ID#')
    master_id = Column(BIGINT(22), comment='#机手ID#')
    province_code = Column(String(20), comment='#省份#')
    city_code = Column(String(20), comment='#城市#')
    district_code = Column(String(20), comment='#区域#')
    province_name = Column(String(50), comment='#省份描述#')
    city_name = Column(String(50), comment='#城市描述#')
    district_name = Column(String(50), comment='#区域描述#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='逻辑删除#ENUM#0:正常,1:删除')


class BOperateLog(Base):
    __tablename__ = 'b_operate_log'
    __table_args__ = {'comment': '履约操作日志表'}

    id = Column(BIGINT(22), primary_key=True, comment='#主键id#')
    log_type = Column(INTEGER(3), comment='#日志类型#')
    business_id = Column(BIGINT(22), comment='#业务表id#')
    operator = Column(BIGINT(22), comment='#操作人#')
    state = Column(INTEGER(3), comment='#状态#')
    msg = Column(String(255), comment='#说明#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


t_b_pay_bill = Table(
    'b_pay_bill', metadata,
    Column('id', BIGINT(20), comment='#应收账单表id#'),
    Column('tenant', String(100), comment='#商户名称#'),
    Column('tenant_id', BIGINT(20), comment='#商户#'),
    Column('constract', String(100), comment='#合同名称#'),
    Column('constract_id', BIGINT(20), comment='#合同id#'),
    Column('order_no', String(50), comment='#订单号#'),
    Column('device_id', BIGINT(20), comment='#设备品类ID#'),
    Column('device_type', String(50), comment='#设备型号#'),
    Column('device_no', String(50), comment='#整机序列号#'),
    Column('bill_cycle', String(50), comment='#账单周期#'),
    Column('bill_month', String(50), comment='#账单月份#'),
    Column('start_rent_day', Date, comment='#起租日#'),
    Column('end_rent_day', Date, comment='#截止日#'),
    Column('rent_state', TINYINT(4), comment='#租赁状态#'),
    Column('rent_type', TINYINT(4), comment='#租赁方式#'),
    Column('pay_type', TINYINT(4), comment='#结算方式#'),
    Column('standard', INTEGER(10), server_default=text("'0'"), comment='#月租标准#'),
    Column('standard_hours', INTEGER(5), server_default=text("'0'"), comment='#月租标准工作小时数#'),
    Column('day_price', DECIMAL(10, 2), server_default=text("'0.00'"), comment='#日单价#'),
    Column('extra_price', DECIMAL(10, 2), server_default=text("'0.00'"), comment='#超时单价#'),
    Column('pause_days', INTEGER(5), server_default=text("'0'"), comment='#设备报停天数#'),
    Column('actual_days', INTEGER(5), server_default=text("'0'"), comment='#实际租赁天数#'),
    Column('actual_hours', INTEGER(5), server_default=text("'0'"), comment='#实际工作小时数#'),
    Column('extra_hours', INTEGER(5), server_default=text("'0'"), comment='#超小时数#'),
    Column('message', String(255), comment='#说明#'),
    Column('status', TINYINT(4), comment='#账单状态#'),
    Column('version', INTEGER(11), comment='#数据版本#'),
    Column('creator_id', BIGINT(20), comment='#创建人id#'),
    Column('creator', String(25), server_default=text("''"), comment='#创建人#'),
    Column('create_time', DateTime, comment='#创建时间#'),
    Column('modifier_id', BIGINT(20), comment='#修改人id#'),
    Column('modifier', String(25), server_default=text("''"), comment='#修改人#'),
    Column('update_time', DateTime, comment='#修改时间#'),
    Column('delete_flag', TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#'),
    comment='平台应付账单表'
)


t_b_pay_order = Table(
    'b_pay_order', metadata,
    Column('id', BIGINT(20), comment='#收款单表ID#'),
    Column('target_name', String(100), comment='#客商名称#'),
    Column('target_id', BIGINT(20), comment='#客商ID#'),
    Column('target_type', TINYINT(4), comment='#单位类型#'),
    Column('contract_id', BIGINT(20), comment='#合同ID#'),
    Column('contract_no', String(100), comment='#合同编号#'),
    Column('order_no', String(100), comment='#订单编号#'),
    Column('order_id', BIGINT(20), comment='#订单ID#'),
    Column('gather_account_type', TINYINT(4), comment='#收款账户类型#'),
    Column('gather_account_name', String(100), comment='#收款账户类型#'),
    Column('gather_account_no', String(50), comment='#收款账号#'),
    Column('gather_account_id', BIGINT(20), comment='#收款账户ID#'),
    Column('gather_bank_name', String(100), comment='#收款银行#'),
    Column('company', String(255), comment='#公司#'),
    Column('all_money', DECIMAL(10, 2), comment='#合计金额#'),
    Column('gather_msg', String(255), comment='#收款备注#'),
    Column('status', TINYINT(4), comment='#收款状态#'),
    Column('order_type', TINYINT(4), comment='#收款单类型#'),
    Column('pay_time', DateTime, comment='#收款时间#'),
    Column('pay_money', DECIMAL(10, 2), comment='#付款金额#'),
    Column('pay_account_type', TINYINT(4), comment='#付款类型#'),
    Column('pay_account_name', String(100), comment='#付款账号名#'),
    Column('pay_account_no', String(100), comment='#账户#'),
    Column('pay_bank_name', String(100), comment='#付款银行#'),
    Column('pay_no', String(50), comment='#付款流水号#'),
    Column('pay_msg', String(255), comment='#付款备注#'),
    Column('audit_msg', String(255), comment='#审核意见#'),
    Column('version', INTEGER(11), comment='#数据版本#'),
    Column('creator_id', BIGINT(20), comment='#创建人id#'),
    Column('creator', String(25), server_default=text("''"), comment='#创建人#'),
    Column('create_time', DateTime, comment='#创建时间#'),
    Column('modifier_id', BIGINT(20), comment='#修改人id#'),
    Column('modifier', String(25), server_default=text("''"), comment='#修改人#'),
    Column('update_time', DateTime, comment='#修改时间#'),
    Column('delete_flag', TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#'),
    comment='付款单信息表'
)


t_b_pay_receive_file = Table(
    'b_pay_receive_file', metadata,
    Column('id', BIGINT(20), comment='#主键ID#'),
    Column('order_id', BIGINT(20), comment='#收付款单ID#'),
    Column('order_type', TINYINT(4), comment='#收付款单类型#'),
    Column('file_id', BIGINT(20), comment='#文件ID#'),
    Column('file_url', String(255), comment='#文件url#'),
    Column('extension', String(100), comment='#文件扩展名#'),
    Column('file_name', String(255), comment='#文件名#'),
    Column('version', INTEGER(11), comment='#数据版本#'),
    Column('creator_id', BIGINT(20), comment='#创建人id#'),
    Column('creator', String(25), server_default=text("''"), comment='#创建人#'),
    Column('create_time', DateTime, comment='#创建时间#'),
    Column('modifier_id', BIGINT(20), comment='#修改人id#'),
    Column('modifier', String(25), server_default=text("''"), comment='#修改人#'),
    Column('update_time', DateTime, comment='#修改时间#'),
    Column('delete_flag', TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#'),
    comment='收付款单文件表\n'
)


t_b_pay_sub_order = Table(
    'b_pay_sub_order', metadata,
    Column('id', BIGINT(20), comment='#核销订单表ID#'),
    Column('pay_bill_id', BIGINT(20), comment='#应收账单ID#'),
    Column('pay_bill_no', BIGINT(20), comment='#应收账单编号#'),
    Column('device_no', BIGINT(20), comment='#整机序列号#'),
    Column('bill_month', Date, comment='#账单月#'),
    Column('contract', String(100), comment='#合同编号#'),
    Column('contract_id', BIGINT(20), comment='#合同ID#'),
    Column('order_id', BIGINT(20), comment='#订单ID#'),
    Column('order_no', String(100), comment='#订单编号#'),
    Column('pay_money', DECIMAL(12, 2), comment='#应收金额=应收账单的结算金额#'),
    Column('receive_money', DECIMAL(12, 2), comment='#已收金额#'),
    Column('wait_money', DECIMAL(12, 2), comment='#待收金额#'),
    Column('check_money', DECIMAL(12, 2), comment='#已核销金额#'),
    Column('wait_check_money', DECIMAL(12, 2), comment='#待核销金额#'),
    Column('current_money', DECIMAL(12, 2), comment='#本次收款#'),
    Column('current_check', DECIMAL(12, 2), comment='#本次核销#'),
    Column('type', TINYINT(4), comment='#子单据类型#'),
    Column('version', INTEGER(11), comment='#数据版本#'),
    Column('creator_id', BIGINT(20), comment='#创建人id#'),
    Column('creator', String(25), server_default=text("''"), comment='#创建人#'),
    Column('create_time', DateTime, comment='#创建时间#'),
    Column('modifier_id', BIGINT(20), comment='#修改人id#'),
    Column('modifier', String(25), server_default=text("''"), comment='#修改人#'),
    Column('update_time', DateTime, comment='#修改时间#'),
    Column('delete_flag', TINYINT(4), server_default=text("'0'"), comment='逻辑删除#ENUM#0:正常,1:删除'),
    comment='核销订单记录表'
)


t_b_pre_order_item = Table(
    'b_pre_order_item', metadata,
    Column('id', BIGINT(20), comment='#主键ID#'),
    Column('item_name', String(100), comment='#费用名称#'),
    Column('item_code', String(50), comment='#费用code#'),
    Column('money', DECIMAL(10, 2), comment='#金额#'),
    Column('message', String(255), comment='#说明#'),
    Column('type', TINYINT(4), comment='#类型#'),
    Column('version', INTEGER(11), comment='#数据版本#'),
    Column('creator_id', BIGINT(20), comment='#创建人id#'),
    Column('creator', String(25), server_default=text("''"), comment='#创建人#'),
    Column('create_time', DateTime, comment='#创建时间#'),
    Column('modifier_id', BIGINT(20), comment='#修改人id#'),
    Column('modifier', String(25), server_default=text("''"), comment='#修改人#'),
    Column('update_time', DateTime, comment='#修改时间#'),
    Column('delete_flag', TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#'),
    comment='收付款单费用明细表'
)


class BProjectInfo(Base):
    __tablename__ = 'b_project_info'
    __table_args__ = {'comment': '工程信息表'}

    id = Column(BIGINT(22), primary_key=True, comment='#主键ID#')
    project_code = Column(String(50), comment='#工程编码#')
    project_name = Column(String(255), comment='#项目名称#')
    address_title = Column(String(100), comment='#定位地址#')
    address = Column(String(200), comment='#项目地址#')
    lat = Column(String(20), comment='#经度#')
    lng = Column(String(20), comment='#纬度#')
    district_code = Column(String(50), comment='#区域code#')
    district_name = Column(String(50), comment='#区域名称#')
    city_code = Column(String(50), comment='#城市code#')
    city_name = Column(String(50), comment='#城市名称#')
    province_code = Column(String(50), comment='#省份id#')
    province_name = Column(String(50), comment='#省份名称#')
    scale = Column(String(50), comment='#工程规模#')
    build_field = Column(String(255), comment='#建筑领域#')
    message = Column(String(255), comment='#备注#')
    region_id = Column(BIGINT(22), comment='#销售大区ID#')
    investment = Column(DECIMAL(18, 2), comment='#单期投资规模（亿）#')
    build_start = Column(Date, comment='#建设开始日期#')
    build_end = Column(Date, comment='#建设结束日期#')
    other_address = Column(String(256), comment='#补充地址#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='逻辑删除#ENUM#0:正常,1:删除')


class BProjectPicture(Base):
    __tablename__ = 'b_project_picture'
    __table_args__ = {'comment': '工程图片表'}

    id = Column(BIGINT(22), primary_key=True, comment='#主键ID#')
    project_id = Column(BIGINT(22), comment='#工程ID#')
    url = Column(String(1000), comment='#文件链接#')
    file_id = Column(BIGINT(22), comment='#文件ID#')
    file_name = Column(String(200), comment='#文件名#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


t_b_receive_bill = Table(
    'b_receive_bill', metadata,
    Column('id', BIGINT(20), comment='#应收账单表id#'),
    Column('customer', String(100), comment='#客户名称#'),
    Column('customer_id', BIGINT(20), comment='#客户ID#'),
    Column('constract_code', String(100), comment='#合同编号#'),
    Column('constract_id', BIGINT(20), comment='#合同id#'),
    Column('customer_order_code', String(50), comment='#订单号#'),
    Column('customer_order_id', BIGINT(20), comment='#订单ID#'),
    Column('device_category_id', BIGINT(20), comment='#设备品类ID#'),
    Column('device_no', String(50), comment='#整机序列号#'),
    Column('bill_cycle_start', DateTime, comment='#账单周期(开始日期)#'),
    Column('bill_cycle_end', DateTime, comment='#账单周期（结束日期）#'),
    Column('bill_month', String(50), comment='#账单月份#'),
    Column('start_rent_day', Date, comment='#起租日#'),
    Column('end_rent_day', Date, comment='#截止日#'),
    Column('rent_state', TINYINT(4), comment='#租赁状态#'),
    Column('leasing_model', TINYINT(4), comment='#租赁方式#'),
    Column('valuation_way', TINYINT(4), comment='#结算方式#'),
    Column('month_days', DECIMAL(10, 2), server_default=text("'0.00'"), comment='#月租标准#'),
    Column('month_hours', DECIMAL(10, 2), server_default=text("'0.00'"), comment='#月租标准工作小时数#'),
    Column('day_price', DECIMAL(10, 2), server_default=text("'0.00'"), comment='#日单价#'),
    Column('extra_price', DECIMAL(10, 2), server_default=text("'0.00'"), comment='#超时单价#'),
    Column('pause_days', DECIMAL(10, 2), server_default=text("'0.00'"), comment='#设备报停天数#'),
    Column('actual_days', DECIMAL(10, 2), server_default=text("'0.00'"), comment='#实际租赁天数#'),
    Column('actual_hours', DECIMAL(10, 2), server_default=text("'0.00'"), comment='#实际工作小时数#'),
    Column('actual_machine_teams', DECIMAL(10, 2), comment='#实际台班租赁数#'),
    Column('extra_hours', DECIMAL(10, 2), server_default=text("'0.00'"), comment='#超小时数#'),
    Column('message', String(255), comment='#说明#'),
    Column('count', DECIMAL(10, 2), comment='#台班数#'),
    Column('status', TINYINT(4), comment='#账单状态#'),
    Column('hour_price', DECIMAL(10, 2), comment='#小时单价#'),
    Column('price', DECIMAL(10, 2), comment='#台班单价#'),
    Column('device_category', String(255), comment='#设备品类#'),
    Column('version', INTEGER(11), comment='#数据版本#'),
    Column('creator_id', BIGINT(20), comment='#创建人id#'),
    Column('creator', String(25), server_default=text("''"), comment='#创建人#'),
    Column('create_time', DateTime, comment='#创建时间#'),
    Column('modifier_id', BIGINT(20), comment='#修改人id#'),
    Column('modifier', String(25), server_default=text("''"), comment='#修改人#'),
    Column('update_time', DateTime, comment='#修改时间#'),
    Column('delete_flag', TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#'),
    Index('unique_bill', 'constract_id', 'device_category_id', 'device_no', 'customer_order_id', unique=True),
    comment='平台应收账单表'
)


t_b_receive_order = Table(
    'b_receive_order', metadata,
    Column('id', BIGINT(20), comment='#收款单表ID#'),
    Column('target_name', String(100), comment='#客商名称#'),
    Column('target_id', BIGINT(20), comment='#客商ID#'),
    Column('target_type', TINYINT(4), comment='#单位类型#'),
    Column('contract_id', BIGINT(20), comment='#合同ID#'),
    Column('contract_no', String(100), comment='#合同编号#'),
    Column('order_no', String(100), comment='#订单编号#'),
    Column('order_id', BIGINT(20), comment='#订单ID#'),
    Column('account_type', TINYINT(4), comment='#收款账户类型#'),
    Column('account_name', String(100), comment='#收款账户类型#'),
    Column('account_no', String(50), comment='#收款账号#'),
    Column('account_id', BIGINT(20), comment='#收款账户ID#'),
    Column('bank_name', String(100), comment='#收款银行#'),
    Column('company', String(255), comment='#公司#'),
    Column('receive_money', DECIMAL(10, 2), comment='#合计金额#'),
    Column('msg', String(255), comment='#收款备注#'),
    Column('status', TINYINT(4), comment='#收款状态#'),
    Column('order_type', TINYINT(4), comment='#收款单类型#'),
    Column('pay_time', DateTime, comment='#收款时间#'),
    Column('pay_money', DECIMAL(10, 2), comment='#付款金额#'),
    Column('pay_account_type', TINYINT(4), comment='#付款类型#'),
    Column('pay_account_name', String(100), comment='#付款账号名#'),
    Column('pay_account_no', String(100), comment='#账户#'),
    Column('pay_bank_name', String(100), comment='#付款银行#'),
    Column('pay_no', String(50), comment='#付款流水号#'),
    Column('pay_msg', String(255), comment='#付款备注#'),
    Column('sub_money', DECIMAL(10, 2), comment='#核销金额#'),
    Column('audit_msg', String(255), comment='#审核意见#'),
    Column('version', INTEGER(11), comment='#数据版本#'),
    Column('creator_id', BIGINT(20), comment='#创建人id#'),
    Column('creator', String(25), server_default=text("''"), comment='#创建人#'),
    Column('create_time', DateTime, comment='#创建时间#'),
    Column('modifier_id', BIGINT(20), comment='#修改人id#'),
    Column('modifier', String(25), server_default=text("''"), comment='#修改人#'),
    Column('update_time', DateTime, comment='#修改时间#'),
    Column('delete_flag', TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#'),
    comment='付款单信息表'
)


t_b_receive_sub_order = Table(
    'b_receive_sub_order', metadata,
    Column('id', BIGINT(20), comment='#核销订单表ID#'),
    Column('receive_bill_id', BIGINT(20), comment='#应收账单ID#'),
    Column('receive_bill_no', BIGINT(20), comment='#应收账单编号#'),
    Column('device_no', BIGINT(20), comment='#整机序列号#'),
    Column('bill_month', Date, comment='#账单月#'),
    Column('contract', String(100), comment='#合同编号#'),
    Column('contract_id', BIGINT(20), comment='#合同ID#'),
    Column('order_id', BIGINT(20), comment='#订单ID#'),
    Column('order_no', String(100), comment='#订单编号#'),
    Column('pay_money', DECIMAL(12, 2), comment='#应收金额=应收账单的结算金额#'),
    Column('receive_money', DECIMAL(12, 2), comment='#已收金额#'),
    Column('wait_money', DECIMAL(12, 2), comment='#待收金额#'),
    Column('check_money', DECIMAL(12, 2), comment='#已核销金额#'),
    Column('wait_check_money', DECIMAL(12, 2), comment='#待核销金额#'),
    Column('current_money', DECIMAL(12, 2), comment='#本次收款#'),
    Column('current_check', DECIMAL(12, 2), comment='#本次核销#'),
    Column('type', TINYINT(4), comment='#子单据类型#'),
    Column('version', INTEGER(11), comment='#数据版本#'),
    Column('creator_id', BIGINT(20), comment='#创建人id#'),
    Column('creator', String(25), server_default=text("''"), comment='#创建人#'),
    Column('create_time', DateTime, comment='#创建时间#'),
    Column('modifier_id', BIGINT(20), comment='#修改人id#'),
    Column('modifier', String(25), server_default=text("''"), comment='#修改人#'),
    Column('update_time', DateTime, comment='#修改时间#'),
    Column('delete_flag', TINYINT(4), server_default=text("'0'"), comment='逻辑删除#ENUM#0:正常,1:删除'),
    comment='核销订单记录表'
)


class BRegionInfo(Base):
    __tablename__ = 'b_region_info'
    __table_args__ = {'comment': '大区表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    type = Column(TINYINT(4), comment='#大区类型#ENUM#1:销售大区,2:招商大区#')
    name = Column(String(50), nullable=False, comment='#大区名称#')
    dept_id = Column(BIGINT(20), nullable=False, comment='#部门id#')
    dept_name = Column(String(50), nullable=False, comment='#部门名称#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BReplaceOrder(Base):
    __tablename__ = 'b_replace_order'
    __table_args__ = {'comment': '更换设备单'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    project_id = Column(BIGINT(20), comment='#项目id#')
    code = Column(String(50), comment='#编号#')
    type = Column(TINYINT(4), server_default=text("'0'"), comment='#更换类型#ENUM#0:设备损坏暂时无法维修:damage#')
    state = Column(TINYINT(4), server_default=text("'0'"), comment='#订单状态#ENUM#0:未审核:wait_approve,1:已审核:approved,2:审核不通过:no_pass,3:关闭:shutdown,4:调度完成:dispatch#')
    director = Column(String(32), comment='#现场负责人#')
    director_phone = Column(String(32), comment='#现场负责人联系电话#')
    reason = Column(String(255), comment='#更换原因#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')
    customer_contract_code = Column(String(100), comment='#合同编号#')
    order_code = Column(String(100), comment='#订单编号#')
    project_name = Column(String(100), comment='#项目名称#')
    replace_time = Column(DateTime, comment='#变更需求日#')
    customer_id = Column(BIGINT(22), comment='#客户id#')
    customer_name = Column(String(100), comment='#客户名称#')
    address = Column(String(100), comment='#施工地址#')
    new_device_tenant_id = Column(BIGINT(22), comment='#新设备商户id#')
    new_device_tenant_name = Column(String(100), comment='#新设备商户name#')
    new_device_tenant_order_id = Column(BIGINT(22), comment='#新设备商户订单id#')
    new_device_tenant_order_code = Column(String(100), comment='#新设备商户订单code#')
    new_device_tenant_contract_id = Column(BIGINT(22), comment='#新设备商户合同id#')
    new_device_tenant_contract_code = Column(String(100), comment='#新设备商户合同code#')
    province_code = Column(String(50), comment='#省份code#')
    province_name = Column(String(100), comment='#省份名称#')
    city_code = Column(String(50), comment='#城市code#')
    city_name = Column(String(100), comment='#城市名称#')
    district_code = Column(String(50), comment='#区域code#')
    district_name = Column(String(100), comment='#区域名称#')


class BReplaceOrderDevice(Base):
    __tablename__ = 'b_replace_order_device'
    __table_args__ = {'comment': '更换设备'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    device_detail_id = Column(BIGINT(20), comment='#设备detail id#')
    replace_order_id = Column(BIGINT(20), comment='#更换单id#')
    start_time = Column(DateTime, comment='#更换开始时间#')
    type = Column(TINYINT(4), server_default=text("'0'"), comment='#更换类型#ENUM#0:旧设备:old,1:新设备:new#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')
    car_no = Column(String(32), comment='#车牌号#')
    dispatch_device_detail_id = Column(BIGINT(20), comment='#调度设备表id#')
    category_id = Column(BIGINT(22), comment='#设备品类id#')
    brand_id = Column(BIGINT(22), comment='#品牌id#')
    device_no = Column(String(50), comment='#设备序列号#')
    device_type = Column(String(100), comment='#设备型号#')
    lease_mode = Column(TINYINT(3), comment='#租赁模式#')
    made_time = Column(Date, comment='#出厂日期#')
    enter_info_id = Column(BIGINT(20), comment='#进场信息id#')
    replace_order_device_id = Column(BIGINT(20), comment='#被更换设备id#')
    category_name = Column(String(60), comment='#品类名称#')
    brand_name = Column(String(60), comment='#品牌名称#')
    work_day = Column(INTEGER(11), comment='#工作天数#')
    cost_type = Column(TINYINT(3), comment='#结算方式#')
    tenant_id = Column(BIGINT(22), comment='#商户id#')
    tenant_name = Column(String(100), comment='#商户名称#')
    enter_time = Column(DateTime, comment='#进场时间#')
    enter_info_code = Column(String(100), comment='#进场单号#')


class BReplaceOrderDeviceParameter(Base):
    __tablename__ = 'b_replace_order_device_parameter'
    __table_args__ = {'comment': '更换订单设备参数'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    replace_order_id = Column(BIGINT(20), comment='#更换订单id#')
    replace_order_device_id = Column(BIGINT(20), comment='#更换订单设备id#')
    device_param_id = Column(BIGINT(20), comment='#设备规格参数id#')
    device_param_name = Column(String(50), comment='#设备规格参数名称#')
    device_param_value = Column(String(50), comment='#参数值#')
    unit_id = Column(BIGINT(20), comment='#计量单位id#')
    unit_name = Column(String(25), comment='#计量单位（冗余）#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BReplaceOrderFile(Base):
    __tablename__ = 'b_replace_order_file'

    id = Column(BIGINT(22), primary_key=True, comment='#主键ID#')
    replace_order_id = Column(BIGINT(22), comment='#更换设备单id#')
    file_id = Column(BIGINT(22), comment='#文件ID#')
    file_name = Column(String(200), comment='#文件名#')
    file_url = Column(String(255), comment='#文件URL#')
    extension = Column(String(200), comment='#拓展名#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BReplaceOrderLog(Base):
    __tablename__ = 'b_replace_order_log'
    __table_args__ = {'comment': '更换设备日常'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    replace_order_id = Column(BIGINT(20), comment='#更换单id#')
    state = Column(TINYINT(4), server_default=text("'0'"), comment='#状态#ENUM#0:创建,1:审核,2:审核不通过,3:关闭,4:完成调度#')
    note = Column(String(255), comment='#说明#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BStopOrder(Base):
    __tablename__ = 'b_stop_order'
    __table_args__ = {'comment': '报停单'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    project_id = Column(BIGINT(20), comment='#项目id#')
    code = Column(String(50), comment='#编号#')
    type = Column(TINYINT(4), server_default=text("'0'"), comment='#报停类型#ENUM#0:保修报停:guarantee,1:政策报停:policy,2:节假日报停:holiday#')
    status = Column(TINYINT(4), server_default=text("'0'"), comment='#订单状态#ENUM#0:未审核:wait_approve,1:已审核:approved,2:审核不通过:no_pass,3:关闭:shutdown#')
    stop_name = Column(String(32), comment='#报停人#')
    stop_phone = Column(String(32), comment='#报停人联系电话#')
    reason = Column(String(255), comment='#报停原因#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')
    project_name = Column(String(100), comment='#项目名称#')
    stop_num = Column(INTEGER(11), comment='#报停数量#')
    stop_day = Column(INTEGER(11), comment='#报停天数#')
    customer_id = Column(BIGINT(20), comment='#客户id#')
    customer_name = Column(String(100), comment='#客户名称#')
    start_time = Column(DateTime, comment='#报停开始时间#')
    end_time = Column(DateTime, comment='#报停截止时间#')
    province_code = Column(String(50), comment='#省份code#')
    province_name = Column(String(100), comment='#省份名称#')
    city_code = Column(String(50), comment='#城市code#')
    city_name = Column(String(100), comment='#城市名称#')
    district_code = Column(String(50), comment='#区域code#')
    district_name = Column(String(100), comment='#区域名称#')
    address = Column(String(100), comment='#施工地址#')
    form_type = Column(TINYINT(4), comment='#单据类型#')
    change_reason = Column(String(100), comment='#变更原因#')
    tenant_id = Column(BIGINT(22), comment='#商户id#')
    tenant_name = Column(String(100), comment='#商户name#')
    change_start_time = Column(DateTime, comment='#变更报停开始时间#')
    change_end_time = Column(DateTime, comment='#变更报停结束时间#')
    change_detail = Column(String(1000), comment='#变更详情#')
    customer_contract_code = Column(String(50), comment='#租赁合同编号#')
    customer_contract_id = Column(BIGINT(20), comment='#租赁合同id#')
    customer_contract_name = Column(String(50), comment='#租赁合同名称#')
    customer_order_id = Column(BIGINT(20), comment='#租赁订单id#')
    customer_order_code = Column(String(50), comment='#租赁订单编号#')


class BStopOrderDevice(Base):
    __tablename__ = 'b_stop_order_device'
    __table_args__ = {'comment': '报停设备'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    stop_order_id = Column(BIGINT(20), comment='#报停单id#')
    supplementary_rent = Column(DECIMAL(16, 2), comment='#补收租金#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')
    enter_info_id = Column(BIGINT(20), comment='#进场信息id#')
    status = Column(TINYINT(4), comment='#状态#')
    category_id = Column(BIGINT(22), comment='#品类id#')
    category_name = Column(String(100), comment='#品类名称#')
    device_no = Column(String(50), comment='#序列号#')
    enter_time = Column(DateTime, comment='#进场时间#')
    brand_id = Column(BIGINT(22), comment='#品牌id#')
    brand_name = Column(String(50), comment='#品牌#')
    tenant_id = Column(BIGINT(22), comment='#商户id#')
    tenant_name = Column(String(50), comment='#商户#')
    lease_mode = Column(TINYINT(4), comment='#租赁模式#')
    valuation_way = Column(TINYINT(4), comment='#结算方式#')
    work_day = Column(INTEGER(11), comment='#工作天数#')
    customer_contract_id = Column(BIGINT(20), comment='#租赁合同id#')
    customer_order_id = Column(BIGINT(20), comment='#租赁订单id#')
    tenant_contract_id = Column(BIGINT(20), comment='#转租合同id#')
    tenant_order_id = Column(BIGINT(20), comment='#转租订单id#')
    tenant_order_device_id = Column(BIGINT(20), comment='#转租订单设备id#')
    customer_contract_code = Column(String(50), comment='#租赁合同编号#')
    customer_contract_name = Column(String(50), comment='#租赁合同名称#')
    customer_order_code = Column(String(50), comment='#租赁订单编号#')
    tenant_contract_code = Column(String(50), comment='#转租合同编号#')
    tenant_contract_name = Column(String(50), comment='#转租合同名称#')
    tenant_order_code = Column(String(50), comment='#转租订单编号#')
    change_status = Column(TINYINT(4), server_default=text("'0'"), comment='#变更状态#')
    change_supplementary_rent = Column(DECIMAL(16, 2), comment='#变更-补收租金#')
    model = Column(String(50), comment='#设备型号#')


class BStopOrderDeviceParameter(Base):
    __tablename__ = 'b_stop_order_device_parameter'
    __table_args__ = {'comment': '报停设备规格参数表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    stop_order_id = Column(BIGINT(20), comment='#报停单id#')
    stop_order_device_id = Column(BIGINT(20), comment='#报停单设备id#')
    device_param_id = Column(BIGINT(20), comment='#设备规格参数id#')
    device_param_name = Column(String(50), comment='#设备规格参数名称#')
    device_param_value = Column(DECIMAL(18, 2), comment='#参数值#')
    unit_id = Column(BIGINT(20), comment='#计量单位id#')
    unit_name = Column(String(25), comment='#计量单位（冗余）#')
    unit_en_name = Column(String(25), comment='#英文计量单位（冗余）#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    modifier = Column(String(25), server_default=text("''"), comment='修改人')
    update_time = Column(DateTime, comment='修改时间')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='逻辑删除#ENUM#0:正常,1:删除')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')


class BStopOrderFile(Base):
    __tablename__ = 'b_stop_order_file'

    id = Column(BIGINT(22), primary_key=True, comment='#主键ID#')
    stop_order_id = Column(BIGINT(22), comment='#报停单id#')
    file_id = Column(BIGINT(22), comment='#文件ID#')
    file_name = Column(String(200), comment='#文件名#')
    file_url = Column(String(512), comment='#文件URL#')
    extension = Column(String(200), comment='#拓展名#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')
    change_status = Column(TINYINT(4), server_default=text("'0'"), comment='#变更状态#')


class BTaskDetailImg(Base):
    __tablename__ = 'b_task_detail_img'
    __table_args__ = {'comment': '报工明细图片表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键ID#')
    task_detail_id = Column(BIGINT(20), comment='#报工明细表id#')
    file_id = Column(BIGINT(20), comment='#文件ID#')
    file_name = Column(String(500), comment='#文件名#')
    file_url = Column(String(1024), comment='#附件链接#')
    extension = Column(String(100), comment='#拓展名#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BTaskDeviceParameter(Base):
    __tablename__ = 'b_task_device_parameter'
    __table_args__ = {'comment': '任务管理设备规格参数表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    task_record_id = Column(BIGINT(20), comment='#报工id#')
    task_detail_id = Column(BIGINT(20), comment='#报工明细表id#')
    device_category_id = Column(BIGINT(20), comment='#设备品类#')
    device_param_id = Column(BIGINT(20), comment='#设备规格参数id#')
    device_param_name = Column(String(50), comment='#设备规格参数名称#')
    device_param_value = Column(DECIMAL(18, 2), comment='#参数值#')
    unit_id = Column(BIGINT(20), comment='#计量单位id#')
    unit_name = Column(String(25), comment='#计量单位（冗余）#')
    unit_en_name = Column(String(25), comment='#英文计量单位（冗余）#')
    type = Column(TINYINT(4), comment='#类型#ENUM#0:商户作业报工:TENANT_PARAM,1:客户作业报工:CUSTOMER_PARAM,2:商户日报工:TENANT_DAY_PARAM,3:客户日报工:CUSTOMER_DAY_PARAM#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    modifier = Column(String(25), server_default=text("''"), comment='修改人')
    update_time = Column(DateTime, comment='修改时间')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='逻辑删除#ENUM#0:正常,1:删除')


class BTaskRecord(Base):
    __tablename__ = 'b_task_record'
    __table_args__ = {'comment': '任务记录表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键ID#')
    task_code = Column(String(50), comment='#任务单号#')
    enter_info_id = Column(BIGINT(20), comment='#进场单id#b_enter_info.id')
    enter_code = Column(String(50), comment='#进场单编码#')
    exit_id = Column(BIGINT(20), comment='#退场单id#')
    dispatch_id = Column(BIGINT(20), comment='#调度id#')
    dispatch_code = Column(String(100), comment='#调度单号#')
    dispatch_device_detail_id = Column(BIGINT(20), comment='#调度设备详情id#')
    notice_id = Column(BIGINT(20), comment='#施工通知单id#')
    notice_code = Column(String(100), comment='#施工通知单编号#')
    customer_contract_id = Column(BIGINT(20), comment='#合同id#')
    customer_contract_code = Column(String(100), comment='#合同编号#')
    customer_contract_name = Column(String(100), comment='#合同名称#')
    customer_order_id = Column(BIGINT(20), comment='#客户订单orderId#')
    customer_order_code = Column(String(100), comment='#客户订单编号#')
    customer_order_device_id = Column(BIGINT(20), comment='#客户订单设备id#')
    customer_order_valuation_id = Column(BIGINT(20), comment='#客户订单计价id#')
    tenant_contract_id = Column(BIGINT(20), comment='#转租合同id#')
    tenant_contract_code = Column(String(100), comment='#转租合同code#')
    tenant_contract_name = Column(String(100), comment='#转租合同名称#')
    tenant_order_id = Column(BIGINT(20), comment='#商户订单id#')
    tenant_order_code = Column(String(100), comment='#商户订单编码#')
    tenant_order_device_id = Column(BIGINT(20), comment='#商户订单设备id#')
    tenant_order_valuation_id = Column(BIGINT(20), comment='#商户订单计价id#')
    project_id = Column(BIGINT(20), comment='#工程id#')
    project_name = Column(String(100), comment='#工程名称#')
    brand_id = Column(BIGINT(20), comment='#品牌id#')
    brand_name = Column(String(100), comment='#品牌名称#')
    using_date = Column(Date, comment='#使用日期#')
    in_time = Column(DateTime, comment='#进场时间#')
    customer_id = Column(BIGINT(20), comment='#承租方id#')
    customer_name = Column(String(50), comment='#客户名称#')
    car_no = Column(String(20), comment='#运输车牌号#')
    device_no = Column(String(50), comment='#整机序列号#')
    master_id = Column(BIGINT(20), comment='#机手id#')
    master_name = Column(String(20), comment='#机手名称#')
    master_phone = Column(String(20), comment='#机手手机号#')
    site_leader_id = Column(BIGINT(20), comment='#现场联系人id#')
    site_leader = Column(String(50), comment='#现场联系人#')
    site_leader_phone = Column(String(50), comment='#现场联系人手机号#')
    device_category_id = Column(BIGINT(20), comment='#设备品类id#')
    device_category_name = Column(String(50), comment='#设备品类名称#')
    province_code = Column(String(100), comment='#省份code#')
    province_name = Column(String(100), comment='#省份名称#')
    city_code = Column(String(100), comment='#城市code#')
    city_name = Column(String(100), comment='#城市名称#')
    district_code = Column(String(100), comment='#区域code#')
    district_name = Column(String(100), comment='#区域名称#')
    address = Column(String(200), comment='#施工地址#')
    finish_time = Column(DateTime, comment='#完成时间#')
    leasing_model = Column(TINYINT(4), comment='#租赁模式#')
    valuation_way = Column(TINYINT(4), comment='#计价方式#')
    order_state = Column(TINYINT(4), comment='#订单状态#')
    tenant_id = Column(BIGINT(20), comment='#商户id#')
    tenant_name = Column(String(50), comment='#商户名称#')
    model = Column(String(100), comment='#设备型号#')
    device_detail_id = Column(BIGINT(20), comment='#设备明细id#')
    driver_id = Column(BIGINT(20), comment='#司机id#')
    driver_name = Column(String(50), comment='#司机姓名#')
    driver_phone = Column(String(50), comment='#司机手机号#')
    stop_start_time = Column(DateTime, comment='#报停开始时间#')
    stop_end_time = Column(DateTime, comment='#报停结束时间#')
    msg = Column(String(200), comment='#备注#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BTaskReportDetail(Base):
    __tablename__ = 'b_task_report_detail'
    __table_args__ = {'comment': '报工详情表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键ID#')
    record_id = Column(BIGINT(20), comment='#记录表id#')
    task_code = Column(String(50), comment='#任务单号#')
    enter_info_id = Column(BIGINT(20), comment='#进场确认单id#b_enter_confirm.id')
    enter_code = Column(String(50), comment='#进场确认单编码#')
    notice_id = Column(BIGINT(20), comment='#施工通知单id#')
    notice_code = Column(String(100), comment='#施工通知单编号#')
    dispatch_id = Column(BIGINT(20), comment='#调度id#')
    dispatch_code = Column(String(100), comment='#调度单编号#')
    dispatch_device_detail_id = Column(BIGINT(20), comment='#调度设备详情id#')
    project_id = Column(BIGINT(20), comment='#工程id#')
    project_name = Column(String(100), comment='#工程名称#')
    customer_id = Column(BIGINT(20), comment='#承租方id#')
    customer_name = Column(String(50), comment='#客户名称#')
    brand_id = Column(BIGINT(20), comment='#品牌id#')
    brand_name = Column(String(100), comment='#品牌名称#')
    using_date = Column(Date, comment='#使用日期#')
    in_time = Column(DateTime, comment='#进场时间#')
    car_no = Column(String(20), comment='#车牌号#')
    master_id = Column(BIGINT(20), comment='#机手id#')
    master_name = Column(String(20), comment='#机手名称#')
    master_phone = Column(String(20), comment='#机手手机号#')
    site_leader_id = Column(BIGINT(20), comment='#现场联系人id#')
    site_leader = Column(String(50), comment='#现场联系人#')
    site_leader_phone = Column(String(50), comment='#现场联系人手机号#')
    order_state = Column(TINYINT(6), comment='#订单状态#')
    tenant_id = Column(BIGINT(20), comment='#商户id#')
    tenant_name = Column(String(50), comment='#商户名称#')
    report_code = Column(String(50), comment='#报工编号#')
    report_type = Column(TINYINT(6), comment='#报工类型#')
    report_state = Column(TINYINT(6), comment='#报工状态#')
    leasing_model = Column(TINYINT(4), comment='#租赁模式#')
    valuation_way = Column(TINYINT(6), comment='#结算方式#')
    cost = Column(DECIMAL(18, 2), comment='#使用时长/方量#')
    customer_contract_id = Column(BIGINT(20), comment='#合同id#')
    customer_contract_code = Column(String(50), comment='#合同code#')
    customer_contract_name = Column(String(100), comment='#合同名称#')
    customer_order_id = Column(BIGINT(20), comment='#客户订单表id#')
    customer_order_code = Column(String(100), comment='#客户订单编码#')
    customer_order_device_id = Column(BIGINT(20), comment='#商户订单设备id#')
    customer_order_valuation_id = Column(BIGINT(20), comment='#商户订单计价id#')
    tenant_contract_id = Column(BIGINT(20), comment='#转租合同id#')
    tenant_contract_code = Column(String(100), comment='#转租合同code#')
    tenant_contract_name = Column(String(100), comment='#转租合同名称#')
    tenant_order_id = Column(BIGINT(20), comment='#商户订单id#')
    tenant_order_code = Column(String(100), comment='#商户订单编号#')
    tenant_order_device_id = Column(BIGINT(20), comment='#商户订单设备id#')
    tenant_order_valuation_id = Column(BIGINT(20), comment='#商户订单计价id#')
    device_no = Column(String(50), comment='#整机序列号#')
    model = Column(String(100), comment='#设备型号#')
    device_category_id = Column(BIGINT(20), comment='#设备品类id#')
    device_category_name = Column(String(50), comment='#设备品类名称#')
    province_code = Column(String(100), comment='#省份code#')
    province_name = Column(String(100), comment='#省份名称#')
    city_code = Column(String(100), comment='#城市code#')
    city_name = Column(String(100), comment='#城市名称#')
    district_code = Column(String(100), comment='#区域code#')
    district_name = Column(String(100), comment='#区域名称#')
    captcha = Column(String(100), comment='#验证码#')
    address = Column(String(200), comment='#施工地址#')
    msg = Column(String(200), comment='#备注/说明#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BTenantContract(Base):
    __tablename__ = 'b_tenant_contract'
    __table_args__ = {'comment': '商户合同表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    tenant_id = Column(BIGINT(20), comment='#商户id#')
    tenant_name = Column(String(50), comment='#商户名称#')
    sign_date = Column(Date, comment='#签署日期#')
    code = Column(String(50), comment='#合同编号#')
    name = Column(String(100), comment='#合同名称#')
    external_code = Column(String(50), comment='#外部合同编号#')
    external_name = Column(String(100), comment='#外部合同编号#')
    status = Column(TINYINT(4), comment='#合同状态#')
    merchants_bd_id = Column(BIGINT(20), comment='#招商BD id#')
    merchants_bd_name = Column(String(50), comment='#招商BD名称#')
    sign_sales_id = Column(BIGINT(20), comment='#签约销售id#')
    sign_sales_name = Column(String(50), comment='#签约销售名称#')
    region_name = Column(String(50), comment='#大区门店#')
    party_a_name = Column(String(50), comment='#甲方（出租方）名称#')
    party_a_unified_social_credit_code = Column(String(50), comment='#甲方统一社会信用代码/身份证#')
    party_a_address = Column(String(500), comment='#甲方通讯地址#')
    party_a_legal_person = Column(String(25), comment='#甲方法定代表人#')
    party_a_contacts = Column(String(25), comment='#甲方联系人#')
    party_a_phone = Column(String(25), comment='#甲方联系方式#')
    party_b_id = Column(BIGINT(20), comment='#甲方主体id#')
    party_b_name = Column(String(50), comment='#乙方（出租方）名称#')
    party_b_unified_social_credit_code = Column(String(50), comment='#乙方统一社会信用代码/身份证#')
    party_b_address = Column(String(500), comment='#乙方通讯地址#')
    party_b_legal_person = Column(String(25), comment='#乙方法定代表人#')
    party_b_contacts = Column(String(25), comment='#乙方联系人#')
    party_b_phone = Column(String(25), comment='#乙方联系方式#')
    party_a_account_name = Column(String(100), comment='#甲方账号名#')
    party_a_bank_account = Column(String(100), comment='#甲方账号#')
    party_a_bank_name = Column(String(100), comment='#甲方开户行#')
    party_b_invoice_name = Column(String(100), comment='#乙方名称#')
    party_b_invoice_tx_id_num = Column(String(50), comment='#乙方纳税人识别号#')
    party_b_invoice_address = Column(String(500), comment='#乙方地址#')
    party_b_invoice_tel = Column(String(50), comment='#乙方电话#')
    party_b_invoice_bank_name = Column(String(100), comment='#乙方开户行#')
    party_b_invoice_bank_account = Column(String(100), comment='#乙方账号#')
    start_date = Column(Date, comment='#合同起始日期#')
    end_date = Column(Date, comment='#合同结束日期#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BTenantContractFile(Base):
    __tablename__ = 'b_tenant_contract_file'
    __table_args__ = {'comment': '商户合同附件表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    tenant_contract_id = Column(BIGINT(20), comment='#商户合同表id#')
    attachment_file_id = Column(BIGINT(20), comment='#附件id#')
    attachment_url = Column(String(1024), comment='#附件url#')
    attachment_name = Column(String(100), comment='#附件名称#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BTenantInfo(Base):
    __tablename__ = 'b_tenant_info'
    __table_args__ = {'comment': '商户信息表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键ID#')
    customer_id = Column(BIGINT(20), comment='#客户id#')
    property = Column(TINYINT(4), server_default=text("'0'"), comment='#商户性质#ENUM#0:企业:ENTERPRISE,1:个人:PERSONAL#')
    code = Column(String(50), comment='#商户编号#')
    name = Column(String(100), index=True, comment='#商户名称#')
    name_pinyin = Column(String(200), comment='#客户名称拼音#')
    province_code = Column(String(25), comment='#省份code#')
    province_name = Column(String(50), comment='#省份名称#')
    city_code = Column(String(25), comment='#城市code#')
    city_name = Column(String(50), comment='#城市名称#')
    district_code = Column(String(25), comment='#区域code#')
    district_name = Column(String(50), comment='#区域名称#')
    address = Column(String(500), comment='#地址#')
    contacts = Column(String(50), comment='#联系人#')
    phone = Column(String(25), comment='#联系电话#')
    type = Column(TINYINT(4), comment='#商户类型#ENUM#0:自营:SELF,1:第三方入驻:#OTHER')
    front_desk_tel = Column(String(50), comment='#前台电话#')
    tenant_source = Column(TINYINT(4), comment='#商户来源#')
    personnel_size = Column(TINYINT(4), comment='#人员规模#')
    tenant_level = Column(TINYINT(4), comment='#商户级别#ENUM#0:大型商户:LARGE,1:中型商户:MEDIUM,2:小型商户:SMALL#')
    cooperation_status = Column(TINYINT(4), comment='#合作状态#')
    device_inventory = Column(INTEGER(11), server_default=text("'0'"), comment='#设备保有量#')
    vacancy_rates = Column(DECIMAL(18, 2), comment='#闲置率(%)#')
    device_operator_num = Column(INTEGER(11), server_default=text("'0'"), comment='#在职机手数量#')
    special_service_personnel = Column(INTEGER(11), server_default=text("'0'"), comment='#专岗服务人数#')
    supply_coverage = Column(TINYINT(4), comment='#供给覆盖范围#0:全国,1:大区级,2:省级,3:市级#')
    logistics_capability = Column(TINYINT(4), comment='#物流能力#0:支持物流,1:不支持物流#')
    logistics_coverage_radius = Column(INTEGER(11), server_default=text("'0'"), comment='#物流覆盖半径#')
    service_coverage_radius = Column(INTEGER(11), server_default=text("'0'"), comment='#服务覆盖半径#')
    support_urgent_order = Column(TINYINT(1), server_default=text("'0'"), comment='#特殊单能力-可接急单#')
    support_night_order = Column(TINYINT(1), server_default=text("'0'"), comment='#特殊单能力-可接夜单#')
    payment_methods = Column(TINYINT(4), comment='#常用收款方式#0：预付，1：现款，2：账期#')
    special_invoice = Column(TINYINT(1), server_default=text("'0'"), comment='#开票类型-专票#')
    ordinary_invoice = Column(TINYINT(1), server_default=text("'0'"), comment='#开票类型-普票#')
    no_invoice = Column(TINYINT(1), server_default=text("'0'"), comment='#开票类型-不开票#')
    key_decision_maker = Column(String(25), comment='#关键决策人#')
    decision_maker_tel = Column(String(25), comment='#决策人电话#')
    decision_maker_age = Column(TINYINT(4), comment='#决策人年龄#')
    decision_maker_position = Column(String(50), comment='#决策人职位#')
    unified_social_credit_code = Column(String(100), comment='#统一社会信用代码#')
    legal_person = Column(String(25), comment='#法人#')
    business_license_file_id = Column(BIGINT(20), comment='#营业执照文件id#')
    business_license_url = Column(String(1000), comment='#营业执照url#')
    id_card_number = Column(String(50), comment='#身份证号码#')
    id_card_front_file_id = Column(BIGINT(20), comment='#身份证正面文件id#')
    id_card_front_url = Column(String(1000), comment='#身份证正面url#')
    id_card_back_file_id = Column(BIGINT(20), comment='#身份证反面文件id#')
    id_card_back_url = Column(String(1000), comment='#身份证反面url#')
    merchants_bd_id = Column(BIGINT(20), comment='#招商BD的id#')
    merchants_bd_name = Column(String(25), comment='#招商BD的名称#')
    registered_capital = Column(TINYINT(4), comment='#注册资本#ENUM#1:5亿以上:GT_5_Y,2:1-5亿:BT_1_5_Y,3:5000-9999万:BT_5000_9999_W,4:2000-4999万:BT_2000_4999_W,5:1000-1999万:BT_1000_1999_W,6:1000万以下:LT_1000_W#')
    paid_in_capital = Column(DECIMAL(18, 4), comment='#实缴资本#')
    register_years = Column(INTEGER(11), comment='#已注册年限#')
    total_assets = Column(DECIMAL(18, 4), comment='#总资产#')
    asset_liability_ratio = Column(DECIMAL(18, 4), comment='#资产负债率#')
    merchant_account = Column(String(50), comment='#商户账号#')
    user_id = Column(BIGINT(20), comment='#商户账号对应的用户id#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BTenantOrder(Base):
    __tablename__ = 'b_tenant_order'
    __table_args__ = {'comment': '商端订单表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    status = Column(TINYINT(4), comment='#订单状态#')
    code = Column(String(50), comment='#订单编号#')
    contract_id = Column(BIGINT(20), comment='#转租合同id#')
    contract_code = Column(String(50), comment='#转租合同编号#')
    tenant_id = Column(BIGINT(20), comment='#商户id#')
    tenant_name = Column(String(50), comment='#商户名称#')
    business_id = Column(BIGINT(20), comment='#主商机id#')
    business_sub_id = Column(BIGINT(20), comment='#子商机id#')
    customer_order_id = Column(BIGINT(20), comment='#租凭订单id#')
    party_a_contacts = Column(String(25), comment='#甲方联系人#')
    party_a_phone = Column(String(25), comment='#甲方联系方式#')
    party_b_contacts = Column(String(25), comment='#乙方联系人#')
    party_b_phone = Column(String(25), comment='#乙方联系方式#')
    merchants_bd_id = Column(BIGINT(20), comment='#招商BD id#')
    merchants_bd_name = Column(String(50), comment='#招商BD名称#')
    site_leader = Column(String(25), comment='#现场负责人#')
    site_leader_phone = Column(String(25), comment='#现场负责人电话#')
    site_actual_user = Column(String(25), comment='#现场实际使用人#')
    project_id = Column(BIGINT(20), comment='#工程id#')
    project_name = Column(String(100), comment='#工程名称#')
    province_code = Column(String(50), comment='#省code#')
    province_name = Column(String(50), comment='#省份名称#')
    city_code = Column(String(50), comment='#市code#')
    city_name = Column(String(50), comment='#城市名称#')
    district_code = Column(String(50), comment='#区code#')
    district_name = Column(String(50), comment='#区域名称#')
    delivery_place = Column(String(200), comment='#施工/设备交付地点#')
    entry_date = Column(Date, comment='#进场日期#')
    departure_date = Column(Date, comment='#离场日期#')
    delivery_method = Column(TINYINT(4), comment='#设备交付方式#ENUM#0:出租方负责运输:LESSOR,1:承租方负责运输:LESSEE#')
    project_content = Column(String(1000), comment='#施工内容#')
    other_valuation_way = Column(String(1024), comment='#其他计价方式#')
    payment_form = Column(TINYINT(4), comment='#支付形式#ENUM#0:电汇:WIRE_TRANSFER,1:银承:BANK_ACCEPTANCE_BILL#')
    payment_terms_gt_thirty_days = Column(INTEGER(11), comment='#支付条款（大于30天）#')
    payment_terms_lt_thirty_days = Column(String(255), comment='#支付条款（小于30天）#')
    entry_fee = Column(DECIMAL(18, 2), comment='#进场费用#')
    cause_type = Column(TINYINT(4), comment='#取消原因类型#')
    cancel_reason = Column(String(200), comment='#取消原因#')
    cancel_time = Column(DateTime, comment='#取消时间#')
    lease_amount = Column(INTEGER(11), server_default=text("'0'"), comment='#租赁台数#')
    sign_sales_id = Column(BIGINT(20), comment='#签约销售id#')
    sign_sales_name = Column(String(25), comment='#签约销售名称#')
    sign_date = Column(Date, comment='#签约日期#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BTenantOrderCost(Base):
    __tablename__ = 'b_tenant_order_cost'
    __table_args__ = {'comment': '商端订单费用分担表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    tenant_order_id = Column(BIGINT(20), nullable=False, comment='#商端订单id#')
    cost_id = Column(BIGINT(20), comment='#费用id#')
    cost_name = Column(String(100), comment='#费用名目(冗余)#')
    undertake_object = Column(TINYINT(4), comment='#承担对象#ENUM#0:甲方:PARTY_A,1:乙方:PARTY_B#')
    money = Column(DECIMAL(18, 2), comment='#金额（元）#')
    sort = Column(INTEGER(11), comment='#排序#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BTenantOrderDevice(Base):
    __tablename__ = 'b_tenant_order_device'
    __table_args__ = {'comment': '商端订单设备表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    tenant_order_id = Column(BIGINT(20), comment='#商端订单id#')
    device_category_id = Column(BIGINT(20), comment='#设备品类id#')
    device_category_name = Column(String(50), comment='#设备品类名称#')
    brand_id = Column(BIGINT(20), comment='#品牌id#')
    brand_name = Column(String(50), comment='#品牌名称#')
    model = Column(String(100), comment='#型号#')
    num = Column(INTEGER(11), comment='#台数#')
    leasing_model = Column(TINYINT(4), comment='#租赁模式#')
    valuation_way = Column(TINYINT(4), comment='#计价方式#')
    invoice_type = Column(TINYINT(4), comment='#开票类型#ENUM#0:不开票:NO_INVOICING,1:普票:ORDINARY_INVOICE,2:专票:SPECIAL_INVOICE#')
    tax_rate = Column(DECIMAL(10, 2), comment='#租金税率#')
    unit_price = Column(DECIMAL(18, 2), comment='#不含税单价#')
    tax_unit_price = Column(DECIMAL(18, 2), comment='#含税单价#')
    first_entry_num = Column(INTEGER(11), comment='#首次进场台数#')
    sort = Column(INTEGER(11), comment='#排序#')
    dispatched_num = Column(INTEGER(11), comment='#商户已调度设备数量#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BTenantOrderDeviceParameter(Base):
    __tablename__ = 'b_tenant_order_device_parameter'
    __table_args__ = {'comment': '商端订单设备参数'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    tenant_order_id = Column(BIGINT(20), comment='#商端订单id#')
    tenant_order_device_id = Column(BIGINT(20), comment='#商端订单设备id#')
    device_category_id = Column(BIGINT(20), comment='#设备品类id#')
    device_category_name = Column(String(50), comment='#设备品类名称#')
    device_param_id = Column(BIGINT(20), comment='#设备规格参数id#')
    device_param_name = Column(String(50), comment='#设备规格参数名称#')
    device_param_value = Column(DECIMAL(18, 2), comment='#参数值#')
    unit_id = Column(BIGINT(20), comment='#计量单位id#')
    unit_name = Column(String(25), comment='#计量单位（冗余）#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BTenantOrderFile(Base):
    __tablename__ = 'b_tenant_order_file'
    __table_args__ = {'comment': '商户合同订单附件表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    tenant_order_id = Column(BIGINT(20), comment='#商户订单表id#')
    attachment_file_id = Column(BIGINT(20), comment='#附件id#')
    attachment_url = Column(String(1024), comment='#附件url#')
    attachment_name = Column(String(100), comment='#附件名称#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BTenantOrderValuation(Base):
    __tablename__ = 'b_tenant_order_valuation'
    __table_args__ = {'comment': '商端订单计价方式约定表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    tenant_order_id = Column(BIGINT(20), comment='#商端订单id#')
    order_device_id = Column(BIGINT(20), comment='#订单设备id#')
    valuation_way = Column(TINYINT(4), comment='#计价方式#')
    month_days = Column(DECIMAL(18, 2), comment='#按月-包月天数#')
    month_hours = Column(DECIMAL(18, 2), comment='#按月-包月时限#')
    month_overtime_fee = Column(DECIMAL(18, 2), comment='#按月-超时费用#')
    month_entry_rule_time_before = Column(Time, comment='#按月-进场规则-时间-前#')
    month_entry_rule_time_before_days = Column(DECIMAL(10, 2), comment='#按月-进场规则-时间-前-天数#')
    month_entry_rule_middle_days = Column(DECIMAL(10, 2), comment='#按月-进场规则-中间进场-天数#')
    month_entry_rule_time_after = Column(Time, comment='#按月-进场规则-时间-后#')
    month_entry_rule_time_after_days = Column(DECIMAL(10, 2), comment='#按月-进场规则-时间-后-天数#')
    month_exit_rule_time_before = Column(Time, comment='#按月-退场规则-时间-前#')
    month_exit_rule_time_before_days = Column(DECIMAL(10, 2), comment='#按月-退场规则-时间-前-天数#')
    month_exit_rule_middle_days = Column(DECIMAL(10, 2), comment='#按月-退场规则-中间进场-天数#')
    month_exit_rule_time_after = Column(Time, comment='#按月-退场规则-时间-后#')
    month_exit_rule_time_after_days = Column(DECIMAL(18, 2), comment='#按月-退场规则-时间-后-天数#')
    month_exchange_machine_hours = Column(DECIMAL(18, 2), comment='#按月-转台班时限#')
    month_exchange_machine_price = Column(DECIMAL(10, 2), comment='#按月-转台班单价#')
    month_exchange_machine_work_rule_match_num = Column(DECIMAL(18, 2), comment='#按月-转台班-报工规则-匹配规则台班数#')
    month_exchange_machine_work_rule_not_match = Column(DECIMAL(18, 2), comment='#按月-转台班-报工规则-不匹配规则台班数#')
    machine_team_hours = Column(DECIMAL(18, 2), comment='#台班-时限#')
    machine_team_work_rule_match_num = Column(DECIMAL(18, 2), comment='#台班-报工规则-匹配规则台班数#')
    machine_team_work_rule_not_match_num = Column(DECIMAL(18, 2), comment='#台班-报工规则-不匹配规则台班数#')
    machine_team_unit_device_num = Column(DECIMAL(18, 2), comment='#台班-单位设备台数#')
    machine_team_unit_operator_num = Column(DECIMAL(18, 2), comment='#台班-单位设备操作员数#')
    machine_team_food_bed_type = Column(TINYINT(4), comment='#台班-住宿伙食#ENUM#0:包食宿:CONTAIN_ALL,1:包住宿，不包伙食:BED,2:包伙食，不包住宿:FOOD,3:不包食宿:NOT_CONTAIN#')
    day_hours = Column(DECIMAL(18, 2), comment='#按日-时限#')
    day_entry_rule_time_before = Column(Time, comment='#按日-进场规则-时间-前#')
    day_entry_rule_time_before_days = Column(DECIMAL(18, 2), comment='#按日-进场规则-时间-前-天数#')
    day_entry_rule_middle_days = Column(DECIMAL(18, 2), comment='#按日-进场规则-中间进场-天数#')
    day_entry_rule_time_after = Column(Time, comment='#按日-进场规则-时间-后#')
    day_entry_rule_time_after_days = Column(DECIMAL(18, 2), comment='#按日-进场规则-时间-后-天数#')
    day_exit_rule_time_before = Column(Time, comment='#按日-退场规则-时间-前#')
    day_exit_rule_time_before_days = Column(DECIMAL(18, 2), comment='#按日-退场规则-时间-前-天数#')
    day_exit_rule_middle_days = Column(DECIMAL(18, 2), comment='#按日-退场规则-中间进场-天数#')
    day_exit_rule_time_after = Column(Time, comment='#按日-退场规则-时间-后#')
    day_exit_rule_time_after_days = Column(DECIMAL(18, 2), comment='#按日-退场规则-时间-后-天数#')
    day_work_rule_match_num = Column(DECIMAL(18, 2), comment='#按日-报工规则-匹配规则天数#')
    day_work_rule_not_match = Column(DECIMAL(18, 2), comment='#按日-报工规则-不匹配规则天数#')
    hour_fee = Column(DECIMAL(18, 0), comment='#按小时-保底金额#')
    hour_duration = Column(DECIMAL(18, 2), comment='#按小时-保底时长#')
    hour_overtime_fee = Column(DECIMAL(18, 2), comment='#按小时-超时费用#')
    hour_work_rule_match_num = Column(DECIMAL(18, 2), comment='#按小时-报工规则-匹配规则小时数#')
    hour_work_rule_not_match = Column(DECIMAL(18, 2), comment='#按小时-报工规则-不匹配规则小时数#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BTenantStorage(Base):
    __tablename__ = 'b_tenant_storage'
    __table_args__ = {'comment': '商户仓库信息表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    tenant_id = Column(BIGINT(20), comment='#商户id#')
    name = Column(String(100), comment='#仓库名称#')
    province_code = Column(String(25), comment='#省份编号#')
    province_name = Column(String(50), comment='#省份名称#')
    city_code = Column(String(25), comment='#城市编号#')
    city_name = Column(String(50), comment='#城市名称#')
    district_code = Column(String(25), comment='#区域编号#')
    district_name = Column(String(50), comment='#区域名称#')
    address = Column(String(500), comment='#地址#')
    address_title = Column(String(200), comment='#地点-标题#')
    lat = Column(String(25), comment='#地点-纬度#')
    lng = Column(String(25), comment='#地点-经度#')
    address_desc = Column(String(200), comment='#补充地址说明#')
    contacts = Column(String(50), comment='#联系人#')
    phone = Column(String(25), comment='#联系电话#')
    remark = Column(String(500), comment='#备注#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BTenantStorageImg(Base):
    __tablename__ = 'b_tenant_storage_img'

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    tenant_storage_id = Column(BIGINT(20), comment='#仓库id#')
    file_id = Column(BIGINT(20), comment='#文件id#')
    file_name = Column(String(500), comment='#文件名称#')
    url = Column(String(1024), comment='#url#')
    extension = Column(String(25), comment='#拓展名#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BTenantStorageScope(Base):
    __tablename__ = 'b_tenant_storage_scope'
    __table_args__ = {'comment': '商户仓库业务范围表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    tenant_storage_id = Column(BIGINT(20), comment='#仓库id#')
    province_code = Column(String(25), comment='#省份code#')
    province_name = Column(String(50), comment='#省份名称#')
    city_code = Column(String(25), comment='#城市编号#')
    city_name = Column(String(50), comment='#城市名称#')
    district_code = Column(String(25), comment='#区域编号#')
    district_name = Column(String(50), comment='#区域名称#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BTopicInfo(Base):
    __tablename__ = 'b_topic_info'
    __table_args__ = {'comment': '专题信息表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键ID#')
    title = Column(String(255), comment='#专题标题#')
    desc = Column(String(255), comment='#专题描述#')
    message = Column(Text, comment='#专题正文#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BTopicPicture(Base):
    __tablename__ = 'b_topic_picture'
    __table_args__ = {'comment': '专题图片表'}

    id = Column(BIGINT(22), primary_key=True)
    topic_id = Column(BIGINT(22), comment='#专题ID#')
    file_id = Column(BIGINT(22), comment='#图片id#')
    is_major = Column(TINYINT(1), comment='#是否主图#1:是,0:否#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BTransactionSetting(Base):
    __tablename__ = 'b_transaction_settings'
    __table_args__ = {'comment': '交易设置表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    collection_qr_code_file_id = Column(BIGINT(20), nullable=False, comment='#收款二维码文件id#')
    collection_qr_code_file_name = Column(String(100), comment='#收款二维码文件名称#')
    collection_qr_code_url = Column(String(1024), nullable=False, comment='#收款二维码url#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(VARCHAR(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(VARCHAR(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BUserAccount(Base):
    __tablename__ = 'b_user_account'
    __table_args__ = {'comment': '用户账户表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键ID#')
    user_id = Column(BIGINT(20), comment='#用户ID#')
    account_type = Column(TINYINT(4), comment='#账户类型#')
    balance = Column(DECIMAL(18, 2), server_default=text("'0.00'"), comment='#余额#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BUserAccountCashout(Base):
    __tablename__ = 'b_user_account_cashout'
    __table_args__ = {'comment': '用户提现记录表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键ID#')
    user_id = Column(BIGINT(20), comment='#用户ID#')
    amount = Column(DECIMAL(18, 2), comment='#提现金额#')
    after_balance = Column(DECIMAL(18, 2), comment='#本次提现后的余额#')
    status = Column(TINYINT(4), comment='#提现状态，0申请中，1提现成功，2提现失败#')
    apply_time = Column(DateTime, comment='#申请时间#')
    operate_desc = Column(String(100), comment='#操作描述-提现失败说明#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BUserAccountRecord(Base):
    __tablename__ = 'b_user_account_record'
    __table_args__ = {'comment': '用户账户流水表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键ID#')
    user_id = Column(BIGINT(20), comment='#用户ID#')
    pre_balance = Column(DECIMAL(18, 2), comment='#交易前余额#')
    current_amount = Column(DECIMAL(18, 2), comment='#本次交易金额#')
    record_type = Column(TINYINT(4), comment='#流水类型，1转入，2转出#')
    busi_type = Column(TINYINT(4), comment='#业务类型，1返佣，2提现#')
    busi_id = Column(BIGINT(20), comment='#关联交易业务ID#')
    busi_desc = Column(String(100), comment='#业务描述#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BUserBankCard(Base):
    __tablename__ = 'b_user_bank_card'
    __table_args__ = {'comment': '用户银行卡信息'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键ID#')
    user_id = Column(BIGINT(20), comment='#用户ID#')
    certificate_type = Column(TINYINT(4), server_default=text("'1'"), comment='#证件类型，1身份证，2护照，3其他#')
    certificate_num = Column(String(100), comment='#证件号码#')
    bank_id = Column(INTEGER(11), comment='#银行id#')
    bank_name = Column(String(50), comment='#开户行#')
    sub_bank_name = Column(String(100), comment='#开户子行#')
    account_name = Column(String(20), comment='#持卡人姓名#')
    card_num = Column(String(50), comment='卡号')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BVisitInfo(Base):
    __tablename__ = 'b_visit_info'
    __table_args__ = {'comment': '拜访信息'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    customer_id = Column(BIGINT(20), comment='#客户id#')
    customer_name = Column(String(200), comment='#客户名称#')
    tenant_id = Column(BIGINT(20), comment='#商户id#')
    tenant_name = Column(String(200), comment='#商户名称#')
    project_id = Column(BIGINT(20), comment='#工程id#')
    project_name = Column(String(200), comment='#工程名字#')
    visitor = Column(String(30), comment='#拜访人名字#')
    visitor_title = Column(String(100), comment='#拜访人职务#')
    visit_objective = Column(TINYINT(4), comment='#拜访目的#ENUM#')
    visit_mode = Column(TINYINT(4), comment='#拜访方式#ENUM#0:上门拜访:visit,1:电话联系:phone,2:微信联系:wechat,3:其他:other')
    visit_time = Column(DateTime, comment='#拜访人时间#')
    summary = Column(String(300), comment='#描述/总结#')
    next_visit_time = Column(DateTime, comment='#下次拜访时间#')
    address_title = Column(String(100), comment='#定位地址标题#')
    address = Column(String(200), comment='#定位地址#')
    lat = Column(String(20), comment='#定位经度#')
    lng = Column(String(20), comment='#定位纬度#')
    type = Column(TINYINT(4), server_default=text("'0'"), comment='#类型#ENUM#0:客户:customer,1:商户:tenant,2:工程:project#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')


class BVisitPicture(Base):
    __tablename__ = 'b_visit_picture'
    __table_args__ = {'comment': '拜访信息-照片关联表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    visit_info_id = Column(BIGINT(20), comment='#拜访信息id#')
    url = Column(String(1000), comment='#文件链接#')
    file_id = Column(BIGINT(22), comment='#文件ID#')
    file_name = Column(String(200), comment='#文件名#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常:normal,1:删除:delete#')
    extension = Column(String(100), comment='#文件拓展名#')


class BWorkReportCustomerDayDetail(Base):
    __tablename__ = 'b_work_report_customer_day_detail'
    __table_args__ = {'comment': '客户日报工明细'}

    id = Column(BIGINT(22), primary_key=True, comment='#主键id#')
    code = Column(String(25), comment='#编号#')
    source_id = Column(BIGINT(20), comment='#来源id#')
    source_code = Column(String(25), comment='#来源编号#')
    enter_id = Column(BIGINT(20), comment='#进场单id#')
    customer_id = Column(BIGINT(20), comment='#客户id#')
    customer_name = Column(String(50), comment='#客户名称#')
    brand_id = Column(BIGINT(22), comment='#品牌id#')
    brand_name = Column(String(100), comment='#品牌名称#')
    model = Column(String(255), comment='#设备型号#')
    device_no = Column(String(50), comment='#设备序列号#')
    num = Column(DECIMAL(18, 2), comment='#使用时长#')
    contract_id = Column(BIGINT(20), comment='#租赁合同id#')
    contract_code = Column(String(50), comment='#租凭合同编号#')
    order_id = Column(BIGINT(20), comment='#租赁订单id#')
    order_code = Column(String(25), comment='#租赁订单编号#')
    order_device_id = Column(BIGINT(20), comment='#b_customer_order_device.id#')
    order_valuation_id = Column(BIGINT(20), comment='#b_customer_order_valuation.id#')
    device_category_id = Column(BIGINT(20), comment='#设备品类id#')
    device_category_name = Column(String(100), comment='#设备品类名称#')
    leasing_model = Column(TINYINT(4), comment='#租赁方式#')
    valuation_way = Column(TINYINT(4), comment='#计价方式#')
    work_report_type = Column(TINYINT(4), comment='#报工类型#')
    start_time = Column(DateTime, comment='#开始时间#')
    end_time = Column(DateTime, comment='#结束时间#')
    project_id = Column(BIGINT(20), comment='#工程id#')
    project_name = Column(String(100), comment='#工程名称#')
    province_code = Column(VARCHAR(50), comment='#省code#')
    province_name = Column(VARCHAR(50), comment='#省份名称#')
    city_code = Column(VARCHAR(50), comment='#市code#')
    city_name = Column(VARCHAR(50), comment='#城市名称#')
    district_code = Column(VARCHAR(50), comment='#区code#')
    district_name = Column(VARCHAR(50), comment='#区域名称#')
    address = Column(String(500), comment='#地址#')
    status = Column(TINYINT(4), comment='#状态#')
    disabled = Column(TINYINT(1), server_default=text("'0'"), comment='#是否已作废#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')
    version = Column(INTEGER(11), comment='#数据版本#')


class BWorkReportCustomerDetail(Base):
    __tablename__ = 'b_work_report_customer_detail'
    __table_args__ = {'comment': '客户作业报工明细表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    code = Column(String(25), comment='#编号#')
    customer_id = Column(BIGINT(20), comment='#客户id#')
    customer_name = Column(String(50), comment='#客户名称#')
    task_detail_id = Column(BIGINT(20), comment='#任务明细id#b_task_report_detail.id')
    enter_id = Column(BIGINT(20), comment='#进场单id#')
    brand_id = Column(BIGINT(20), comment='#品牌id#')
    brand_name = Column(String(50), comment='#品牌名称#')
    model = Column(String(255), comment='#设备型号#')
    device_no = Column(String(50), comment='#设备序列号#')
    master_id = Column(BIGINT(20), comment='#机手id#')
    master_phone = Column(String(20), comment='#机手手机#')
    master_name = Column(String(50), comment='#机手姓名#')
    work_date = Column(Date, comment='#作业日期#')
    num = Column(DECIMAL(18, 2), comment='#使用时长#')
    contract_id = Column(BIGINT(20), comment='#租赁合同id#')
    contract_code = Column(String(50), comment='#租凭合同编号#')
    order_id = Column(BIGINT(20), comment='#租赁订单id#')
    order_code = Column(String(25), comment='#租赁订单编号#')
    order_device_id = Column(BIGINT(20), comment='#b_customer_order_device.id#')
    order_valuation_id = Column(BIGINT(20), comment='#b_customer_order_valuation.id#')
    device_category_id = Column(BIGINT(20), comment='#设备品类id#')
    device_category_name = Column(String(100), comment='#设备品类#')
    leasing_model = Column(TINYINT(4), comment='#租赁方式#')
    valuation_way = Column(TINYINT(4), comment='#计价方式#')
    work_report_type = Column(TINYINT(4), comment='#报工类型#')
    machine_team_num = Column(DECIMAL(18, 2), comment='#台班量#')
    project_id = Column(BIGINT(20), comment='#工程id#')
    project_name = Column(String(100), comment='#工程名称#')
    province_code = Column(VARCHAR(50), comment='#省code#')
    province_name = Column(VARCHAR(50), comment='#省份名称#')
    city_code = Column(VARCHAR(50), comment='#市code#')
    city_name = Column(VARCHAR(50), comment='#城市名称#')
    district_code = Column(VARCHAR(50), comment='#区code#')
    district_name = Column(VARCHAR(50), comment='#区域名称#')
    address = Column(String(500), comment='#地址#')
    status = Column(TINYINT(4), comment='#状态#')
    break_flag = Column(TINYINT(1), server_default=text("'0'"), comment='#违约标志#0:不违约；1:违约#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')
    version = Column(INTEGER(11), comment='#数据版本#')


class BWorkReportDayValuationSnapshoot(Base):
    __tablename__ = 'b_work_report_day_valuation_snapshoot'
    __table_args__ = {'comment': '日报工计价方式快照'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    work_report_day_id = Column(BIGINT(20), comment='#日报工id#')
    work_report_type = Column(TINYINT(4), comment='#报工类型#')
    type = Column(TINYINT(4), comment='#类型#ENUM#0:客户:CUSTOMER,1:商户:TENANT#')
    valuation_obj = Column(Text, comment='#计价方式对象（json结构）#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    modifier = Column(String(25), server_default=text("''"), comment='修改人')
    update_time = Column(DateTime, comment='修改时间')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='逻辑删除#ENUM#0:正常,1:删除')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')


class BWorkReportDeviceParameter(Base):
    __tablename__ = 'b_work_report_device_parameter'
    __table_args__ = {'comment': '报工设备参数'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    work_report_id = Column(BIGINT(20), comment='#报工id#')
    device_category_id = Column(BIGINT(20), comment='#设备品类#')
    device_param_id = Column(BIGINT(20), comment='#设备规格参数id#')
    device_param_name = Column(String(50), comment='#设备规格参数名称#')
    device_param_value = Column(DECIMAL(18, 2), comment='#参数值#')
    unit_id = Column(BIGINT(20), comment='#计量单位id#')
    unit_name = Column(String(25), comment='#计量单位（冗余）#')
    unit_en_name = Column(String(25), comment='#英文计量单位（冗余）#')
    type = Column(TINYINT(4), comment='#类型#ENUM#0:商户作业报工:TENANT_PARAM,1:客户作业报工:CUSTOMER_PARAM,2:商户日报工:TENANT_DAY_PARAM,3:客户日报工:CUSTOMER_DAY_PARAM#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    modifier = Column(String(25), server_default=text("''"), comment='修改人')
    update_time = Column(DateTime, comment='修改时间')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='逻辑删除#ENUM#0:正常,1:删除')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')


class BWorkReportTenantDayDetail(Base):
    __tablename__ = 'b_work_report_tenant_day_detail'
    __table_args__ = {'comment': '商户日报工明细'}

    id = Column(BIGINT(22), primary_key=True, comment='#主键id#')
    code = Column(String(25), comment='#编号#')
    source_id = Column(BIGINT(20), comment='#来源id#')
    source_code = Column(String(25), comment='#来源编号#')
    enter_id = Column(BIGINT(20), comment='#进场单id#')
    tenant_id = Column(BIGINT(20), comment='#商户id#')
    tenant_name = Column(String(100), comment='#商户名称#')
    brand_id = Column(BIGINT(22), comment='#品牌id#')
    brand_name = Column(String(100), comment='#品牌名称#')
    model = Column(String(255), comment='#设备型号#')
    device_no = Column(String(50), comment='#设备序列号#')
    num = Column(DECIMAL(18, 2), comment='#使用时长#')
    contract_id = Column(BIGINT(20), comment='#转租合同id#')
    contract_code = Column(String(50), comment='#转租合同编号#')
    order_id = Column(BIGINT(20), comment='#转租订单id#')
    order_code = Column(String(25), comment='#转租订单编号#')
    order_device_id = Column(BIGINT(20), comment='#商户转租订单设备id#tenant_order_device.id#')
    order_valuation_id = Column(BIGINT(20), comment='#商户转租订单设备计价方式##b_tenant_order_valuation.id#')
    device_category_id = Column(BIGINT(20), comment='#设备品类id#')
    device_category_name = Column(String(100), comment='#设备品类#')
    leasing_model = Column(TINYINT(4), comment='#租赁方式#')
    valuation_way = Column(TINYINT(4), comment='#计价方式#')
    work_report_type = Column(TINYINT(4), comment='#报工类型#')
    start_time = Column(DateTime, comment='#开始时间#')
    end_time = Column(DateTime, comment='#结束时间#')
    project_id = Column(BIGINT(20), comment='#工程id#')
    project_name = Column(String(100), comment='#工程名称#')
    province_code = Column(VARCHAR(50), comment='#省code#')
    province_name = Column(VARCHAR(50), comment='#省份名称#')
    city_code = Column(VARCHAR(50), comment='#市code#')
    city_name = Column(VARCHAR(50), comment='#城市名称#')
    district_code = Column(VARCHAR(50), comment='#区code#')
    district_name = Column(VARCHAR(50), comment='#区域名称#')
    address = Column(String(500), comment='#地址#')
    status = Column(TINYINT(4), comment='#状态#')
    disabled = Column(TINYINT(1), server_default=text("'0'"), comment='#是否已作废#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')
    version = Column(INTEGER(11), comment='#数据版本#')


class BWorkReportTenantDetail(Base):
    __tablename__ = 'b_work_report_tenant_detail'
    __table_args__ = {'comment': '客户作业报工明细表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    code = Column(String(25), comment='#编号#')
    tenant_id = Column(BIGINT(20), comment='#商户id#')
    tenant_name = Column(String(100), comment='#商户名称#')
    task_detail_id = Column(BIGINT(20), comment='#任务明细id#b_task_report_detail.id')
    enter_id = Column(BIGINT(20), comment='#进场单id#')
    brand_id = Column(BIGINT(20), comment='#品牌id#')
    brand_name = Column(String(50), comment='#品牌名称#')
    model = Column(String(255), comment='#设备型号#')
    device_no = Column(String(50), comment='#设备序列号#')
    master_id = Column(BIGINT(20), comment='#机手id#')
    master_phone = Column(String(20), comment='#机手手机#')
    master_name = Column(String(50), comment='#机手姓名#')
    work_date = Column(Date, comment='#作业日期#')
    num = Column(DECIMAL(18, 2), comment='#使用时长#')
    contract_id = Column(BIGINT(20), comment='#转租合同id#')
    contract_code = Column(String(50), comment='#转租合同编号#')
    order_id = Column(BIGINT(20), comment='#转租订单id#')
    order_code = Column(String(25), comment='#转租订单编号#')
    order_device_id = Column(BIGINT(20), comment='#商户转租订单设备id#tenant_order_device.id#')
    order_valuation_id = Column(BIGINT(20), comment='#商户转租订单设备计价方式##b_tenant_order_valuation.id#')
    device_category_id = Column(BIGINT(20), comment='#设备品类id#')
    device_category_name = Column(String(100), comment='#设备品类#')
    leasing_model = Column(TINYINT(4), comment='#租赁方式#')
    valuation_way = Column(TINYINT(4), comment='#计价方式#')
    work_report_type = Column(TINYINT(4), comment='#报工类型#')
    machine_team_num = Column(DECIMAL(18, 2), comment='#台班量#')
    project_id = Column(BIGINT(20), comment='#工程id#')
    project_name = Column(String(100), comment='#工程名称#')
    province_code = Column(VARCHAR(50), comment='#省code#')
    province_name = Column(VARCHAR(50), comment='#省份名称#')
    city_code = Column(VARCHAR(50), comment='#市code#')
    city_name = Column(VARCHAR(50), comment='#城市名称#')
    district_code = Column(VARCHAR(50), comment='#区code#')
    district_name = Column(VARCHAR(50), comment='#区域名称#')
    address = Column(String(500), comment='#地址#')
    status = Column(TINYINT(4), comment='#状态#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')
    version = Column(INTEGER(11), comment='#数据版本#')


class FlywaySchemaHistory(Base):
    __tablename__ = 'flyway_schema_history'

    installed_rank = Column(INTEGER(11), primary_key=True)
    version = Column(String(50))
    description = Column(String(200), nullable=False)
    type = Column(String(20), nullable=False)
    script = Column(String(1000), nullable=False)
    checksum = Column(INTEGER(11))
    installed_by = Column(String(100), nullable=False)
    installed_on = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    execution_time = Column(INTEGER(11), nullable=False)
    success = Column(TINYINT(1), nullable=False, index=True)


class Shedlock(Base):
    __tablename__ = 'shedlock'

    name = Column(String(64), primary_key=True)
    lock_until = Column(TIMESTAMP(fsp=3), nullable=False)
    locked_at = Column(TIMESTAMP(fsp=3), nullable=False, server_default=text("CURRENT_TIMESTAMP(3)"))
    locked_by = Column(String(255), nullable=False)
