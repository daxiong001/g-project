# coding: utf-8
from sqlalchemy import Column, DateTime, String, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, TINYINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class BBaseDept(Base):
    __tablename__ = 'b_base_dept'
    __table_args__ = {'comment': '部门表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    parent_id = Column(BIGINT(20), server_default=text("'0'"), comment='#父部门id#')
    ancestors = Column(VARCHAR(1024), server_default=text("''"), comment='#祖级列表#')
    name = Column(VARCHAR(30), server_default=text("''"), comment='#部门名称#')
    sort = Column(INTEGER(11), server_default=text("'0'"), comment='#排序#')
    status = Column(TINYINT(4), server_default=text("'0'"), comment='#状态#ENUM#1:正常,2:停用#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BBaseMenu(Base):
    __tablename__ = 'b_base_menu'
    __table_args__ = {'comment': '权限菜单表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    parent_id = Column(BIGINT(20), nullable=False, comment='#上级id#')
    menu_code = Column(String(100), comment='#编号#')
    menu_name = Column(String(100), nullable=False, comment='#菜单名称#')
    sort = Column(INTEGER(11), nullable=False, server_default=text("'0'"), comment='#排序#')
    menu_path = Column(String(200), comment='#菜单地址#')
    type = Column(TINYINT(4), nullable=False, comment='#菜单类型#ENUM#1:菜单,2:按钮#')
    icon = Column(String(200), comment='#菜单图标#')
    remark = Column(String(255), comment='#备注#')
    menu_show = Column(TINYINT(1), server_default=text("'1'"), comment='#是否展示#')
    web_type = Column(TINYINT(4), comment='#网站类型#ENUM#1:运营后台端:OPERATION_ADMIN,2:商家web端:MERCHANT_WEB,3:机手小程序端:ROBOT_APPLETS#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BBaseMenuAuth(Base):
    __tablename__ = 'b_base_menu_auth'
    __table_args__ = {'comment': '菜单接口权限表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    menu_id = Column(BIGINT(20), nullable=False, comment='#菜单id#REF#b_base_menu.id#')
    auth_path = Column(String(1000), comment='#接口地址#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BBaseRole(Base):
    __tablename__ = 'b_base_role'
    __table_args__ = {'comment': '角色表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    type = Column(TINYINT(4), nullable=False, server_default=text("'2'"), comment='#角色类型#ENUM#1:预置角色:PRESET,2:自定义角色:CUSTOM#')
    name = Column(String(100), nullable=False, comment='#角色名称#')
    code = Column(String(100), nullable=False, comment='#角色编码#')
    remark = Column(String(200), comment='#备注#')
    data_scope = Column(TINYINT(4), nullable=False, comment='#数据范围#ENUM#1:全部:ALL,2:自定义:CUSTOM,3:部门:DEPT,4:部门及下级部门:DEPT_AND_CHILD,5:本人:SELF#')
    status = Column(TINYINT(4), nullable=False, server_default=text("'0'"), comment='#状态#ENUM#1:正常,2:停用#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BBaseRoleDataScope(Base):
    __tablename__ = 'b_base_role_data_scope'
    __table_args__ = {'comment': '角色和部门关联表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    role_id = Column(BIGINT(20), nullable=False, comment='#角色id#')
    dept_id = Column(BIGINT(20), nullable=False, comment='#部门id#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BBaseRoleMenu(Base):
    __tablename__ = 'b_base_role_menu'
    __table_args__ = {'comment': '角色菜单表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    role_id = Column(BIGINT(20), nullable=False, comment='#角色id#RFE#b_base_role.id#')
    menu_id = Column(BIGINT(20), nullable=False, comment='#菜单id#REF#b_base_menu.id#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BBaseSy(Base):
    __tablename__ = 'b_base_sys'
    __table_args__ = {'comment': '系统表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    name = Column(String(50), comment='#系统名称#')
    web_type = Column(TINYINT(4), comment='#网站类型#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BBaseUser(Base):
    __tablename__ = 'b_base_user'
    __table_args__ = {'comment': '用户表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键ID#')
    type = Column(TINYINT(4), comment='#用户类型ENUM#1:运营后台2:商家,3:机手#')
    dept_ids = Column(String(1000), nullable=False, comment='#部门id,多个用逗号隔开#')
    username = Column(String(50), comment='#用户名#')
    real_name = Column(String(200), comment='#真实姓名#')
    real_name_pinyin = Column(String(200), comment='#真实姓名拼音#')
    password = Column(String(255), comment='#密码#')
    mobile = Column(String(50), comment='#手机号#')
    first_login_time = Column(DateTime, comment='#第一次登录时间#')
    last_login_time = Column(DateTime, comment='#最后登录时间#')
    status = Column(TINYINT(4), server_default=text("'0'"), comment='#用户状态#ENUM#1:正常,2:停用#')
    admin = Column(TINYINT(1), server_default=text("'0'"), comment='#是否为管理员#')
    wei_xin_openid = Column(String(100), comment='#微信用户唯一标识#')
    wei_xin_union_id = Column(String(100), comment='#用户在微信开放平台的唯一标识符#')
    version = Column(INTEGER(11), comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BBaseUserDept(Base):
    __tablename__ = 'b_base_user_dept'
    __table_args__ = {'comment': '用户部门关联表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    user_id = Column(BIGINT(20), nullable=False, comment='#用户id#REF#b_base_user.id#')
    dept_id = Column(BIGINT(20), nullable=False, comment='#部门id#REF#b_base_dept.id#')
    dept_name = Column(String(50), comment='#部门名称#')
    version = Column(INTEGER(11), nullable=False, comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')


class BBaseUserRole(Base):
    __tablename__ = 'b_base_user_role'
    __table_args__ = {'comment': '用户角色表'}

    id = Column(BIGINT(20), primary_key=True, comment='#主键id#')
    user_id = Column(BIGINT(20), nullable=False, comment='#用户id#REF#b_base_user.id#')
    role_id = Column(BIGINT(20), nullable=False, comment='#角色id#REF#b_base_role.id#')
    version = Column(INTEGER(11), nullable=False, comment='#数据版本#')
    creator_id = Column(BIGINT(20), comment='#创建人id#')
    creator = Column(String(25), server_default=text("''"), comment='#创建人#')
    create_time = Column(DateTime, comment='#创建时间#')
    modifier_id = Column(BIGINT(20), comment='#修改人id#')
    modifier = Column(String(25), server_default=text("''"), comment='#修改人#')
    update_time = Column(DateTime, comment='#修改时间#')
    delete_flag = Column(TINYINT(4), server_default=text("'0'"), comment='#逻辑删除#ENUM#0:正常,1:删除#')
