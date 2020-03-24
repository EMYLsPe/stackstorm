import boto3
from st2common.runners.base_action import Action


class EODNSRoute:

    def run(self, host, target):
        self.host = host
        self.target = target

        hostArray = host.split(".")
        length = len(hostArray)
        hostZone = hostArray[length-3] + "." + hostArray[length-2] + "." + hostArray[length-1]

#         if hostZone == "bite.pearsondev.tech":
        if hostZone == "dev.prsn.io":
            return (True, self.createRoute53Entry())
        else:
            return False, "Given host is not permitted in bite.pearsondev.tech hostZone"


    def createRoute53Entry(self):
        client = boto3.client('route53')

        response = client.change_resource_record_sets(
            HostedZoneId='Z10308243O3W8MXERVWSX',
            ChangeBatch={
                'Changes': [
                    {
                        'Action': 'CREATE',
                        'ResourceRecordSet': {
                            'Name': self.host,
                            'Type': 'CNAME',
                            'TTL': 300,
                            'ResourceRecords': [
                                {
                                    'Value': self.target
                                },
                            ]
                        }
                    },
                ]
            }
        )

        return response
