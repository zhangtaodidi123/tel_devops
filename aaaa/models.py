from django.db import models

from django.contrib import admin

from django.db import models

from django.db import models




class University(models.Model):
    # id = models.IntegerField(primary_key=False)
    createdat = models.CharField(max_length=50, verbose_name='创建时间')  # Field name made lowercase.
    updatedat = models.CharField(max_length=50, verbose_name='更新时间')  # Field name made lowercase.
    hostname = models.CharField(max_length=50, verbose_name='主机名称')
    tigger = models.CharField(max_length=100, verbose_name='报警名称')
    media = models.CharField(max_length=100, verbose_name='通知媒介')
    tel_log = models.CharField(max_length=100, verbose_name='电话日志记录')
    queren = models.CharField(max_length=100, verbose_name='是否确认')
    class Meta:
        verbose_name = '电话报警相关记录'
        verbose_name_plural = '电话报警相关记录'
        managed = True
        db_table = 'university'

    def __str__(self):
        return self.hostname


class alert(models.Model):
    ipaddress =  models.CharField(max_length=50, verbose_name='主机名称')
    alert = models.CharField(max_length=100, verbose_name='报警名称')
    class Meta:
        verbose_name = '当前zabbix平台所有报警'
        verbose_name_plural = '当前zabbix平台所有报警'
        managed = True
        db_table = 'now_alert'
    def __str__(self):
        return self.ipaddress

class now_alert(models.Model):
    ipaddress =  models.CharField(max_length=50, verbose_name='主机名称')
    alert = models.CharField(max_length=100, verbose_name='报警名称')
    class Meta:
        verbose_name = '当前zabbix平台所有报警'
        verbose_name_plural = '当前zabbix平台所有报警'
        managed = True
        db_table = '2_now_alert'
    def __str__(self):
        return self.ipaddress


class alert_level(models.Model):
    name = models.CharField(max_length=50,verbose_name="报警关键字")
    level = models.CharField(max_length=50,verbose_name="报警级别")

    class Meta:
        verbose_name='报警级别设置'
        verbose_name_plural = '报警级别设置'
        managed = True
        db_table = 'alert_level'




class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Jenkins_data(models.Model):
    data = models.CharField(max_length=50) # 日期列
    job_name = models.CharField(max_length=50) # 项目名称列
    fabu_all_count = models.CharField(max_length=20) #发布总次数列
    prd_success = models.CharField(max_length=20) # 生产成功数
    prd_abort = models.CharField(max_length=20) #生产回滚数
    prd_faill = models.CharField(max_length=20) #生产失败数
    fat_success = models.CharField(max_length=20) #测试成功数
    fat_abort = models.CharField(max_length=20) #测试回滚数
    fat_faill = models.CharField(max_length=20) # 测试失败
    all_success = models.CharField(max_length=20) #总成功数
    all_faill = models.CharField(max_length=20) # 总失败数
    all_abort = models.CharField(max_length=20) # 总回滚数

'''CMDB数据库表结构设计'''

'''部门信息的表结构设计'''
class Department(models.Model):
    name = models.CharField(max_length=32, verbose_name='部门名称', unique=True)
    comment = models.CharField(max_length=128, verbose_name='备注', null=True, blank=True)
    class Meta:
        verbose_name = '部门'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class DataCenter(models.Model):
    '''机房区域'''
    name = models.CharField(max_length=32, verbose_name='机房区域')
    manufactory_choices = (
        (0, 'UCloud'),
        (1, 'Aliyun')
    )
    manufactory = models.SmallIntegerField(choices=manufactory_choices, default=0, verbose_name='云服务商')
    address = models.CharField(max_length=128, verbose_name='机房地址', null=True, blank=True)
    project_name = models.CharField(max_length=32, verbose_name='所属项目')
    email = models.CharField(max_length=32, verbose_name='邮箱', null=True, blank=True)
    mobile = models.CharField(max_length=16, verbose_name='联系方式', null=True, blank=True)
    comment = models.TextField(max_length=256, verbose_name='备注', null=True, blank=True)

    class Meta:
        unique_together = (('name', 'project_name'),)
        verbose_name = '机房区域'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s -- %s' % (self.project_name, self.name)


