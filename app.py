#!/usr/bin/env python3

from aws_cdk import core

from notify_change_aws_ip_range.notify_change_aws_ip_range_stack import NotifyChangeAwsIpRangeStack


app = core.App()
NotifyChangeAwsIpRangeStack(app, "notify-change-aws-ip-range")

app.synth()
