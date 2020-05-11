import json
import pytest

from aws_cdk import core
# from hello-cdk.hello_cdk_stack import HelloCdkStack
from notify_change_aws_ip_range.notify_change_aws_ip_range_stack import NotifyChangeAwsIpRangeStack


def get_template():
    app = core.App()
    stack_name = 'notify-change-aws-ip-range'
    NotifyChangeAwsIpRangeStack(app, stack_name)
    return json.dumps(app.synth().get_stack(stack_name).template)


def test_sns_tpic_not_created():
    assert(not("AWS::SNS::Topic" in get_template()))

def test_sns_subscription_created():
    assert("AWS::SNS::Subscription" in get_template())