class EIP(models.Model):
    name = models.CharField(max_length=32, verbose_name='EIP名称')
    ip_address = models.GenericIPAddressField(protocol='ipv4', verbose_name='IP地址', unique=True)
    bandwidth = models.CharField(max_length=16, verbose_name='带宽(MB)')
    band_status_choices = (
        (0, '已绑定'),
        (1, '未绑定')
    )
    band_status = models.SmallIntegerField(choices=band_status_choices, verbose_name='绑定状态')
    data_center = models.ForeignKey('DataCenter', verbose_name='机房区域', on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.CharField(max_length=256, verbose_name='备注', null=True, blank=True)

    class Meta:
        verbose_name = 'EIP'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ip_address

class ULB(models.Model):
    name = models.CharField(max_length=32, verbose_name='ULB名称')
    base_network = models.GenericIPAddressField(protocol='ipv4', verbose_name='基础网络', unique=True)
    eip = models.OneToOneField('EIP', verbose_name='EIP' ,on_delete=models.SET_NULL, null=True, blank=True)
    data_center = models.ForeignKey('DataCenter', verbose_name='机房区域', on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.CharField(max_length=128, verbose_name='备注', null=True, blank=True)

    class Meta:
        verbose_name = 'ULB'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class OsType(models.Model):
    '''系统类型'''
    name = models.CharField(max_length=32, verbose_name='系统类型')
    version = models.CharField(max_length=32, verbose_name='系统版本')

    class Meta:
        verbose_name = '系统类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s -- %s' % (self.name, self.version)


class BusinessUnit(models.Model):
    '''业务线'''
    name = models.CharField(max_length=64, verbose_name='业务线', unique=True)
    owner = models.ForeignKey('user', verbose_name='负责人', on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.CharField(max_length=128, verbose_name='备注', null=True, blank=True)

    class Meta:
        verbose_name = '业务线'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class AppUnit(models.Model):
    '''应用表'''
    name = models.CharField(max_length=64, verbose_name='应用名称', unique=True)
    business_unit = models.ForeignKey('BusinessUnit', verbose_name='所属业务线', on_delete=models.SET_NULL, null=True, blank=True)
    owner = models.ForeignKey('User', verbose_name='应用负责人', on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.CharField(max_length=128, verbose_name='备注', null=True, blank=True)

    class Meta:
        verbose_name = 'APP'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



class Domain(models.Model):
    '''域名表'''
    domain = models.CharField(max_length=32, verbose_name='域名', unique=True)
    app_unit = models.ForeignKey('AppUnit', verbose_name='App应用', on_delete=models.SET_NULL, null=True, blank=True)
    owner = models.ForeignKey('user', verbose_name='负责人', on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.CharField(max_length=256, verbose_name='备注', null=True, blank=True)

    class Meta:
        verbose_name = '域名'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.domain



class Hosts(models.Model):
    '''主机信息'''
    name = models.CharField(max_length=32, verbose_name='主机名称', unique=True)
    cpu = models.CharField(max_length=8, verbose_name='CPU核数')
    memory = models.CharField(max_length=8, verbose_name='内存大小(MB)')
    disk = models.CharField(max_length=16, verbose_name='磁盘大小(GB)')
    ip_in = models.GenericIPAddressField(protocol='ipv4', verbose_name='内网IP', unique=True)
    ip_out = models.GenericIPAddressField(protocol='ipv4', verbose_name='外网IP', null=True, blank=True)
    eip = models.OneToOneField('EIP', on_delete=models.SET_NULL, null=True, blank=True)
    # domain = models.ManyToManyField('Domain', verbose_name='所属域名')
    app_unit = models.ForeignKey('AppUnit', verbose_name='App应用', on_delete=models.SET_NULL, null=True, blank=True)
    ulb = models.ForeignKey('ULB', verbose_name='所属ULB', on_delete=models.SET_NULL, null=True, blank=True)
    os_type = models.ForeignKey('OsType', verbose_name='系统类型', on_delete=models.SET_NULL, null=True, blank=True)
    data_center = models.ForeignKey('DataCenter', verbose_name='机房区域', on_delete=models.SET_NULL, null=True, blank=True)
    status_choices = (
        (0, '在线'),
        (1, '下线'),
        (2, '空闲')
    )
    host_status = models.SmallIntegerField(choices=status_choices,verbose_name='状态', default=0)
    comment = models.TextField(max_length=256, verbose_name='备注', null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True, blank=True)
    update_date = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        verbose_name = '主机信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name