# Generated by Django 5.1 on 2024-09-19 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0005_propage"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactMe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("FirstName", models.CharField(max_length=30)),
                ("LastName", models.CharField(max_length=30)),
                ("Email", models.CharField(max_length=50)),
                ("Message", models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name="reg",
            name="email",
        ),
        migrations.AddField(
            model_name="reg",
            name="Email",
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
