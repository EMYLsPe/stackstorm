#!/bin/sh


cp ./create_eo.yaml /opt/stackstorm/packs/bitesize/actions/workflows/
cp ../delete/delete_eo.yaml /opt/stackstorm/packs/bitesize/actions/workflows/

cp ./* /opt/stackstorm/packs/bitesize/actions/
cp ../delete/* /opt/stackstorm/packs/bitesize/actions/

cd /opt/stackstorm/packs/bitesize/actions/

st2 action create create_eo.meta.yaml
st2 action create set_eo_deployment.yaml
st2 action create set_eo_ingress.yaml
st2 action create set_eo_istio_role_binding.yaml
st2 action create set_eo_limits.yaml
st2 action create set_eo_role.yaml
st2 action create set_eo_secrets.yaml
st2 action create set_eo_svc.yaml
#st2 action create create_eo_route53_entry.yaml

st2 action create delete_eo.meta.yaml
