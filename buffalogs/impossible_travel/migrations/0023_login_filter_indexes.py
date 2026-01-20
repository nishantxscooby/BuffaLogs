from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("impossible_travel", "0022_remove_tasksettings_unique_task_execution_mode_and_more"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="login",
            index=models.Index(fields=["timestamp"], name="login_timestamp_idx"),
        ),
        migrations.AddIndex(
            model_name="login",
            index=models.Index(fields=["ip"], name="login_ip_idx"),
        ),
        migrations.AddIndex(
            model_name="login",
            index=models.Index(fields=["country"], name="login_country_idx"),
        ),
        migrations.AddIndex(
            model_name="login",
            index=models.Index(fields=["event_id"], name="login_event_id_idx"),
        ),
    ]
