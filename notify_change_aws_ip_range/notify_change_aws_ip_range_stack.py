from aws_cdk import (
    aws_sns as sns,
    # aws_sns_subscriptions as subs,
    core
)


class NotifyChangeAwsIpRangeStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        topic = sns.Topic(
            self, "HelloCdkTopic"
        )
        # topic.add_subscription(subs.UrlSubscription("https://foobar.com/"))
