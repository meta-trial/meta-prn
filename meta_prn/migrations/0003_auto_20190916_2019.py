# Generated by Django 2.2.3 on 2019-09-16 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("meta_prn", "0002_auto_20190910_2345")]

    operations = [
        migrations.RemoveField(model_name="historicaldeathreport", name="action_item"),
        migrations.RemoveField(model_name="historicaldeathreport", name="history_user"),
        migrations.RemoveField(
            model_name="historicaldeathreport", name="parent_action_item"
        ),
        migrations.RemoveField(
            model_name="historicaldeathreport", name="related_action_item"
        ),
        migrations.RemoveField(model_name="historicaldeathreport", name="site"),
        migrations.DeleteModel(name="DeathReport"),
        migrations.DeleteModel(name="HistoricalDeathReport"),
    ]