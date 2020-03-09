import base64

from st2common.runners.base_action import Action

secrettemplate = {
    "kind": "Secret",
    "apiVersion": "v1",
    "metadata": {
        "name": "",
        "namespace": ""
    },
    "data": {}
}


class CreateEOSecretTemplate(Action):

    def run(self, namespace, name, secrets, isSecretEncrypted):

        self.namespace         = namespace
        self.name              = name
        self.secrets           = secrets
        self.isSecretEncrypted = isSecretEncrypted

        return (True, self._createSecretConfig())

    def _createSecretConfig(self):

        sdata = {}
        for key in self.secrets:
            value = self.secrets[key]
            sdata[key] = value if self.isSecretEncrypted else base64.b64encode(value.replace('\\n', '\n'))

        mysecret                          = secrettemplate
        mysecret['metadata']['name']      = self.name
        mysecret['metadata']['namespace'] = self.namespace
        mysecret['data']                  = sdata

        return mysecret
