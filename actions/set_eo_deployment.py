from st2common.runners.base_action import Action


deploymentTemplate = {
    "apiVersion": "extensions/v1beta1",
    "kind": "Deployment",
    "metadata": {
        "labels": {"name": "environment-operator"},
        "name": "environment-operator",
        "namespace": ""
    },
    "spec": {
        "progressDeadlineSeconds": 600,
        "replicas": 1,
        "revisionHistoryLimit": 10,
        "selector": {"matchLabels": {"name": "environment-operator"}},
        "strategy": {"rollingUpdate": {"maxSurge": 1, "maxUnavailable": 1}, "type": "RollingUpdate"},
        "template": {
            "metadata": {
                "labels": {"name": "environment-operator", "app": "environment-operator", "version": "v1.0.0"},
                "name": "environment-operator"
            },
            "spec": {
                "automountServiceAccountToken": True,
                "containers": [
                    {
                        "env": [
                            {
                                "name": "GIT_REMOTE_REPOSITORY",
                                "value": ""
                            },
                            {
                                "name": "GIT_BRANCH",
                                "value": ""
                            },
                            {
                                "name": "GIT_PRIVATE_KEY",
                                "valueFrom": {
                                    "secretKeyRef": {"key": "key", "name": "git-private-key"}
                                }
                            },
                            {
                                "name": "DOCKER_REGISTRY",
                                "value": "815492460363.dkr.ecr.us-east-1.amazonaws.com"
                            },
                            {
                                "name": "PROJECT",
                                "value": ""
                            },
                            {
                                "name": "ENVIRONMENT_NAME",
                                "value": ""
                            },
                            {
                                "name": "BITESIZE_FILE",
                                "value": ""
                            },
                            {
                                "name": "AUTH_TOKEN_FILE",
                                "value": "/etc/auth/token"
                            },
                            {
                                "name": "DEBUG",
                                "value": "false"
                            },
                            {
                                "name": "NAMESPACE",
                                "valueFrom": {
                                    "fieldRef": {"apiVersion": "v1", "fieldPath": "metadata.namespace"}
                                }
                            },
                            {
                                "name": "EXTERNAL_CRD_EXTERNAL_SECRETS_ENABLED",
                                "value": "true"
                            },
                            {
                                "name": "ENVIRONMENT",
                                "value": ""
                            },
                            {
                                "name": "AWS_REGION",
                                "value": ""
                            },
                            {
                                "name": "ENVTYPE",
                                "value": ""
                            }
                        ],
                        "image": "",
                        "imagePullPolicy": "Always",
                        "name": "environment-operator",
                        "ports": [{"containerPort": 8080, "protocol": "TCP"}],
                        "resources": {},
                        "securityContext": {"procMount": "Default", "runAsUser": 1000},
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "volumeMounts": [
                            {
                                "mountPath": "/etc/auth",
                                "name": "auth-token",
                                "readOnly": True
                            },
                            {
                                "mountPath": "/etc/git",
                                "name": "git-key",
                                "readOnly": True
                            }
                        ]
                    }
                ],
                "dnsPolicy": "ClusterFirst",
                "restartPolicy": "Always",
                "schedulerName": "default-scheduler",
                "securityContext": {},
                "serviceAccount": "environment-operator",
                "serviceAccountName": "environment-operator",
                "terminationGracePeriodSeconds": 30,
                "volumes": [
                    {
                        "name": "auth-token",
                        "secret": {"defaultMode": 420, "secretName": "auth-token-file"}
                    },
                    {
                        "name": "git-key",
                        "secret": {"defaultMode": 420,  "secretName": "git-private-key"}
                    }
                ]
            }
        }
    }
}


class CreateEODeployment(Action):

    def run(self, namespace, gitRemoteRepository, gitBranch, project, environmentType, bitesizeFile, imageVersion, environment, awsRegion, image):

        self.namespace           = namespace
        self.gitRemoteRepository = gitRemoteRepository
        self.gitBranch           = gitBranch
        self.project             = project
        self.environmentType     = environmentType
        self.bitesizeFile        = bitesizeFile
        self.imageVersion        = imageVersion
        self.environment         = environment
        self.awsRegion           = awsRegion
        self.image               = image

        return (True, self._createDeploymentConfig())

    def _createDeploymentConfig(self):
        myconf = deploymentTemplate
        myconf['metadata']['namespace'] = self.namespace
        myconf['spec']['template']['spec']['containers'][0]['env'][0]['value']  = self.gitRemoteRepository
        myconf['spec']['template']['spec']['containers'][0]['env'][1]['value']  = self.gitBranch
        myconf['spec']['template']['spec']['containers'][0]['env'][4]['value']  = self.project
        myconf['spec']['template']['spec']['containers'][0]['env'][5]['value']  = self.environmentType
        myconf['spec']['template']['spec']['containers'][0]['env'][6]['value']  = self.bitesizeFile
        myconf['spec']['template']['spec']['containers'][0]['env'][11]['value'] = self.environment
        myconf['spec']['template']['spec']['containers'][0]['env'][12]['value'] = self.awsRegion
        myconf['spec']['template']['spec']['containers'][0]['env'][13]['value'] = self.environmentType
        myconf['spec']['template']['spec']['containers'][0]['image']            = self.image + ':' + self.imageVersion

        return myconf
