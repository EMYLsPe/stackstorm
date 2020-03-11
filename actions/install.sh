#!/bin/sh


mv ./create_eo.yaml /opt/stackstorm/packs/bitesize/actions/workflows/
mv ./delete/delete_eo.yaml /opt/stackstorm/packs/bitesize/actions/workflows/

mv ./* /opt/stackstorm/packs/bitesize/actions/
mv ./delete/* /opt/stackstorm/packs/bitesize/actions/

cd /opt/stackstorm/packs/bitesize/actions/

st2 action create create_eo.meta.yaml
st2 action create set_eo_deployment.yaml
st2 action create set_eo_ingress.yaml
st2 action create set_eo_istio_role_binding.yaml
st2 action create set_eo_limits.yaml
st2 action create set_eo_role.yaml
st2 action create set_eo_secrets.yaml
st2 action create set_eo_svc.yaml

st2 action create delete_eo.meta.yaml
