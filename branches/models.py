# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.db import models

class Branch(models.Model):
    branchid = models.IntegerField(blank=False, null=False, primary_key=True)
    lineid = models.ForeignKey('Line', models.DO_NOTHING, db_column='lineid')
    frombusid = models.ForeignKey('Bus', models.DO_NOTHING, db_column='frombusid',
                related_name='frombus')
    tobusid = models.ForeignKey('Bus', models.DO_NOTHING, db_column='tobusid',
                related_name='tobus')
    ckt = models.CharField(max_length=2, blank=True, null=True)
    branchname = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.branchname

    class Meta:
        #managed = False
        db_table = 'branch'


class Bus(models.Model):
    busid = models.IntegerField(blank=False, null=False, primary_key=True)
    busnum = models.IntegerField(blank=True, null=True)
    busname = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'bus'

    def __str__(self):
        return self.busname


class Equipment(models.Model):
    equipmentid = models.IntegerField(blank=False, null=False, primary_key=True)
    branchid = models.ForeignKey(Branch, models.DO_NOTHING, db_column='branchid')
    busid = models.ForeignKey(Bus, models.DO_NOTHING, db_column='busid')
    equipmentname = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.equipmentname

    class Meta:
        #managed = False
        db_table = 'equipment'


class Line(models.Model):
    lineid = models.IntegerField(blank=False, null=False, primary_key=True)
    linename = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.linename

    class Meta:
        #managed = False
        db_table = 'line'
