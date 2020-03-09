from st2common.runners.base_action import Action

ingress = {
    "kind": "Ingress",
    "apiVersion": "extensions/v1beta1",
    "metadata": {
        "namespace": "",
        "name": "environment-operator"
    },
    "spec": {
        "rules": [
          {
            "host": "",
            "http": {
              "paths": [
                {
                  "path": "/",
                  "backend": {
                    "serviceName": "environment-operator",
                    "servicePort": 80
                  }
                }
              ]
            }
          }
        ]
    }
}


class CreateEOIngress(Action):

    def run(self, namespace, ingressHost):

        self.namespace   = namespace
        self.ingressHost =  ingressHost

        return (True, self._createIngressConfig())

    def _createIngressConfig(self):
        myconf = ingress
        myconf['metadata']['namespace']    = self.namespace
        myconf['spec']['rules'][0]['host'] = self.ingressHost

        if self.ingressHost is None:
            myconf['spec']['rules'][0]['host'] = "environment-operator." + self.namespace + ".bite.pearsondev.tech"
        else:
            myconf['spec']['rules'][0]['host'] = self.ingressHost

        return myconf
