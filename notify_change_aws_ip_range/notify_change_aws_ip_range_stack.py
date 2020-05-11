from aws_cdk import (
    aws_sns as sns,
    aws_sns_subscriptions as subs,
    core
)


class NotifyChangeAwsIpRangeStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        topic = sns.Topic.from_topic_arn(self, 'AmazonIpSpaceChanged', topic_arn = 'arn:aws:sns:us-east-1:806199016981:AmazonIpSpaceChanged')
        topic.add_subscription(subs.UrlSubscription("https://hogehoge.com"))
